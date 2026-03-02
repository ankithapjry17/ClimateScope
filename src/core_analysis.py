import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("data/processed/cleaned_weather_data.csv")

print("===== DATASET SHAPE =====")
print(df.shape)

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())

print("\n===== UNIQUE COUNTRIES COUNT =====")
print(df["country"].nunique())

print("\n===== TEMPERATURE DISTRIBUTION ANALYSIS =====")

print("Minimum Temperature:", df["temperature_celsius"].min())
print("Maximum Temperature:", df["temperature_celsius"].max())
print("Average Temperature:", df["temperature_celsius"].mean())
print("Standard Deviation:", df["temperature_celsius"].std())

# IQR-based extreme detection
Q1 = df["temperature_celsius"].quantile(0.25)
Q3 = df["temperature_celsius"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

extreme_temp = df[
    (df["temperature_celsius"] < lower_bound) |
    (df["temperature_celsius"] > upper_bound)
]

print("\nLower Bound:", lower_bound)
print("Upper Bound:", upper_bound)
print("Number of Extreme Temperature Records:", extreme_temp.shape[0])

print("\n===== TOP 5 HOTTEST MONTHLY RECORDS =====")
print(df.sort_values("temperature_celsius", ascending=False)[
    ["country", "month", "temperature_celsius"]
].head())

print("\n===== TOP 5 COLDEST MONTHLY RECORDS =====")
print(df.sort_values("temperature_celsius", ascending=True)[
    ["country", "month", "temperature_celsius"]
].head())

print("\n===== TOP CORRELATIONS WITH TEMPERATURE =====")

correlation_matrix = df.corr(numeric_only=True)

temp_correlations = correlation_matrix["temperature_celsius"].sort_values(ascending=False)

print(temp_correlations.head(6))
print(temp_correlations.tail(6))

print("\n===== MONTHLY TEMPERATURE TREND =====")

monthly_avg_temp = df.groupby("month")["temperature_celsius"].mean()

print(monthly_avg_temp)

import matplotlib.pyplot as plt

print("\n===== GENERATING MONTHLY TEMPERATURE TREND GRAPH =====")

monthly_avg_temp = df.groupby("month")["temperature_celsius"].mean()

plt.figure()
plt.plot(monthly_avg_temp.index, monthly_avg_temp.values)
plt.xlabel("Month")
plt.ylabel("Average Temperature (°C)")
plt.title("Global Monthly Average Temperature Trend")
plt.show()

print("\n===== GENERATING CORRELATION HEATMAP =====")

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure()
correlation_matrix = df.corr(numeric_only=True)

sns.heatmap(correlation_matrix)
plt.title("Climate Data Correlation Heatmap")
plt.show()