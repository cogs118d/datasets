# COGS 118D Dataset Guide

Pick one of these eight datasets and use it for HW 1, HW 2 and HW 3. Every dataset has a starter Colab notebook that loads, cleans and plots the data, then leaves the analysis to you.

## Getting started

1. Read the guide below and pick a dataset.
2. Click its **Open in Colab** badge. Colab opens a copy of the starter notebook that loads the data straight from this repository.
3. *File → Save a copy in Drive* so your work is saved, then run the cells from the top.

| # | Dataset | Starter notebook | Data |
| --- | --- | --- | --- |
| 1 | Risk Sensitivity | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR-GITHUB-USERNAME/cogs118d-datasets/blob/main/notebooks/01_risk_sensitivity_starter.ipynb) [`01_risk_sensitivity_starter.ipynb`](notebooks/01_risk_sensitivity_starter.ipynb) | [`data/01_risk_sensitivity/`](data/01_risk_sensitivity/) |
| 2 | Olist E-Commerce | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR-GITHUB-USERNAME/cogs118d-datasets/blob/main/notebooks/02_olist_starter.ipynb) [`02_olist_starter.ipynb`](notebooks/02_olist_starter.ipynb) | [`data/02_olist/`](data/02_olist/) |
| 3 | Hotel Bookings | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR-GITHUB-USERNAME/cogs118d-datasets/blob/main/notebooks/03_hotels_starter.ipynb) [`03_hotels_starter.ipynb`](notebooks/03_hotels_starter.ipynb) | [`data/03_hotels/`](data/03_hotels/) |
| 4 | NBA Shot Logs | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR-GITHUB-USERNAME/cogs118d-datasets/blob/main/notebooks/04_nba_shots_starter.ipynb) [`04_nba_shots_starter.ipynb`](notebooks/04_nba_shots_starter.ipynb) | [`data/04_nba_shots/`](data/04_nba_shots/) |
| 5 | Lichess Games | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR-GITHUB-USERNAME/cogs118d-datasets/blob/main/notebooks/05_lichess_starter.ipynb) [`05_lichess_starter.ipynb`](notebooks/05_lichess_starter.ipynb) | [`data/05_lichess/`](data/05_lichess/) |
| 6 | Bikeshare | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR-GITHUB-USERNAME/cogs118d-datasets/blob/main/notebooks/06_bikeshare_starter.ipynb) [`06_bikeshare_starter.ipynb`](notebooks/06_bikeshare_starter.ipynb) | [`data/06_bikeshare/`](data/06_bikeshare/) |
| 7 | Risk and Happiness (Rutledge) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR-GITHUB-USERNAME/cogs118d-datasets/blob/main/notebooks/07_rutledge_happiness_starter.ipynb) [`07_rutledge_happiness_starter.ipynb`](notebooks/07_rutledge_happiness_starter.ipynb) | [`data/07_rutledge_happiness/`](data/07_rutledge_happiness/) |
| 8 | Stress and Anxiety | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR-GITHUB-USERNAME/cogs118d-datasets/blob/main/notebooks/08_stress_anxiety_starter.ipynb) [`08_stress_anxiety_starter.ipynb`](notebooks/08_stress_anxiety_starter.ipynb) | [`data/08_stress_anxiety/`](data/08_stress_anxiety/) |

Working on your own computer instead? Clone the repo and, in the notebook's Settings cell, switch `BASE_URL` to the local `../data/...` line.

## At a glance

All eight support HW 1 and HW 2. They differ most on HW 3: pick a dataset whose HW 3 column says **Strong** or **Good** for the method you want to learn.

| Dataset | Field | One row is | Size | HW 1: Describe | HW 2: Predict / Moderate / Mediate | HW 3: Mixed effects | HW 3: Survival | Data in this repo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1. Risk Sensitivity | Psychology (online experiment) | one choice or rating | 563 people; 99,088 learning-task trials | Strong | Strong for all three | **Strong**: trials within people; people crossed with activities | Not appropriate | Yes |
| 2. Olist E-Commerce | Online shopping | one order | 99,441 orders, 2016–2018 | Strong | Strong for all three | Moderate: orders within sellers | **Strong**: days until delivery | Yes |
| 3. Hotel Bookings | Hospitality | one booking | 119,390 bookings, 2015–2017 | Strong | Strong for prediction and moderation; weak for mediation | **Good**: bookings within agents and countries | **Strong**: days until cancellation | Yes |
| 4. NBA Shot Logs | Sports | one shot | 128,069 shots by 281 players, 2014–15 | Strong | Strong for all three | **Good**: shots within players, games and defenders | Not appropriate | Yes |
| 5. Lichess Games | Online games | one game | 19,113 games | Strong | Strong for all three | Weak: most players appear once | **Good**: moves until a decisive ending | Yes |
| 6. Bikeshare | Transportation | one hour | 8,645 hours in 2011 | Strong | Strong for prediction (counts) and moderation; mediation not natural | **Good**: hours within days | Not appropriate | Yes |
| 7. Risk and Happiness (Rutledge) | Psychology (smartphone app) | one trial | 47,067 people; 2.7 million trials | Strong | Strong for all three | **Strong**: trials within plays within people | Weak: censoring is approximate | Yes (converted to CSV) |
| 8. Stress and Anxiety | Psychology (online experiment) | one trial | 427 people; 107,869 trials | Strong | Strong for all three | **Strong**: trials within people | Not appropriate | Yes (trimmed to needed columns) |

**Two things to know before you choose.** The four psychology datasets have many rows per person, which makes them natural for mixed-effects models. Olist, Hotels and Lichess are the best choices if you want to do survival analysis in HW 3.

## 1. Risk Sensitivity

563 online participants each completed three different measures of risk-taking plus a personality questionnaire, so you can ask whether "risk-taking" is one trait or several.

- **Starter notebook:** [`notebooks/01_risk_sensitivity_starter.ipynb`](notebooks/01_risk_sensitivity_starter.ipynb) · data in [`data/01_risk_sensitivity/`](data/01_risk_sensitivity/)
- **Source:** [nivlab/RiskData on GitHub](https://github.com/nivlab/RiskData). The authors' README is copied here as `SOURCE_README.md`.
- **Academic paper:** Radulescu, A., Holmes, K., & Niv, Y. (2020). [On the convergent validity of risk sensitivity measures](https://psyarxiv.com/qdhx4). *PsyArXiv* preprint.

### What's in it

- **Gambles from description** (Holt–Laury): 10 choices between a safer gamble A and a riskier gamble B. The odds of the good outcome rise from question 1 to 10. One row per choice.
- **Gambles from experience:** a 176-trial learning task with four options that pay 0, 2 or 4 cents. On "risk trials," people choose between a sure 2 cents and a 50/50 chance of 0 or 4. One row per trial.
- **DOSPERT:** 30 everyday risky activities, each rated 1–7 for benefit, risk, and how likely the person is to do it.
- **BIS/BAS:** 24 items measuring sensitivity to punishment (BIS) and reward (BAS drive, fun seeking, reward responsiveness).

### Research questions it can support

- Do people who gamble in one task also take risks in the other tasks and in daily life?
- How fast do people learn which option pays more, and do they differ?
- After the risky option pays off, are people more likely to choose it again?
- Do people do risky activities because they see more benefit, or because they see less risk?
- Are reward-sensitive people (high BAS) bigger risk-takers?

### Important variables

| Variable | Table | Type | Use as |
| --- | --- | --- | --- |
| `chose_risky` | `hl` (description) | 0/1 | Outcome |
| `chose_better` | `df` (learning task) | 0/1 | Outcome |
| `chose_risky` | `df` (risk trials only) | 0/1 | Outcome |
| `likelihood` | `dospert_wide` | 1–7 rating | Outcome |
| `question`, `trial`, `trialtype` | `hl`, `df` | Numbers / categories | Predictor |
| previous trial's outcome | `df` (you create it) | Number | Predictor |
| `benefit`, `risk` | `dospert_wide` | 1–7 rating | Predictor or mediator |
| `bis`, `bas_drive`, `bas_fun_seeking`, `bas_reward` | `people` | Scale score | Predictor |
| `subj`, `activity` | all | ID | Grouping variables |

### Limitations

- Stakes are a few cents, so the tasks may not reflect real-life risk.
- The public files have no age, gender or other demographics.
- The learning task's payoffs and the BIS/BAS item order are reconstructed from the data and the README. Check the paper before you interpret trial types.
- The questionnaire relationships are correlational, not experimental.
- The tables have different grains (choice, rating, person). Say which one you are analyzing.

### Homework starting points

| HW | Starting question | Analysis |
| --- | --- | --- |
| HW 1 | How does the share choosing the risky gamble change across the 10 description questions? | Describe a trend |
| HW 1 | How does accuracy in the learning task change across trials, and how much do people differ? | Describe learning |
| HW 1 | How are benefit, risk and likelihood ratings related across people and activities? | Describe relationships |
| HW 2 | How well do trial number, trial type and the last outcome predict choosing the better option in held-out data? | Prediction |
| HW 2 | Does the pull of a recent win on the risky option change as the task goes on? | Moderation |
| HW 2 | Does perceived risk lower the likelihood of an activity *through* lower perceived benefit? | Mediation |
| HW 2 | Do BIS/BAS scores predict how many safe choices someone makes? | Prediction |
| HW 3 | How much does risky choice vary between people? Model learning with a random intercept (and slope) for each person. | **Mixed effects** |
| HW 3 | Model DOSPERT likelihood with crossed random effects for people and activities. | **Mixed effects** |
| HW 3 | Survival analysis | **Not appropriate.** No task measures time until an event. Use mixed effects. |

## 2. Olist Brazilian E-Commerce

About 99,000 real, anonymized orders placed from September 2016 to October 2018 on Olist, a Brazilian marketplace that connects small sellers to shoppers. Most orders have a 1–5 star review, so you can study what makes customers unhappy.

- **Starter notebook:** [`notebooks/02_olist_starter.ipynb`](notebooks/02_olist_starter.ipynb) · data in [`data/02_olist/`](data/02_olist/)
- **Source:** [Brazilian E-Commerce Public Dataset by Olist on Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) (free Kaggle account; check the license on that page). This repo includes the five tables the notebook uses.
- **Academic paper:** None. The data were released by the company.

### What's in it

The data come as several linked tables (orders, items, sellers, customers, reviews). The notebook joins them into **one row per order** with the purchase date, delivery dates, the promised delivery date, price, shipping cost, the seller's and customer's states, and the review score.

### Research questions it can support

- How much does late delivery hurt review scores?
- Do orders shipped between states take longer, and does that explain worse reviews?
- Are some sellers consistently better or worse than others?
- Which orders take longest to arrive, and what predicts a fast delivery?

### Important variables

| Variable | Type | Use as |
| --- | --- | --- |
| `review_score` | 1–5 stars | Outcome |
| `low_review` | 0/1 (1–2 stars) | Outcome |
| `delivery_days` | Days | Outcome, predictor or mediator |
| `late` | 0/1 (after the promised date) | Outcome or predictor |
| `cross_state` | 0/1 | Predictor |
| `price`, `freight`, `n_items` | Numbers | Predictor |
| `promised_days` | Days | Predictor |
| `customer_state`, `seller_state` | 27 states | Predictor or grouping |
| `seller_id` | ID | Grouping variable |
| `time_days`, `event_delivered` | Days, 0/1 | Survival time and event (table `surv`) |

### Limitations

- Observational: late orders may differ from on-time orders in many ways besides lateness.
- Only customers who chose to leave a review are rated, and reviews are strongly skewed toward 5 stars.
- Orders that were canceled or never delivered have no delivery date. Decide whether to drop them and say so.
- Customers almost never order twice, so customers are not a useful grouping variable. Most sellers have only a handful of orders.
- A few orders contain several items from different sellers. The notebook keeps the first seller.

### Homework starting points

| HW | Starting question | Analysis |
| --- | --- | --- |
| HW 1 | What does the distribution of review scores look like, and how does it differ for late vs. on-time orders? | Describe group differences |
| HW 1 | How long does delivery take, and how does it vary by customer state? | Describe distributions |
| HW 2 | How well can you predict a low review (1–2 stars) in held-out orders? How much does delivery information add? | Prediction |
| HW 2 | Does lateness hurt reviews more for orders with several items? | Moderation |
| HW 2 | Do cross-state orders get worse reviews *because* they take longer to arrive? | Mediation |
| HW 3 | How much do review scores vary between sellers? Fit orders nested within sellers. | **Mixed effects** (moderate: many sellers have few orders) |
| HW 3 | What predicts how long an order takes to arrive? Orders still in transit are censored. | **Survival** (strong fit) |

## 3. Hotel Booking Demand

119,390 real bookings at two hotels in Portugal, a resort hotel in the Algarve and a city hotel in Lisbon, for arrivals between July 2015 and August 2017. About 37% of bookings were canceled, and the data record what was known when each booking was made.

- **Starter notebook:** [`notebooks/03_hotels_starter.ipynb`](notebooks/03_hotels_starter.ipynb) · data in [`data/03_hotels/`](data/03_hotels/)
- **Source:** Published with the paper below. This repo includes the cleaned [TidyTuesday version](https://github.com/rfordatascience/tidytuesday/tree/master/data/2020/2020-02-11), which combines the two hotels into one file.
- **Academic paper:** Antonio, N., de Almeida, A., & Nunes, L. (2019). [Hotel booking demand datasets](https://doi.org/10.1016/j.dib.2018.11.126). *Data in Brief, 22*, 41–49.

### What's in it

One row per booking with 32 columns: which hotel, lead time (days between booking and arrival), arrival date, length of stay, adults and children, meal plan, guest's country, booking channel and agent, deposit type, repeat-guest status, earlier cancellations, special requests, average daily price (`adr`, in euros), and whether the booking was canceled.

### Research questions it can support

- Are bookings made far in advance more likely to be canceled?
- Do repeat guests cancel less, and does that depend on how early they booked?
- Does price or season affect cancellations?
- How quickly after booking do cancellations happen, and what speeds them up?

### Important variables

| Variable | Type | Use as |
| --- | --- | --- |
| `is_canceled` | 0/1 | Outcome |
| `adr` | Euros per night | Outcome or predictor |
| `total_of_special_requests` | Count | Outcome or predictor |
| `lead_time` | Days | Predictor |
| `hotel` | Resort / City | Predictor |
| `deposit_type`, `market_segment`, `customer_type` | Categories | Predictor |
| `is_repeated_guest`, `previous_cancellations` | 0/1, count | Predictor |
| `agent`, `country` | IDs / codes | Grouping variables |
| `time_days`, `event_canceled` | Days, 0/1 | Survival time and event (table `surv`) |

### Limitations

- **Leakage:** `reservation_status` and `reservation_status_date` are recorded *after* the outcome. Don't use them as predictors of cancellation.
- `deposit_type = "Non Refund"` bookings were canceled 99% of the time, which is the opposite of what you'd expect. Treat it as a data quirk and say how you handle it.
- `adr` has a negative value and one of 5,400 euros. Check for outliers before modeling price.
- `company` is missing for 94% of bookings. Agent and company are anonymized ID numbers.
- Only two hotels, and no guest IDs, so you can't follow individual guests.

### Homework starting points

| HW | Starting question | Analysis |
| --- | --- | --- |
| HW 1 | How does the cancellation rate differ between the two hotels and across arrival months? | Describe group differences |
| HW 1 | How is lead time distributed, and how does it differ for canceled vs. kept bookings? | Describe distributions |
| HW 2 | How well can you predict cancellation in held-out bookings? Which predictors matter most? | Prediction |
| HW 2 | Is the link between lead time and cancellation different for repeat guests, or for the two hotels? | Moderation |
| HW 2 | Does lead time affect cancellation through the number of special requests? | Mediation (expect a weak or null result) |
| HW 3 | How much do cancellation rates vary across booking agents or countries? | **Mixed effects** |
| HW 3 | How long after booking do cancellations happen? Bookings that were kept are censored at arrival. | **Survival** (strong fit) |

## 4. NBA Shot Logs 2014–15

Every tracked shot from October 28, 2014 to March 4, 2015 of the NBA season: 128,069 shots by 281 players. Player-tracking cameras recorded how far each shot was from the basket and how close the nearest defender was.

- **Starter notebook:** [`notebooks/04_nba_shots_starter.ipynb`](notebooks/04_nba_shots_starter.ipynb) · data in [`data/04_nba_shots/`](data/04_nba_shots/)
- **Source:** [NBA shot logs on Kaggle](https://www.kaggle.com/datasets/dansbecker/nba-shot-logs) (free Kaggle account), originally scraped from the NBA's stats website.
- **Academic paper:** None.

### What's in it

One row per shot: the shooter, the game, home or away, period and game clock, shot clock, number of dribbles, how long the shooter held the ball (touch time), shot distance, 2- or 3-pointer, the closest defender and their distance, and whether the shot went in.

### Research questions it can support

- How quickly does shooting accuracy fall with distance?
- Does a close defender lower the chance of making a shot, and does that depend on distance?
- Do players shoot worse late in the shot clock, or after many dribbles?
- How much do players differ in accuracy once you account for where they shoot from?

### Important variables

| Variable | Type | Use as |
| --- | --- | --- |
| `FGM` | 0/1 (made) | Outcome |
| `PTS` | 0, 2 or 3 | Outcome |
| `SHOT_DIST` | Feet | Predictor |
| `CLOSE_DEF_DIST` | Feet | Predictor or mediator |
| `SHOT_CLOCK` | Seconds left | Predictor |
| `DRIBBLES`, `TOUCH_TIME` | Count, seconds | Predictor or mediator |
| `home`, `PERIOD`, `three_pointer` | 0/1, 1–7, 0/1 | Predictor |
| `player_id`, `GAME_ID`, `CLOSEST_DEFENDER_PLAYER_ID` | IDs | Grouping variables |

### Limitations

- Players choose when and where to shoot, so every predictor is tangled up with shot selection. For example, defenders stand closer on short shots, which can hide the effect of defender distance.
- Tracking errors: 312 negative touch times (set to missing), and some 3-pointers have impossibly short recorded distances.
- `SHOT_CLOCK` is missing for about 4% of shots, mostly when the game clock had less than 24 seconds left.
- Only part of one season. Game results (`W`, `FINAL_MARGIN`) are known only after the game, so don't use them to predict individual shots.

### Homework starting points

| HW | Starting question | Analysis |
| --- | --- | --- |
| HW 1 | How does the make rate change with shot distance? Where do shots come from? | Describe relationships |
| HW 1 | How does the make rate change with defender distance? Is the pattern what you expected? | Describe relationships |
| HW 2 | How well do distance, defender distance, shot clock and dribbles predict makes in held-out shots? | Prediction |
| HW 2 | Does a close defender matter more on long shots or short shots? | Moderation |
| HW 2 | Does shot distance affect accuracy partly through how closely the shot is defended? | Mediation |
| HW 3 | How much do players differ in accuracy? Fit shots nested within shooters, possibly crossed with games or defenders. | **Mixed effects** |
| HW 3 | Survival analysis | **Not appropriate.** Every shot happens; there is no waiting time or censoring. Use mixed effects. |

## 5. Lichess Chess Games

About 20,000 online chess games from Lichess.org (19,113 after removing duplicates), with both players' ratings, the time control, the opening, the number of moves and how each game ended.

- **Starter notebook:** [`notebooks/05_lichess_starter.ipynb`](notebooks/05_lichess_starter.ipynb) · data in [`data/05_lichess/`](data/05_lichess/)
- **Source:** [Chess Game Dataset (Lichess) on Kaggle](https://www.kaggle.com/datasets/datasnaek/chess) (free Kaggle account), collected through the Lichess API.
- **Academic paper:** None.

### What's in it

One row per game: whether it was rated, the time control (for example `15+2` = 15 minutes plus 2 seconds per move), number of moves (`turns`), how it ended (checkmate, resignation, time-out or draw), the winner, both players' IDs and ratings, the moves themselves, and the opening name and code.

### Research questions it can support

- How strongly does a rating advantage predict winning?
- Does rating matter more in rated games than in casual games?
- Do stronger players draw more, and is that because their games last longer?
- How long do games last before someone is checkmated or resigns?

### Important variables

| Variable | Type | Use as |
| --- | --- | --- |
| `white_won` | 0/1 (draws excluded) | Outcome |
| `winner` | White / Black / draw | Outcome |
| `turns` | Count of moves | Outcome, predictor or mediator |
| `victory_status` | Mate / resign / out of time / draw | Outcome |
| `rating_diff`, `mean_rating` | Rating points | Predictor |
| `rated` | 0/1 | Predictor or moderator |
| `base_minutes`, `increment_seconds` | Minutes, seconds | Predictor |
| `opening_eco`, `opening_ply` | Code, count | Predictor |
| `time_moves`, `event_decisive` | Moves, 0/1 | Survival time and event |

### Limitations

- The games come from a selection of Lichess users, not a random sample of all games.
- The original file contains 945 duplicate games. The notebook removes them.
- Most players appear in only one game, so mixed-effects models by player don't work well.
- The `created_at` and `last_move_at` timestamps are unreliable. Use `turns` as the measure of game length.
- Only about 5% of games are draws, so draw models have few events.

### Homework starting points

| HW | Starting question | Analysis |
| --- | --- | --- |
| HW 1 | How does White's win rate change with the rating difference? | Describe relationships |
| HW 1 | How are game lengths distributed, and do they differ by how the game ended? | Describe distributions |
| HW 2 | How well do ratings, time control and opening predict the winner in held-out games? | Prediction |
| HW 2 | Does a rating advantage matter more in rated games than in casual games? | Moderation |
| HW 2 | Do higher-rated games end in draws more often *because* they last longer? | Mediation |
| HW 3 | Mixed effects | **Weak fit.** Most players have one game. Only try it if you restrict to players with 10 or more games. |
| HW 3 | How many moves until a game ends by checkmate or resignation? Draws and time-outs are censored. | **Survival** (the more natural choice here) |

## 6. Capital Bikeshare

Hourly counts of bike rentals from the Capital Bikeshare system in Washington, D.C. for 2011 (8,645 hours), with the weather and calendar for each hour. Each row is an hour, not a person: the outcome is how many people rented a bike.

- **Starter notebook:** [`notebooks/06_bikeshare_starter.ipynb`](notebooks/06_bikeshare_starter.ipynb) · data in [`data/06_bikeshare/`](data/06_bikeshare/)
- **Source:** The `Bikeshare` data from the [ISLP textbook package](https://islp.readthedocs.io/en/latest/datasets/Bikeshare.html). The full two-year version is on the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset).
- **Academic paper:** Fanaee-T, H., & Gama, J. (2014). [Event labeling combining ensemble detectors and background knowledge](https://doi.org/10.1007/s13748-013-0040-3). *Progress in Artificial Intelligence, 2*, 113–127.

### What's in it

One row per hour: month, day of the year, hour, holiday, day of the week, working day, weather type, temperature, "feels like" temperature, humidity and wind speed, plus rental counts for casual riders, registered members, and the total (`bikers`).

### Research questions it can support

- How do rentals change over the day, and is the daily pattern different on working days?
- How much do temperature, humidity and rain matter?
- Does warm weather boost casual riders more than commuters?
- Which hours and conditions have unusually high or low demand?

### Important variables

| Variable | Type | Use as |
| --- | --- | --- |
| `bikers` | Count per hour | Outcome |
| `casual`, `registered` | Counts per hour | Outcome |
| `hr` | Hour 0–23 | Predictor (usually as a category) |
| `workingday`, `holiday`, `weekday` | 0/1, 0/1, 0–6 | Predictor or moderator |
| `weathersit` | 4 weather types | Predictor |
| `temp`, `atemp`, `hum`, `windspeed` | Rescaled to 0–1 | Predictor |
| `mnth`, `season` | Categories | Predictor |
| `day` | Day of year 1–365 | Grouping variable |

### Limitations

- Counts, not people: you can't say anything about individual riders.
- Neighboring hours are strongly correlated (time-series data), so treating hours as independent overstates certainty.
- Weather is rescaled (for example, `temp` = °C / 41). The notebook adds `temp_celsius`.
- Only one hour has "heavy rain/snow." Merge it with light rain before modeling weather.
- The counts are far more spread out than a Poisson model allows. Expect to need a negative binomial model.

### Homework starting points

| HW | Starting question | Analysis |
| --- | --- | --- |
| HW 1 | How do average rentals change over the day on working days vs. weekends? | Describe patterns |
| HW 1 | How do rentals relate to temperature and weather type? | Describe relationships |
| HW 2 | How well do hour, working day and weather predict rentals in held-out hours? Poisson or negative binomial? | Prediction (count model) |
| HW 2 | Is the daily rhythm different on working days? Does temperature matter more on weekends? | Moderation |
| HW 2 | Mediation | **Not natural here.** The weather variables aren't a causal chain. Focus on prediction and moderation. |
| HW 3 | How much of the variation in rentals is between days? Fit hours nested within days. | **Mixed effects** |
| HW 3 | Survival analysis | **Not appropriate.** These are counts per hour, not times until an event. Use mixed effects. |

## 7. Risky Decisions and Happiness (Rutledge, Great Brain Experiment)

47,067 people played *What makes me happy?* in The Great Brain Experiment smartphone app between 2013 and 2015. On every trial they chose between a sure amount of points and a 50/50 gamble. Every 2–3 trials they rated "How happy are you right now?" from 0 to 100.

- **Starter notebook:** [`notebooks/07_rutledge_happiness_starter.ipynb`](notebooks/07_rutledge_happiness_starter.ipynb) · data in [`data/07_rutledge_happiness/`](data/07_rutledge_happiness/)
- **Source:** Rutledge, R. B. [Risky decision and happiness task: The Great Brain Experiment smartphone app](https://doi.org/10.5061/dryad.prr4xgxkk). Dryad. The original is a MATLAB file; this repo has it converted to three CSV tables (by `scripts/convert_rutledge.py`) plus the authors' README with every variable's codes.
- **Academic papers** (the README asks you to cite the ones you use):
  - Rutledge, R. B., Skandali, N., Dayan, P., & Dolan, R. J. (2014). [A computational and neural model of momentary subjective well-being](https://doi.org/10.1073/pnas.1407535111). *PNAS, 111*, 12252–12257.
  - Rutledge, R. B., Smittenaar, P., Zeidman, P., et al. (2016). [Risk taking for potential reward decreases across the lifespan](https://doi.org/10.1016/j.cub.2016.05.017). *Current Biology, 26*, 1634–1639.
  - Rutledge, R. B., Moutoussis, M., Smittenaar, P., et al. (2017). [Association of neural and emotional impacts of reward prediction errors with major depression](https://doi.org/10.1001/jamapsychiatry.2017.1713). *JAMA Psychiatry, 74*, 790–797.
  - Bedder, R. L., Vaghi, M. M., Dolan, R. J., & Rutledge, R. B. (2023). [Risk taking for potential losses but not gains increases with time of day](https://doi.org/10.1038/s41598-023-31738-x). *Scientific Reports, 13*, 5534.

### What's in it

Each play has 30 trials: 11 **gain** trials (sure win vs. gamble between a bigger win and 0), 11 **loss** trials (sure loss vs. gamble between a bigger loss and 0), and 8 **mixed** trials (0 vs. gamble between a win and a loss). The notebook builds three tables:

- `df`: one row per trial, with the choice, the outcome, response time and the happiness rating when one was asked.
- `people`: one row per player, with age group, gender, education, region, device, life satisfaction and number of plays.
- `dep`: 1,858 players who also completed a depression questionnaire (BDI-II).

The full data have 2.7 million trials, so by default the notebook keeps a random 5,000 players plus everyone with a depression score. Change `N_PLAYERS` to use more.

### Research questions it can support

- Do people gamble more to avoid losses than to get gains?
- Does risk-taking change with age, and differently for gains and losses?
- Does happiness go up after wins and down after losses? Does it track *surprise* more than the outcome itself?
- Are more depressed people less happy during the game, and is that explained by their overall life satisfaction?

### Important variables

| Variable | Table | Type | Use as |
| --- | --- | --- | --- |
| `chose_gamble` | `df` | 0/1 | Outcome |
| `happiness` | `df` | 0–100 (every 2–3 trials) | Outcome |
| `choice_rt` | `df` | Seconds | Outcome |
| `trial_type` | `df` | Gain / loss / mixed | Predictor or moderator |
| `ev_advantage` | `df` | Points (gamble's average minus sure amount) | Predictor |
| `outcome`, `rpe` | `df` | Points | Predictor (for happiness) |
| `age_group`, `female`, `region`, `device` | `people` | Categories | Predictor or moderator |
| `life_satisfaction` | `people` | 0–10 | Predictor or mediator |
| `bdi_total` | `dep` | 0–63 | Predictor |
| `player`, `play` | all | IDs | Grouping variables |

### Limitations

- App users chose to play, so they aren't a representative sample (many are from the UK).
- Points aren't real money. Age is recorded in bins (18–24, 25–29, …).
- Happiness is asked only 12 times per play. Many ratings sit at exactly 50 (where the slider sometimes started), 0 or 100.
- The trial amounts changed between app versions 1–2 and 3–5 (`design_version`), and survey answers were overwritten for people who updated the app.
- `life_satisfaction` isn't described in the README's field table, so its exact question wording is unknown.
- Only 1,858 players have depression scores, and all depression analyses are correlational.

### Homework starting points

| HW | Starting question | Analysis |
| --- | --- | --- |
| HW 1 | How often do people gamble on gain, loss and mixed trials? How does it change as the gamble gets better? | Describe group differences |
| HW 1 | How is happiness distributed, and how does it differ by age group or depression score? | Describe distributions |
| HW 2 | How well do the gamble's value, trial type and age predict choosing the gamble for *new* players? | Prediction |
| HW 2 | Does the effect of age on gambling differ for gain, loss and mixed trials? | Moderation |
| HW 2 | Is depression linked to lower in-game happiness *through* lower life satisfaction? (one row per player) | Mediation |
| HW 3 | How much do happiness ratings vary between people? Does happiness track the latest outcome or reward prediction error, with trials nested in players? | **Mixed effects** (strong fit) |
| HW 3 | How long until a player plays again? | **Survival: weak fit.** The data don't say when each player stopped being observed, so censoring times are approximate. Choose mixed effects unless you've checked with the instructor. |

## 8. Stress, Anxiety and Reward Learning

427 adults from 47 countries, recruited on Prolific in April 2020 during the first COVID-19 wave, did two reward-learning tasks and filled in questionnaires on stress, anxiety, depression and COVID-19 risk. The question is whether stressed and anxious people learn differently when the world keeps changing.

- **Starter notebook:** [`notebooks/08_stress_anxiety_starter.ipynb`](notebooks/08_stress_anxiety_starter.ipynb) · data in [`data/08_stress_anxiety/`](data/08_stress_anxiety/)
- **Source:** [OSF project ps38n](https://osf.io/ps38n/). This repo includes `reversal_n427.csv`, `signal_n427.csv` and `merge_all_factor_427.csv` from `all_analyses/behavioural_analyses/analyses/`, with the two task files trimmed to the columns the notebook uses (`scripts/slim_stress_files.py`).
- **Academic paper:** Guitart-Masip, M., Walsh, A., Dayan, P., & Olsson, A. (2023). [Anxiety associated with perceived uncontrollable stress enhances expectations of environmental volatility and impairs reward learning](https://doi.org/10.1038/s41598-023-45179-z). *Scientific Reports, 13*, 18451.

### What's in it

On each trial, participants chose one of three pictures. One of them was the "target," which paid off more often.

- **Signalled task:** 5 games of 25 trials. The target pays off 75% of the time (the others 25%), and a new game means a new target.
- **Reversal task:** one game of about 125 trials. The target pays off 80% of the time and switches *without warning* every 20–30 trials.

The notebook builds `df` (one row per trial, both tasks) and `people` (one row per participant). Each participant has one score per questionnaire, computed by the authors and standardized so 0 is about average: state anxiety and trait anxiety (STAI), uncontrollable stress and self-efficacy (two parts of the Perceived Stress Scale), depression (PHQ-9) and COVID-19 risk.

### Research questions it can support

- How quickly do people find the target, and is it harder when changes aren't announced?
- After a loss, how often do people abandon the target, even though it usually pays?
- Do more anxious or stressed people learn more slowly, and only when the world changes without warning?
- Is the link between stress and learning explained by anxiety?

### Important variables

| Variable | Table | Type | Use as |
| --- | --- | --- | --- |
| `chose_target` | `df` | 0/1 | Outcome |
| `rt` | `df` | Seconds | Outcome |
| `trial_in_block`, `trial_overall` | `df` | Counts | Predictor |
| `task` | `df` | Signalled / reversal | Predictor or moderator |
| `prev_reward`, `prev_chose_target` | `df` | 0/1 | Predictor (win-stay / lose-shift) |
| `state_anxiety`, `trait_anxiety` | `df`, `people` | Standardized score | Predictor, moderator or mediator |
| `uncontrollable_stress`, `self_efficacy` | `df`, `people` | Standardized score | Predictor |
| `depression`, `covid_risk` | `df`, `people` | Standardized score | Predictor |
| `age`, `gender` | `people` | Years, category | Predictor |
| `participant`, `block` | `df` | IDs | Grouping variables |

### Limitations

- Stress and anxiety were measured, not manipulated, so their links to learning are correlational.
- Data were collected at an unusual moment (spring 2020), which may limit generalization.
- Gender, education and place of residence were typed in freely. The notebook cleans gender; the others need cleaning if you use them.
- 1,004 trials had no response and are set to missing.
- In the reversal task, a "block" is the stretch between target switches, which participants could not see.
- 427 people is a modest sample for questions about individual differences.

### Homework starting points

| HW | Starting question | Analysis |
| --- | --- | --- |
| HW 1 | How does the chance of choosing the target change within a block, in each task? | Describe learning curves |
| HW 1 | How are the questionnaire scores distributed and related? How often do people stay after a win vs. a loss? | Describe distributions and relationships |
| HW 2 | How well do trial position, the last reward and questionnaire scores predict choosing the target for *new* participants? | Prediction |
| HW 2 | Do more anxious people learn more slowly within a block? Is that only true in the reversal task? | Moderation |
| HW 2 | Is uncontrollable stress linked to leaving the target after a loss *through* state anxiety? (one row per participant) | Mediation |
| HW 3 | Fit trials nested within participants, with a random intercept and a random slope for trial in block. How much do people differ? | **Mixed effects** (strong fit) |
| HW 3 | Survival analysis | **Not a natural fit.** You could count trials until someone finds a new target, but that is a constructed measure. Use mixed effects. |

## Repository layout

```
data/        one folder per dataset (CSV files, plus the original authors' READMEs where available)
notebooks/   the eight starter notebooks
scripts/     how the Rutledge and Stress files were prepared, and configure_repo.py
```

See [DATA_SOURCES.md](DATA_SOURCES.md) for where each file came from and its license.

## Sources

Data sources and papers, in the order used above. Cite the dataset (and the paper, if there is one) in every homework.

- [nivlab/RiskData (GitHub)](https://github.com/nivlab/RiskData) · [Radulescu, Holmes & Niv (2020), PsyArXiv](https://psyarxiv.com/qdhx4)
- [Olist Brazilian E-Commerce (Kaggle)](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- [Antonio, de Almeida & Nunes (2019), Data in Brief](https://doi.org/10.1016/j.dib.2018.11.126) · [TidyTuesday hotels.csv](https://github.com/rfordatascience/tidytuesday/tree/master/data/2020/2020-02-11)
- [NBA shot logs (Kaggle)](https://www.kaggle.com/datasets/dansbecker/nba-shot-logs)
- [Chess Game Dataset, Lichess (Kaggle)](https://www.kaggle.com/datasets/datasnaek/chess)
- [ISLP Bikeshare](https://islp.readthedocs.io/en/latest/datasets/Bikeshare.html) · [UCI Bike Sharing Dataset](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset) · [Fanaee-T & Gama (2014)](https://doi.org/10.1007/s13748-013-0040-3)
- [Rutledge, Great Brain Experiment data (Dryad)](https://doi.org/10.5061/dryad.prr4xgxkk) · [Rutledge et al. (2014), PNAS](https://doi.org/10.1073/pnas.1407535111) · [Rutledge et al. (2016), Current Biology](https://doi.org/10.1016/j.cub.2016.05.017) · [Rutledge et al. (2017), JAMA Psychiatry](https://doi.org/10.1001/jamapsychiatry.2017.1713) · [Bedder et al. (2023), Scientific Reports](https://doi.org/10.1038/s41598-023-31738-x)
- [OSF project ps38n](https://osf.io/ps38n/) · [Guitart-Masip, Walsh, Dayan & Olsson (2023), Scientific Reports](https://doi.org/10.1038/s41598-023-45179-z)
