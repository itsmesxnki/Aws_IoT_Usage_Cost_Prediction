# Aws_IoT_Usage_Cost_Prediction

## Project Overview

Welcome to the Time Series Forecasting Project using ARIMA! This repository contains a comprehensive guide and implementation for forecasting future billing costs which is incurred by aws iot core based on historical billing data. The primary focus of this project is to leverage the ARIMA (AutoRegressive Integrated Moving Average) model for accurate and insightful time series predictions.

## Key Features

- **Data Loading and Preprocessing:** The project includes detailed steps for loading and preparing the dataset, specifically handling date conversions and setting the appropriate index for time series analysis.
- **Monthly Aggregation:** The dataset is resampled to a monthly frequency, aggregating the total costs to facilitate a smoother analysis and better forecast accuracy.
- **ARIMA Model Implementation:** A robust ARIMA model is fitted to the prepared dataset. The ARIMA parameters (p, d, q) can be adjusted to optimize model performance.
- **Future Forecasting:** The model is used to predict future billing costs, providing valuable insights into upcoming financial trends.

## Project Structure

- **Data Preparation:**
  - Extracting data (exported the data as a csv file from aws billing and cost management service).
  - Loading data from a CSV file.
  - Converting date columns to datetime format.
  - Setting the date column as the index for time series operations.
  - Resampling data to monthly frequency and aggregating total costs.

- **Model Fitting:**
  - Implementing the ARIMA model with an initial order of (1, 1, 1).
  - Fitting the model to the monthly aggregated data.

- **Forecasting:**
  - Predicting the next month's billing cost.
  - Printing the forecasted cost for easy interpretation.

## Getting Started

### Prerequisites

- Python 3.x
- pandas
- statsmodels

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/itsmesxnki/Aws_IoT_Usage_Cost_Prediction.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Aws_IoT_Usage_Cost_Prediction
   ```
3. Install the required libraries:
   ```bash
   pip install pandas statsmodels
   ```

### Usage

1. Place your data file `Final_Dataset.csv` in the project directory.
2. Run the Python script:
   ```bash
   ARIMA_MODEL.ipynb
   ```
3. View the forecasted cost for the next month in the console output.

## Understanding ARIMA

ARIMA stands for AutoRegressive Integrated Moving Average, a powerful statistical method for time series analysis and forecasting. It combines three key components:

- **AutoRegressive (AR) Component:** Captures the relationship between an observation and a specified number of lagged observations.
- **Integrated (I) Component:** Applies differencing to make the time series stationary, removing trends or seasonality.
- **Moving Average (MA) Component:** Models the relationship between an observation and a residual error from a moving average model applied to lagged observations.

By combining these components, ARIMA provides a versatile and effective approach to time series forecasting.

## Contributions

Contributions are welcome! If you have any ideas or improvements, feel free to open an issue or submit a pull request.

## Acknowledgments

This project utilizes the powerful pandas and statsmodels libraries, which are instrumental in data manipulation and time series analysis. Special thanks to the open-source community for their contributions to these libraries.

---

By following this README, you should be able to set up and run the ARIMA time series forecasting model on your billing data, providing valuable insights and future predictions for your financial analysis. Happy forecasting!
