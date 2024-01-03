from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import joblib
import numpy as np
from sqlalchemy import create_engine, Column, Integer, Float, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the FastAPI app
app = FastAPI()

# Load the saved model and class names
model_filename = "knn_model_with_names.joblib"
saved_data = joblib.load(model_filename)
knn_model = saved_data["model"]
class_names = saved_data["class_names"]

# SQLAlchemy setup
DATABASE_URL = "mysql+mysqlconnector://root:root@localhost:3306/api"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define the database model for input data and predictions
class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    sepal_length = Column(Float)
    sepal_width = Column(Float)
    petal_length = Column(Float)
    petal_width = Column(Float)
    predicted_class = Column(Integer)
    species = Column(VARCHAR(15))

# Create the table in the database
Base.metadata.create_all(bind=engine)

# Create a Pydantic model for input validation
class InputData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Create a Pydantic model for the entire request
class InputDataList(BaseModel):
    inputs: List[InputData]

# Define the endpoint for making predictions with multiple inputs
@app.post("/predict-multiple")
def predict_multiple(input_data: InputDataList):
    predictions = []

    # Create a database session
    db = SessionLocal()

    # ...

    try:
        for single_input in input_data.inputs:
            features = np.array([
                single_input.sepal_length,
                single_input.sepal_width,
                single_input.petal_length,
                single_input.petal_width
            ]).reshape(1, -1)

            prediction = knn_model.predict(features)[0]
            species = class_names[prediction]

            # Save the input data and prediction to the database
            db_prediction = Prediction(
                sepal_length=single_input.sepal_length,
                sepal_width=single_input.sepal_width,
                petal_length=single_input.petal_length,
                petal_width=single_input.petal_width,
                predicted_class=int(prediction),
                species=species
            )
            db.add(db_prediction)
            db.commit()  # Ensure that you commit changes to the database

            predictions.append({"prediction": int(prediction), "species": species})
    finally:
        db.close()  # Ensure that you close the database session
