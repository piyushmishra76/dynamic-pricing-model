from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os

# Create FastAPI app
app = FastAPI(
    title="Dynamic Pricing Prediction API",
    description="""
    Predict ride cost using
    machine learning.
    """,
    version="1.0.0"
)


# Load model and preprocessor
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

model_path = os.path.join(
    BASE_DIR,
    "models",
    "dynamic_pricing_model.pkl"
)

preprocessor_path = os.path.join(
    BASE_DIR,
    "models",
    "preprocessor.pkl"
)

model = joblib.load(model_path)

preprocessor = joblib.load(
    preprocessor_path
)


# Input schema
class RideInput(BaseModel):
    Number_of_Riders: int
    Number_of_Drivers: int
    Location_Category: str
    Customer_Loyalty_Status: str
    Number_of_Past_Rides: int
    Average_Ratings: float
    Time_of_Booking: str
    Vehicle_Type: str
    Expected_Ride_Duration: float


# Home route
@app.get(
    "/",
    tags=["Home"]
)
def home():
    return {
        "message":
        "Dynamic Pricing API is running"
    }


# Prediction route
@app.post(
    "/predict",
    tags=["Prediction"]
)
def predict(data: RideInput):

    input_data = pd.DataFrame([{
        "Number_of_Riders":
        data.Number_of_Riders,

        "Number_of_Drivers":
        data.Number_of_Drivers,

        "Location_Category":
        data.Location_Category,

        "Customer_Loyalty_Status":
        data.Customer_Loyalty_Status,

        "Number_of_Past_Rides":
        data.Number_of_Past_Rides,

        "Average_Ratings":
        data.Average_Ratings,

        "Time_of_Booking":
        data.Time_of_Booking,

        "Vehicle_Type":
        data.Vehicle_Type,

        "Expected_Ride_Duration":
        data.Expected_Ride_Duration
    }])

    processed_data = preprocessor.transform(
        input_data
    )

    prediction = model.predict(
        processed_data
    )

    return {
        "Predicted_Ride_Cost":
        round(float(prediction[0]), 2)
    }