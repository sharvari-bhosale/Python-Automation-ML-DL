import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import (
    RandomForestClassifier,
    BaggingClassifier,
    AdaBoostClassifier,
    VotingClassifier
)

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)


#-------------------------------------------------------------------
# Step 1 : Load the dataset
#-------------------------------------------------------------------

df = pd.read_csv("breast_cancer.csv")

print("=" * 60)
print("             BREAST CANCER PREDICTION")
print("=" * 60)

print("\nShape of dataset : ", df.shape)

print("\nFirst 5 records : ")
print(df.head())


#-------------------------------------------------------------------
# Step 2 : Separate features and labels
#-------------------------------------------------------------------

X = df.drop("target", axis=1)
Y = df["target"]

print("\nX shape : ", X.shape)
print("Y shape : ", Y.shape)


#-------------------------------------------------------------------
# Step 3 : Split dataset into training and testing
#-------------------------------------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)


#-------------------------------------------------------------------
# Step 4 : Scale the features
#-------------------------------------------------------------------

scalar = StandardScaler()

X_train = scalar.fit_transform(X_train)
X_test = scalar.transform(X_test)


#-------------------------------------------------------------------
# Step 5 : Create the models
#-------------------------------------------------------------------

# Decision Tree
model_dt = DecisionTreeClassifier(random_state=42)


# Logistic Regression
model_lr = LogisticRegression(max_iter=1000)


# Random Forest
model_rf = RandomForestClassifier(
    n_estimators=10,
    random_state=42
)


# Bagging with Decision Tree
base_model = DecisionTreeClassifier(random_state=42)

model_bagging = BaggingClassifier(
    estimator=base_model,
    n_estimators=10,
    random_state=42
)


# AdaBoost
model_boosting = AdaBoostClassifier(
    n_estimators=50,
    learning_rate=1.0,
    random_state=42
)


# Voting Classifier - Hard Voting
model_log = LogisticRegression(max_iter=1000)
model_det = DecisionTreeClassifier(random_state=42)
model_knn = KNeighborsClassifier(n_neighbors=5)

model_hard_voting = VotingClassifier(
    estimators=[
        ("logistic", model_log),
        ("decision_tree", model_det),
        ("knn", model_knn)
    ],
    voting="hard"
)


# Voting Classifier - Soft Voting
model_log_soft = LogisticRegression(max_iter=1000)
model_det_soft = DecisionTreeClassifier(random_state=42)
model_knn_soft = KNeighborsClassifier(n_neighbors=5)

model_soft_voting = VotingClassifier(
    estimators=[
        ("logistic", model_log_soft),
        ("decision_tree", model_det_soft),
        ("knn", model_knn_soft)
    ],
    voting="soft"
)


#-------------------------------------------------------------------
# Step 6 : Store all models
#-------------------------------------------------------------------

models = {
    "Decision Tree": model_dt,
    "Logistic Regression": model_lr,
    "Random Forest": model_rf,
    "Bagging": model_bagging,
    "Boosting": model_boosting,
    "Hard Voting": model_hard_voting,
    "Soft Voting": model_soft_voting
}


#-------------------------------------------------------------------
# Step 7 : Train and evaluate all models
#-------------------------------------------------------------------

accuracies = {}
predictions = {}

print("\n" + "=" * 60)
print("              MODEL ACCURACY COMPARISON")
print("=" * 60)

for name, model in models.items():

    # Train the model
    model.fit(X_train, Y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(Y_test, y_pred)

    # Store accuracy and predictions
    accuracies[name] = accuracy
    predictions[name] = y_pred

    print(f"{name:<22} : {accuracy * 100:.2f}%")


#-------------------------------------------------------------------
# Step 8 : Find the best model
#-------------------------------------------------------------------

best_model_name = max(accuracies, key=accuracies.get)
best_accuracy = accuracies[best_model_name]

best_prediction = predictions[best_model_name]


print("\n" + "=" * 60)
print("                    BEST MODEL")
print("=" * 60)

print("Best Model    : ", best_model_name)
print("Best Accuracy : ", f"{best_accuracy * 100:.2f}%")


#-------------------------------------------------------------------
# Step 9 : Classification report of best model
#-------------------------------------------------------------------

print("\n" + "=" * 60)
print("             CLASSIFICATION REPORT")
print("=" * 60)

print(classification_report(Y_test, best_prediction))


#-------------------------------------------------------------------
# Step 10 : Confusion matrix of best model
#-------------------------------------------------------------------

print("\n" + "=" * 60)
print("                 CONFUSION MATRIX")
print("=" * 60)

cm = confusion_matrix(Y_test, best_prediction)

print(cm)


#-------------------------------------------------------------------
# Step 11 : Display confusion matrix
#-------------------------------------------------------------------

ConfusionMatrixDisplay(
    confusion_matrix=cm
).plot()

plt.title("Confusion Matrix - " + best_model_name)
plt.tight_layout()
plt.show()


#-------------------------------------------------------------------
# Step 12 : Compare model accuracies graphically
#-------------------------------------------------------------------

plt.figure(figsize=(10, 6))

plt.bar(
    accuracies.keys(),
    [accuracy * 100 for accuracy in accuracies.values()]
)

plt.xlabel("Machine Learning Models")
plt.ylabel("Accuracy (%)")
plt.title("Breast Cancer Prediction - Model Accuracy Comparison")

plt.xticks(rotation=30)
plt.ylim(0, 100)

plt.tight_layout()
plt.show()


#-------------------------------------------------------------------
# Step 13 : Final result
#-------------------------------------------------------------------

print("\n" + "=" * 60)
print("                  FINAL RESULT")
print("=" * 60)

print("Best Model    : ", best_model_name)
print("Best Accuracy : ", f"{best_accuracy * 100:.2f}%")

print("=" * 60)