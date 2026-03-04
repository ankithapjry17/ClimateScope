# Milestone 1: Data Preparation & Initial Analysis

## Dataset
Global Weather Repository (Kaggle)

## Dataset Overview
- Total Records: 123,941
- Total Columns: 41
- Data collected across multiple countries and locations
- Includes temperature, humidity, wind speed, precipitation, pressure, visibility, UV index, and air quality metrics

## Data Schema Highlights
- 23 Float (numerical) columns
- 7 Integer columns
- 11 Categorical/String columns
- Key time-related column: last_updated
- Geographic attributes: country, latitude, longitude

## Data Inspection Findings
- No missing values detected across columns
- Dataset contains structured daily weather observations
- Data types verified using pandas (.info())
- Statistical summary generated using (.describe())

## Data Cleaning & Preprocessing Steps
- Removed duplicate records
- Applied forward-fill as precautionary missing value handling
- Converted `last_updated` column to datetime format
- Created a new `month` feature from the date column
- Aggregated daily data into monthly averages grouped by country

## Data Quality Assessment
- Dataset is complete with no null values
- Data is consistent across numerical and categorical columns
- Suitable for further statistical analysis and visualization

## Output
Cleaned and aggregated dataset saved at:

data/processed/cleaned_weather_data.csv

Milestone 1 successfully completed.  
The dataset is now cleaned, structured, and ready for analysis and visualization in the next phase.
