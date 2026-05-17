# Dynamic Pricing Prediction System
## Live Demo

Deployed API:

https://dynamic-pricing-model-api-deployed.onrender.com/docs

You can test ride cost prediction directly using the FastAPI Swagger interface.
## Project Overview

This project predicts the **ride cost** in a dynamic pricing system using machine learning.

The goal was to study the dataset carefully, understand what factors affect ride pricing, test different models, and finally build a system that can predict the ride cost from input features.

The project includes:

- data assessment
- data cleaning
- exploratory data analysis
- statistical testing
- feature engineering attempt
- preprocessing
- model building
- model comparison
- residual analysis
- FastAPI deployment

---

## Problem Statement

Ride pricing can change based on different factors such as:

- number of riders
- number of drivers
- location
- customer loyalty
- booking time
- vehicle type
- ride duration

The objective of this project was:

> **To predict the historical cost of a ride using ride-related features.**

---

## Dataset Description

The dataset contains the following input features:

| Feature | Meaning |
|---|---|
| Number_of_Riders | Number of riders requesting the ride |
| Number_of_Drivers | Number of available drivers |
| Location_Category | Location type such as Urban, Suburban, or Rural |
| Customer_Loyalty_Status | Loyalty level of the customer |
| Number_of_Past_Rides | Number of previous rides taken by the customer |
| Average_Ratings | Average rating of the customer |
| Time_of_Booking | Time period when the ride was booked |
| Vehicle_Type | Type of vehicle used |
| Expected_Ride_Duration | Estimated duration of the ride |

### Target Variable

| Feature | Meaning |
|---|---|
| Historical_Cost_of_Ride | Ride cost to be predicted |

---

## Data Assessment and Cleaning

Before modeling, the dataset was carefully checked for quality issues.

### What was checked
- missing values
- duplicate rows
- incorrect data types
- categorical consistency
- outliers
- distributions

### Findings
- No missing values were found.
- No duplicate rows were found.
- Categorical values were balanced and consistent.
- `Number_of_Drivers` showed outliers and skewness, but they were kept because they represented realistic business conditions.

This step was important because cleaning should not remove valid real-world values.

---

## Exploratory Data Analysis

EDA was performed to understand the data better.

### Main observations

#### 1. Expected Ride Duration
`Expected_Ride_Duration` showed a very strong positive relationship with ride cost.

Correlation with target was around:

```text
0.928
This means ride duration is the strongest numerical factor affecting pricing.

2. Vehicle Type

Premium rides generally had higher cost than Economy rides.

3. Other Numerical Features

Variables such as:

Number_of_Riders
Number_of_Drivers
Number_of_Past_Rides
Average_Ratings

showed weak linear relationships with ride cost.

This suggested that the pricing pattern in the dataset is mostly linear and not highly complex.

Statistical Analysis

Statistical tests were used to verify the observations from EDA.

T-Test

A T-test was performed to check whether Vehicle_Type affects ride cost.

Result

The p-value was very small and below 0.05.

Conclusion

Vehicle_Type has a statistically significant effect on ride cost.

ANOVA

ANOVA was used for categorical variables with more than two categories, such as:

Time_of_Booking
Location_Category
Customer_Loyalty_Status
Result

These variables did not show statistically significant influence on ride cost in this dataset.

Conclusion

They were not strong pricing factors here.

Feature Engineering

A new feature called Demand_Supply_Ratio was tested.

It was created using:

Number_of_Riders / Number_of_Drivers

The idea was to capture demand-supply imbalance.

However, this feature did not improve the model, so it was not used in the final workflow.

This is an important part of the project because it shows that not every engineered feature is useful.

Data Preprocessing

Machine learning models cannot directly use text values like:

Urban
Premium
Morning
Gold

So preprocessing was needed.

Method Used

The following sklearn tools were used:

ColumnTransformer
OneHotEncoder
Why sklearn preprocessing was used

It was preferred over manual encoding because:

it keeps train and test preprocessing consistent
it is more suitable for deployment
it avoids column mismatch problems
it is a more professional workflow
Unknown Category Handling

OneHotEncoder was used with:

handle_unknown='ignore'

This helps the model work safely even if a new category appears later during deployment.

Models Tested

Two regression models were tested:

Linear Regression
Random Forest Regressor
Evaluation Metrics

The following metrics were used to compare models:

MAE

Mean Absolute Error

This shows the average error in prediction.

Lower MAE means better performance.

RMSE

Root Mean Squared Error

This gives more penalty to larger errors.

Lower RMSE means better performance.

R² Score

This shows how much of the variation in ride cost is explained by the model.

Higher R² means better performance.

Model Results
Linear Regression
MAE: 52.56
RMSE: 67.44
R² Score: 0.875
Random Forest Regressor
MAE: 55.04
RMSE: 73.35
R² Score: 0.852
Why Linear Regression Was Selected

Linear Regression was selected as the final model because it performed better than Random Forest.

Reasons
It had the highest R² score
It had lower MAE and RMSE
The dataset showed a strong linear relationship, especially with ride duration
It was easier to interpret
It matched the behavior of the data well

This shows that a simpler model can sometimes work better than a more complex one when the data is mostly linear.

Residual Analysis

Residual analysis was done to check model errors.

Observations
Residuals were centered around zero
The model made balanced predictions overall
A mild increase in error was seen for higher ride costs
Conclusion

The model fit was strong overall, with only minor error variation at higher prices.