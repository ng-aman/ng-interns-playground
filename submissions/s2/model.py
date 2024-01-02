import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

def train_and_save_model():
    # Load Iris dataset
    data = pd.read_csv('C:\\Users\\SRIJAN\\OneDrive - S. Jaykishan\\Desktop\\ng-interns-playground\\submissions\\s2\\iris.csv')

    # Input and output columns
    x = data.drop(['Species', 'Id'], axis=1)
    y = data['Species']

    # Split the data
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    # Random Forest Prediction
    model_rf = RandomForestClassifier()
    model_rf.fit(x_train, y_train)

    # Save the model to a pickle file
    with open('iris_model_rf.pkl', 'wb') as model_file:
        pickle.dump(model_rf, model_file)

if __name__ == "__main__":
    train_and_save_model()
























