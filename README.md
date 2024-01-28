
# Currency Exchange Rate Recommendation System

## Introduction
The Currency Exchange Rate Prediction System is a Python application designed to assist users in analyzing historical currency exchange rates. It predicts future rates and makes recommendations on buying or selling currencies.

## Getting Started

### Prerequisites
- Python 3.10 or higher
- Pip package manager
- Virtual environment (recommended)

### Installation
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Set up a virtual environment (optional but recommended).
4. Run `setup.py` to install necessary libraries listed in `requirements.txt`.

```bash
python setup.py install
```

## Project Structure

- `Currency Exchange Recommendation System.ipynb`: Jupyter notebook with all the analysis and prediction code.
- `setup.py`: Script to set up the project dependencies.
- `requirements.txt`: List of libraries required for the project.

## Modules Overview

### Importing Libraries
The system utilizes a variety of Python libraries:
- `plotly.express` and `plotly.graph_objects` for interactive plotting.
- `pandas` for data manipulation and analysis.
- `numpy` for numerical computations.
- `matplotlib.pyplot` and `seaborn` for static plotting.
- `sklearn` for machine learning tasks, including model selection and feature selection.
- `xgboost` for the XGBoost algorithm implementation.
- `statsmodels` for the implementation of many statistical models.
- `yfinance` for fetching historical market data.
- `warnings` to suppress warnings for cleaner output.

### Data Loading
The yfinance library is used to download historical exchange rate data for the specified currency pair (e.g., PKR to USD). The data is then saved to a CSV file for later use.

### Data Preprocessing
This step includes handling missing values, converting date strings to datetime objects, and filling any remaining missing values with forward-fill method to maintain data continuity.

### Exploratory Data Analysis (EDA)
EDA is performed to understand data distributions and relationships. This includes generating a candlestick chart with volume and a box plot to visualize the distribution of data.

### Feature Engineering
The system creates new features like lag features (to capture temporal dependencies) and technical indicators such as Simple Moving Average (SMA) and Relative Strength Index (RSI), which are widely used in technical analysis.

### Data Normalization and Feature Selection
Skewness of the features is assessed, and outlier handling is performed through Interquartile Range (IQR) capping. Features are then selected based on their correlation with the target variable and Recursive Feature Elimination (RFE) using a Random Forest Regressor.

### Model Training and Evaluation
Several models are trained and evaluated:

### Linear Regression: For linear relationships.
Random Forest Regressor: For non-linear relationships and feature importance ranking.
Gradient Boosting Regressor: For sequential error reduction.
XGBoost Regressor: For a scalable and efficient gradient boosting implementation.
The best model is selected based on Mean Squared Error (MSE) and R-squared (R2) metrics.

### Recommendation Engine
A function is designed to recommend whether to buy or sell based on the predictions of the best model and the current price.

### Forecasting
The system can forecast the exchange rate for a specified number of future days using the best-performing model.

### Visualization
Interactive visualizations are created using Plotly to display predicted and actual values, and trends over time.

## Contributing
Feel free to fork the project, make changes, and submit a pull request.


## Acknowledgments
- The dataset used in this project is courtesy of Yahoo Finance.
- This project is inspired by the challenges faced by currency traders in predicting exchange rates.