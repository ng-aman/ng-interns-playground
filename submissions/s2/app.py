from fastapi import FastAPI, HTTPException
from typing import List, Dict
import pickle
import sqlite3

app = FastAPI()

# Load the trained model from the pickle file
with open('iris_model_rf.pkl', 'rb') as model_file:
    loaded_model_rf = pickle.load(model_file)

# Train the model 
@app.post("/train")
def train_model():
    train_and_save_model()
    return {"message": "Model trained successfully"}

# Endpoint for making batch predictions
@app.post("/predict")
def predict_rf_batch(request_data: Dict[str, List[Dict[str, float]]]):
    try:
        input_data = request_data.get("data", [])

        # Convert input data to a 2D array
        input_values = [
            [
                sample.get("sepal_length", 0.0),
                sample.get("sepal_width", 0.0),
                sample.get("petal_length", 0.0),
                sample.get("petal_width", 0.0),
            ]
            for sample in input_data
        ]

        # Make predictions using the loaded model
        predictions = loaded_model_rf.predict(input_values)

        # Prepare the output in the specified JSON format
        output_data = [{"input": sample, "output": prediction} for sample, prediction in zip(input_data, predictions)]

        # Insert values into the SQLite database
        with sqlite3.connect('local_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS predictions (input TEXT, output TEXT)')
            cursor.executemany('INSERT INTO predictions VALUES (?, ?)', [(str(sample), str(prediction)) for sample, prediction in zip(input_data, predictions)])
            conn.commit()

        return {"data": output_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
