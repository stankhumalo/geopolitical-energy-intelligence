# Geopolitical Energy Intelligence Platform

## 1. Project overview

**Objective:** Investigate whether geopolitical events and other market developments are associated with changes in Brent crude oil prices.

The long-term goal is to build a data-driven research platform that combines historical oil prices with geopolitical event information to analyse price movements and volatility.

The project is intended for research and decision support, not as a guaranteed price prediction or trading signal.

## 2. Current progress

### Data preparation

- Imported historical Brent crude oil price data from `brent.csv` using Pandas.
- Converted `observation_date` into a datetime data type.
- Identified missing values in the price column and removed rows with missing prices.
- Calculated percentage changes between consecutive available price observations.

### Statistical analysis

Calculated summary statistics for daily returns:

| Metric | Result |
|---|---:|
| Average daily return | +0.0708% |
| Standard deviation of daily returns | 2.7043 percentage points |
| Returns within one standard deviation of the mean | 982 |
| Total valid daily returns | 1,263 |
| Percentage within one standard deviation | 77.75% |
| Largest daily positive return | +18.0195% |
| Largest daily negative return | −15.4334% |

The 77.75% result means that 982 returns fell between the range of approximately −2.63% and +2.78%, measured relative to the historical mean. This is an observed property of the dataset, not a guaranteed future range.

Standard deviation measures historical dispersion. It does not independently predict the direction of the next price movement.

## 3. Initial case study: 17 April 2026

### Observation

The largest negative daily return identified by the current script occurred on 17 April 2026.

| Date | Brent spot price | Daily return |
|---|---:|---:|
| 16 April 2026 | $116.63 | +1.48% |
| 17 April 2026 | $98.63 | −15.43% |
| 20 April 2026 | $103.40 | +4.84% |
| 21 April 2026 | $106.14 | +2.65% |
| 22 April 2026 | $113.44 | +6.88% |

Prices shown are from the current dataset. The return is calculated relative to the preceding available price observation, not necessarily the preceding calendar day.

### Initial hypothesis

News reporting, including CNBC coverage identified during the investigation, attributed the sharp oil price decline to Iran declaring the Strait of Hormuz open to commercial shipping.

A plausible mechanism is that reopening the shipping route reduced concerns about potential oil supply disruptions and lowered the geopolitical risk premium embedded in oil prices.

### Important limitations

- The timing of the announcement must be checked against the market's trading hours and the observed price movement.
- Other developments, including US–Iran negotiations and the Israel–Lebanon ceasefire, may also have influenced market expectations.
- News coverage supports a possible explanation but does not establish how much each event contributed to the decline.
- The dataset measures Brent spot prices, while some news reports discuss Brent futures. These are different price measures and should not be treated as interchangeable.

### Next investigation

1. Verify the announcement's timing using reliable reporting.
2. Review the price movements before and after 17 April.
3. Investigate the largest positive return separately.
4. Build a structured dataset of geopolitical events and dates.
5. Compare returns and volatility around event dates with other periods.

## 4. Current tools

- Python
- Pandas for data cleaning and analysis
- NumPy and Matplotlib available for future analysis and visualisation
- Historical Brent crude oil price CSV data (unsure of accuracy)

## 5. Current status

**Stage 1: Historical data exploration — in progress.**

The project has established a working data cleaning and descriptive-statistics workflow. The next stage is to make the analysis reproducible, investigate extreme movements systematically, and begin testing relationships between event information and market behaviour.
