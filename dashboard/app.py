# dashboard/app.py

import sys
import os
import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="ClimateScope Dashboard",
    layout="wide"
)

# -------------------------------
# Custom Light Theme Styling
# -------------------------------
st.markdown("""
<style>

/* Main Background */
.stApp {
    background-color: #F8F9FA;
}

/* Sidebar - Light Yellow */
section[data-testid="stSidebar"] {
    background-color: #FFF9C4;
    border-right: 2px solid #FDD835;
}

/* Sidebar Heading */
section[data-testid="stSidebar"] h2 {
    color: #B8860B;
    font-size: 24px;
    font-weight: bold;
}

/* Main Title */
.main-title {
    font-size: 45px;
    font-weight: bold;
    text-align: center;
    color: #1F4E79;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #555;
}

/* Section Headings (Key Metrics, Seasonal, etc.) */
h3 {
    font-size: 30px;
    font-weight: 900;
    color: #0D47A1;
}

/* KPI Cards */
div[data-testid="metric-container"] {
    background-color: #FFFFFF;
    border-radius: 12px;
    padding: 22px;
    border: 1px solid #E0E0E0;
}

/* KPI Label */
div[data-testid="metric-container"] > div:nth-child(1) {
    font-size: 20px;
    font-weight: 700;
}

/* KPI Value (Avg Temp, Hottest, Coldest, etc.) */
div[data-testid="metric-container"] > div:nth-child(2) {
    font-size: 46px;      /* Increased properly */
    font-weight: 900;
    color: #000000;
}

/* Info Boxes */
div.stAlert {
    background-color: #FFFFFF;
    border-radius: 10px;
    border: 1px solid #E0E0E0;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# Header
# -------------------------------
st.markdown('<div class="main-title">🌍 ClimateScope Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Advanced Global Climate Analytics</div>', unsafe_allow_html=True)

st.divider()

# -------------------------------
# Add Parent Path
# -------------------------------
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.analysis import load_data

# -------------------------------
# Load Data
# -------------------------------
df = load_data("data/processed/final.parquet")

# -------------------------------
# Sidebar Filters
# -------------------------------
st.sidebar.header("🔎 Filters")

countries = sorted(df['country'].unique())
selected_country = st.sidebar.selectbox("Select Country", countries)

months = sorted(df['month'].unique())
selected_month = st.sidebar.selectbox("Select Month", months)

# -------------------------------
# Filter Data
# -------------------------------
country_df = df[df['country'] == selected_country]
region_df = df[df['month'] == selected_month]

# -------------------------------
# KPI Section
# -------------------------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "🌡 Avg Temperature (°C)",
    f"{round(country_df['temperature_celsius'].mean(), 2)}"
)

col2.metric(
    "🔥 Max Temperature (°C)",
    f"{round(country_df['temperature_celsius'].max(), 2)}"
)

col3.metric(
    "💨 Avg Wind Speed (kph)",
    f"{round(country_df['wind_kph'].mean(), 2)}"
)

st.divider()

# -------------------------------
# Seasonal Trend
# -------------------------------
st.subheader("📈 Seasonal Temperature Trend")

trend_df = country_df.sort_values("month")

fig_trend = px.line(
    trend_df,
    x="month",
    y="temperature_celsius",
    markers=True,
    template="plotly_white",
    title=f"Monthly Temperature Trend - {selected_country}"
)

st.plotly_chart(fig_trend, use_container_width=True)

st.info("Shows how temperature changes across months for selected country.")

st.divider()

# -------------------------------
# Regional Comparison
# -------------------------------
st.subheader("🌎 Regional Temperature Comparison")

fig_region = px.bar(
    region_df,
    x="country",
    y="temperature_celsius",
    template="plotly_white",
    title=f"Temperature Comparison - Month {selected_month}"
)

fig_region.update_layout(xaxis_tickangle=-45)

st.plotly_chart(fig_region, use_container_width=True)

st.info("Compares temperature across countries for selected month.")

st.divider()

# -------------------------------
# Correlation Analysis
# -------------------------------
st.subheader("📊 Correlation Insights")

numeric_cols = [
    "temperature_celsius",
    "temperature_fahrenheit",
    "wind_mph",
    "wind_kph",
    "wind_degree",
    "latitude",
    "longitude"
]

corr_df = country_df[numeric_cols].corr()

fig_corr = px.imshow(
    corr_df,
    text_auto=True,
    aspect="auto",
    template="plotly_white",
    title=f"Correlation Heatmap - {selected_country}",
    color_continuous_scale="RdBu_r"
)

st.plotly_chart(fig_corr, use_container_width=True)

st.info("Correlation ranges from -1 to +1. Red = positive relationship, Blue = negative.")

st.divider()

# -------------------------------
# Extreme Weather Analysis
# -------------------------------
st.subheader("🔥 Extreme Weather Analysis")

hottest = country_df.loc[country_df['temperature_celsius'].idxmax()]
coldest = country_df.loc[country_df['temperature_celsius'].idxmin()]

col1, col2 = st.columns(2)

col1.metric(
    "🔥 Hottest Month",
    f"{round(hottest['temperature_celsius'], 2)} °C",
    f"Month: {hottest['month']}"
)

col2.metric(
    "❄ Coldest Month",
    f"{round(coldest['temperature_celsius'], 2)} °C",
    f"Month: {coldest['month']}"
)

fig_box = px.box(
    country_df,
    y="temperature_celsius",
    template="plotly_white",
    title=f"Temperature Distribution - {selected_country}"
)

st.plotly_chart(fig_box, use_container_width=True)

st.info("Boxplot shows temperature spread and potential outliers.")