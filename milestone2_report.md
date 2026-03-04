# ClimateScope - Milestone 2 Report

## 1. Introduction

ClimateScope is an interactive climate analytics dashboard developed using Python and Streamlit.  
The objective of this project is to analyze global weather data and identify patterns, trends, correlations, and extreme events.

---

## 2. Tools and Technologies Used

- Python
- Pandas (Data Processing)
- Plotly (Interactive Visualizations)
- Streamlit (Dashboard Development)
- Parquet (Efficient Data Storage)

---

## 3. Data Processing

The dataset was cleaned and processed using Pandas.  
Key steps performed:

- Removed missing values
- Converted temperature units
- Standardized country and month fields
- Saved processed data in Parquet format

---

## 4. Analysis Performed

### 4.1 Key Performance Indicators (KPIs)

Displayed:
- Average Temperature
- Maximum Temperature
- Average Wind Speed
- Hottest Month
- Coldest Month

Purpose:
To provide quick statistical summary of selected country.

---

### 4.2 Seasonal Trend Analysis

Visualization: Line Chart

Shows monthly temperature variation for selected country.

Insight:
Helps identify seasonal patterns and climate fluctuations.

---

### 4.3 Regional Comparison

Visualization: Bar Chart

Compares temperature across countries for selected month.

Insight:
Helps understand regional temperature differences.

---

### 4.4 Correlation Analysis

Visualization: Heatmap

Analyzed relationship between:

- Temperature (Celsius & Fahrenheit)
- Wind Speed (mph & kph)
- Wind Degree
- Latitude
- Longitude

Correlation values range from -1 to +1.

Insight:
Identifies strong positive and negative relationships between climate variables.

---

### 4.5 Extreme Weather Detection

Visualization: Boxplot

Identified:
- Hottest Month
- Coldest Month
- Temperature distribution
- Outliers

Purpose:
To detect extreme climate behavior and variability.

---

## 5. Key Findings

- Temperature shows seasonal variation across months.
- Strong positive correlation exists between temperature in Celsius and Fahrenheit.
- Wind speed in mph and kph are strongly correlated.
- Some countries show higher temperature variability.
- Extreme months can be identified clearly through KPI metrics.

---

## 6. Conclusion

The ClimateScope dashboard successfully provides:

- Statistical summaries
- Seasonal pattern analysis
- Regional comparisons
- Correlation insights
- Extreme weather detection

The interactive filters allow dynamic exploration of climate data, making the dashboard suitable for analytical and presentation purposes.

---

## 7. Future Improvements

- Add rainfall and humidity analysis
- Add forecasting using machine learning
- Deploy dashboard online
- Add map-based visualization