# Data sources and licenses

Every file in `data/` is a copy (or a lightly reformatted copy) of a public dataset. Please cite the original source in your homework. **Check each license before making this repository public**; licenses marked "not verified" could not be confirmed when the repo was assembled (September 2026).

| Folder | Original source | Changes in this repo | License |
| --- | --- | --- | --- |
| `01_risk_sensitivity` | [nivlab/RiskData](https://github.com/nivlab/RiskData) (Radulescu, Holmes & Niv, 2020) | None. Authors' README copied as `SOURCE_README.md` | Not verified (no license file in the source repo) |
| `02_olist` | [Olist, Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) | Only the 5 tables the notebook uses (of 9) | Not verified; see the Kaggle page (reported as CC BY-NC-SA 4.0) |
| `03_hotels` | Antonio, de Almeida & Nunes (2019), [Data in Brief](https://doi.org/10.1016/j.dib.2018.11.126); [TidyTuesday version](https://github.com/rfordatascience/tidytuesday/tree/master/data/2020/2020-02-11) | None (TidyTuesday's combined file) | CC BY 4.0 (published with the article) |
| `04_nba_shots` | [NBA shot logs, Kaggle](https://www.kaggle.com/datasets/dansbecker/nba-shot-logs) | None | Not verified; see the Kaggle page |
| `05_lichess` | [Chess Game Dataset (Lichess), Kaggle](https://www.kaggle.com/datasets/datasnaek/chess) | None (the notebook removes 945 duplicate games) | Not verified; see the Kaggle page |
| `06_bikeshare` | [ISLP `Bikeshare`](https://islp.readthedocs.io/en/latest/datasets/Bikeshare.html), from the [UCI Bike Sharing Dataset](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset) (Fanaee-T & Gama, 2014) | None | UCI: CC BY 4.0 |
| `07_rutledge_happiness` | Rutledge, [Dryad](https://doi.org/10.5061/dryad.prr4xgxkk) | MATLAB file converted to 3 CSV tables with `scripts/convert_rutledge.py`; authors' README included | Dryad: CC0 |
| `08_stress_anxiety` | [OSF ps38n](https://osf.io/ps38n/) (Guitart-Masip, Walsh, Dayan & Olsson, 2023) | Two task files trimmed to 14 columns with `scripts/slim_stress_files.py` | Not verified; see the OSF project page |

If a license doesn't allow redistribution, delete that folder and point the notebook's `BASE_URL` back at the original source (each original link is above).
