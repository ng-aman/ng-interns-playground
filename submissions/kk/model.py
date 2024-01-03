from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target
class_names = iris.target_names

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the KNN classifier with the desired number of neighbors (k)
knn_classifier = KNeighborsClassifier(n_neighbors=3)

# Train the model
knn_classifier.fit(X_train, y_train)

# Save the model and class names to a dictionary
saved_data = {"model": knn_classifier, "class_names": class_names}

# Save the dictionary to a file using joblib
model_filename = "knn_model_with_names.joblib"
joblib.dump(saved_data, model_filename)
print(f"Model and class names saved to {model_filename}")
