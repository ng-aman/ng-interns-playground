from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
import joblib

# Define FastAPI app
app = FastAPI()

# Database setup
DATABASE_URL = "mysql+mysqlconnector://root:12345@localhost:3306/iris_db"

Base = declarative_base()

# Model for database table
class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True, index=True)
    sepal_length = Column(Float)
    sepal_width = Column(Float)
    petal_length = Column(Float)
    petal_width = Column(Float)
    species = Column(String(255), index=True)

# SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)  # Create tables if they do not exist
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Load and preprocess Iris dataset
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Train a simple model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "iris_model.joblib")

# Define request model
class BatchPredictionRequest(BaseModel):
    data: list

# Route to perform batch predictions
@app.post("/batch-predictions/")
def batch_predictions(request: BatchPredictionRequest, db: Session = Depends(get_db)):
    predictions = []

    for sample_data in request.data:
        # Make predictions using the trained model
        prediction = model.predict([sample_data])[0]
        species = iris.target_names[prediction]

        # Store prediction in the database
        db_prediction = Prediction(
            sepal_length=sample_data[0],
            sepal_width=sample_data[1],
            petal_length=sample_data[2],
            petal_width=sample_data[3],
            species=species
        )
        db.add(db_prediction)
        db.commit()  # Commit changes inside the loop
        db.refresh(db_prediction)

        # Append prediction to the result
        predictions.append({"input_data": sample_data, "prediction": species})

    return predictions
