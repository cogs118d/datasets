"""Convert the Dryad file Rutledge_GBE_risk_data_TOD.mat into three tidy CSV tables.

Source: Rutledge, R. B. Risky decision and happiness task: The Great Brain Experiment smartphone app.
Dryad, https://doi.org/10.5061/dryad.prr4xgxkk (CC0). Column meanings follow the dataset README.

Usage:  python convert_rutledge.py path/to/Rutledge_GBE_risk_data_TOD.mat
Writes: rutledge_trials.csv.gz, rutledge_people.csv, rutledge_depression.csv
"""
import sys
import numpy as np
import pandas as pd
from scipy.io import loadmat

mat = loadmat(sys.argv[1], squeeze_me=True, struct_as_record=False)

people, trials = [], []
for s in mat["subjData"]:
    people.append({"player": int(s.id), "age_code": int(s.age), "female": int(s.isFemale),
                   "education_code": int(s.education), "location_code": int(s.location),
                   "native_language_code": (None if np.isnan(np.float64(s.nativeLanguage)) else int(s.nativeLanguage)),
                   "device": s.deviceType, "life_satisfaction": s.lifeSatisfaction, "n_plays": int(s.nPlays)})
    plays = [s.data] if np.ndim(s.data) == 2 and s.data.dtype != object else list(s.data)
    days, tods, vers = (np.atleast_1d(s.dayNumber), np.atleast_1d(s.timeOfDay), np.atleast_1d(s.designVersion))
    for i, m in enumerate(plays):
        m = np.asarray(m, dtype=float)
        trials.append(pd.DataFrame({
            "player": int(s.id), "play": i + 1, "trial": m[:, 0].astype(int),
            "sure_amount": m[:, 2], "gamble_win": m[:, 3], "gamble_lose": m[:, 4],
            "chose_gamble": m[:, 6].astype(int), "outcome": m[:, 7], "choice_rt": m[:, 8].round(3),
            "happiness": m[:, 9], "day_number": days[i],
            "time_of_day_gmt": round(float(tods[i]) * 24, 2), "design_version": int(vers[i])}))

pd.concat(trials, ignore_index=True).to_csv("rutledge_trials.csv.gz", index=False, compression="gzip")
pd.DataFrame(people).to_csv("rutledge_people.csv", index=False)
pd.DataFrame([{"player": int(d.id), "bdi_total": d.bdiTotal, "dep_status": d.depStatus,
               "dep_meds": d.depMeds, "dep_family": d.depFamily} for d in mat["depData"]]
             ).to_csv("rutledge_depression.csv", index=False)
print("done")
