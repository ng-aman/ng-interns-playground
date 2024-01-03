# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Decision Tree model
model = DecisionTreeClassifier()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Save the trained model and target names using joblib
model_and_names = {
    'model': model,
    'target_names': target_names
}
joblib.dump(model_and_names, 'decision_tree_model_with_names.joblib')

# Now, you can load the model and target names later using:
# loaded_data = joblib.load('decision_tree_model_with_names.joblib')
# loaded_model = loaded_data['model']
# loaded_target_names = loaded_data['target_names']
