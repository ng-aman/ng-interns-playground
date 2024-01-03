from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import numpy as np
import pickle
from sklearn import datasets  # Import the Iris dataset

# Define the FastAPI app
app = FastAPI()

# Define the database connection URL
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:deepu@localhost/iris_database"

# Create a database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Define SQLAlchemy database models
Base = declarative_base()

class SomeData(Base):
    __tablename__ = "some_data"

    id = Column(Integer, primary_key=True, index=True)
    sepal_length = Column(Float)
    sepal_width = Column(Float)
    petal_length = Column(Float)
    petal_width = Column(Float)
    predicted_species = Column(String)

# Load the saved model
with open('svm_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Create a sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Load the Iris dataset
iris = datasets.load_iris()

# Define request body schema
class InputData(BaseModel):
    inputs: list[list[float]]

# Prediction and database storing endpoint
@app.post("/predict")
def predict_species(data: InputData):
    try:
        input_array = np.array(data.inputs)

        if input_array.shape[1] != 4:
            raise HTTPException(status_code=422, detail="Each input should contain 4 values: sepal_length, sepal_width, petal_length, petal_width")

        predictions = loaded_model.predict(input_array)
        species = [iris.target_names[prediction] for prediction in predictions]

        # Store the predicted data in the database
        db = SessionLocal()
        for i, prediction in enumerate(predictions):
            db_data = SomeData(
                sepal_length=data.inputs[i][0],
                sepal_width=data.inputs[i][1],
                petal_length=data.inputs[i][2],
                petal_width=data.inputs[i][3],
                predicted_species=iris.target_names[prediction]
            )
            db.add(db_data)
        db.commit()
        db.close()

        return {"predictions": species}

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

# Endpoint to create the table and test the database connection
@app.get("/setup")
async def setup():
    try:
        Base.metadata.create_all(bind=engine)
        with engine.connect() as connection:
            return {"message": "Table created, connection successful"}
    except Exception as e:
        return {"message": f"Error setting up the table or connecting to the database: {str(e)}"}
