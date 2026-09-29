"""Keep only the columns the starter notebook uses from the two OSF task files (ps38n).
The originals (about 38 MB each, 99 columns) are in all_analyses/behavioural_analyses/analyses/ at https://osf.io/ps38n/.
Usage: python slim_stress_files.py reversal_n427.csv signal_n427.csv"""
import sys, pandas as pd
COLS = ["Prolific.ID", "Age.in.years", "Gender", "Highest.level.of.education", "State.of.residence",
        "myCount", "gameCount", "rewardGain", "Resp.keys", "Resp.corr", "Resp.rt", "Resp_3.keys", "Resp_3.corr", "Resp_3.rt"]
for path in sys.argv[1:]:
    pd.read_csv(path, low_memory=False)[COLS].to_csv(path, index=False)
    print("slimmed", path)
