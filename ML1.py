from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Step 1: Load the dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Step 2: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train the machine learning model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Step 4: Make predictions on the testing set
y_pred = model.predict(X_test)

# Step 5: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


import pyautocad

acad = pyautocad.Autocad()

# Set up drawing parameters
drawing_name = "P&ID_Diagram"
drawing_units = pyautocad.UnitType.Millimeters
drawing_template = "C:\\Path\\to\\DrawingTemplate.dwt"  # Replace with your own template path

# Create a new drawing
drawing = acad.doc.ActiveDocument.Application.Documents.Add(drawing_template)

# Set drawing units
drawing.ActiveLayout.BlockUnit = drawing_units
drawing.ActiveLayout.PaperUnit = drawing_units

# Start drawing P&ID components
drawing.ModelSpace.AddCircle(0, 0, 10)  # Example: Adding a circle as a component

# Save the drawing
drawing.SaveAs("C:\\Path\\to\\Save\\Location\\" + drawing_name + ".dwg")

# Close AutoCAD application
acad.Application.Quit()
