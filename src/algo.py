import pandas as pd
import numpy as nump
import matplotlib.pyplot as plt


br = pd.read_csv('data/brent.csv')
br["observation_date"] = pd.to_datetime(br["observation_date"])
br = br.dropna(
    subset=["DCOILBRENTEU"]
).reset_index(drop=True)
br["Daily_Return"] = br["DCOILBRENTEU"].pct_change() * 100

#gets average % of daily return
average = br["Daily_Return"].mean()

#gets standard deviation
std = br["Daily_Return"].std()

#defines lowest + highest range of std
lower = average - std
upper = average + std

#tracks sum of which returns fall between the highest and lowest std
within_range = br["Daily_Return"].between(lower, upper).sum()
#tracks count of return
total = br["Daily_Return"].count()

#shows count of return with range
print("Within one standard deviation:", within_range)
#shows total count
print("Total returns:", total)
#shows percentage of total return within std
print("Percentage:", round(within_range / total * 100, 2), "%")

#print(br[br["DCOILBRENTEU"].isna()].head(10))

largest_rise = br.loc[br["Daily_Return"].idxmax()]
largest_fall = br.loc[br["Daily_Return"].idxmin()]

print("Largest daily rise:")

print(largest_rise[["observation_date", "DCOILBRENTEU", "Daily_Return"]])

print("\nLargest daily fall:")
print(largest_fall[["observation_date", "DCOILBRENTEU", "Daily_Return"]])

event_date = pd.Timestamp("2026-04-17")

start_date = event_date - pd.Timedelta(days=5)
end_date = event_date + pd.Timedelta(days=5)

window = br[
    br["observation_date"].between(start_date, end_date)
]

window_display = window[
    ["observation_date", "DCOILBRENTEU", "Daily_Return"]
].copy()

window_display["DCOILBRENTEU"] = (
    window_display["DCOILBRENTEU"].round(2)
)

window_display["Daily_Return"] = (
    window_display["Daily_Return"].round(2)
)

print(window_display.to_string(index=False))