import pandas as pd                         # Import Pandas for data handling
import matplotlib.pyplot as plt             # Import Matplotlib for graphs

from sklearn.model_selection import train_test_split    # Split data into training and testing sets
from sklearn.preprocessing import StandardScaler        # Standardize feature values

from sklearn.linear_model import LogisticRegression     # Import Logistic Regression
from sklearn.tree import DecisionTreeClassifier          # Import Decision Tree
from sklearn.neighbors import KNeighborsClassifier       # Import KNN
from sklearn.ensemble import RandomForestClassifier      # Import Random Forest
from sklearn.ensemble import BaggingClassifier            # Import Bagging
from sklearn.ensemble import AdaBoostClassifier           # Import AdaBoost
from sklearn.ensemble import VotingClassifier             # Import Voting Classifier

from sklearn.metrics import accuracy_score                # Calculate accuracy
from sklearn.metrics import classification_report         # Generate classification report
from sklearn.metrics import confusion_matrix              # Generate confusion matrix
from sklearn.metrics import ConfusionMatrixDisplay        # Display confusion matrix graph


def BreastCancerPrediction():                              # Function for Breast Cancer Prediction

    df = pd.read_csv("breast_cancer.csv")                  # Load the breast cancer dataset

    print("Dataset Shape :", df.shape)                     # Display dataset shape
    print("\nFirst Five Records :")                        
    print(df.head())                                       # Display first five records

    X = df.drop("target", axis=1)                          # Store input features
    Y = df["target"]                                       # Store target column

    X_train, X_test, Y_train, Y_test = train_test_split(   # Split dataset into training and testing data
        X, Y,
        test_size=0.2,                                     # Use 20% data for testing
        random_state=42                                    # Set random state for reproducible results
    )

    scalar = StandardScaler()                              # Create StandardScaler object

    X_train = scalar.fit_transform(X_train)                # Fit scaler on training data and transform it
    X_test = scalar.transform(X_test)                      # Transform testing data using training scaler

    LogisticModel = LogisticRegression(                   # Create Logistic Regression model
        max_iter=1000,                                     # Set maximum number of iterations
        random_state=42                                    # Set random state
    )

    DecisionTreeModel = DecisionTreeClassifier(            # Create Decision Tree model
        random_state=42                                    # Set random state
    )

    KNNModel = KNeighborsClassifier(                       # Create KNN model
        n_neighbors=5                                      # Select 5 nearest neighbours
    )

    RandomForestModel = RandomForestClassifier(            # Create Random Forest model
        n_estimators=10,                                   # Create 10 decision trees
        random_state=42                                    # Set random state
    )

    BaggingModel = BaggingClassifier(                      # Create Bagging model
        estimator=DecisionTreeClassifier(random_state=42), # Use Decision Tree as base estimator
        n_estimators=10,                                   # Create 10 estimators
        random_state=42                                    # Set random state
    )

    BoostingModel = AdaBoostClassifier(                    # Create AdaBoost model
        n_estimators=50,                                   # Set number of boosting estimators
        learning_rate=1.0,                                 # Set learning rate
        random_state=42                                    # Set random state
    )

    HardVotingModel = VotingClassifier(                    # Create Hard Voting model
        estimators=[                                       # Define models used for voting
            ("Logistic Regression", LogisticRegression(max_iter=1000)),  # Add Logistic Regression
            ("Decision Tree", DecisionTreeClassifier(random_state=42)),   # Add Decision Tree
            ("KNN", KNeighborsClassifier(n_neighbors=5))                  # Add KNN
        ],
        voting="hard"                                      # Use majority voting
    )

    SoftVotingModel = VotingClassifier(                    # Create Soft Voting model
        estimators=[                                       # Define models used for voting
            ("Logistic Regression", LogisticRegression(max_iter=1000)),  # Add Logistic Regression
            ("Decision Tree", DecisionTreeClassifier(random_state=42)),   # Add Decision Tree
            ("KNN", KNeighborsClassifier(n_neighbors=5))                  # Add KNN
        ],
        voting="soft"                                      # Use probability-based voting
    )

    models = {                                             # Store all models in a dictionary
        "Logistic Regression": LogisticModel,              # Store Logistic Regression
        "Decision Tree": DecisionTreeModel,                # Store Decision Tree
        "KNN": KNNModel,                                   # Store KNN
        "Random Forest": RandomForestModel,                # Store Random Forest
        "Bagging": BaggingModel,                           # Store Bagging
        "Boosting (AdaBoost)": BoostingModel,              # Store AdaBoost
        "Voting - Hard": HardVotingModel,                  # Store Hard Voting
        "Voting - Soft": SoftVotingModel                   # Store Soft Voting
    }

    accuracies = {}                                        # Create dictionary to store model accuracies
    predictions = {}                                       # Create dictionary to store predictions

    for name, model in models.items():                      # Loop through every model

        model.fit(X_train, Y_train)                        # Train the model

        Y_pred = model.predict(X_test)                     # Predict testing data

        accuracy = accuracy_score(Y_test, Y_pred)          # Calculate model accuracy

        accuracies[name] = accuracy                        # Store model accuracy
        predictions[name] = Y_pred                          # Store model predictions

        print("\n", name)                                  # Display model name
        print("Accuracy :", accuracy * 100, "%")            # Display model accuracy

    BestModelName = max(accuracies, key=accuracies.get)    # Find the model with highest accuracy
    BestAccuracy = accuracies[BestModelName]               # Get the highest accuracy

    print("\n==========================================")         # Display separator
    print("Best Model :", BestModelName)                   # Display best model
    print("Best Accuracy :", BestAccuracy * 100, "%")      # Display best accuracy
    print("==========================================")         # Display separator

    BestPrediction = predictions[BestModelName]            # Get predictions of best model

    print("\nClassification Report -", BestModelName)       # Display classification report heading
    print(classification_report(Y_test, BestPrediction))   # Display classification report

    BestCM = confusion_matrix(Y_test, BestPrediction)      # Calculate best model confusion matrix

    print("\nConfusion Matrix -", BestModelName)            # Display confusion matrix heading
    print(BestCM)                                          # Display confusion matrix values

    ConfusionMatrixDisplay(                                # Create confusion matrix display
        confusion_matrix=BestCM
    ).plot()                                               # Plot best model confusion matrix

    plt.title("Confusion Matrix - " + BestModelName)       # Add title to confusion matrix graph
    plt.show()                                             # Display confusion matrix graph

    LRPrediction = predictions["Logistic Regression"]      # Get Logistic Regression predictions

    LRcm = confusion_matrix(Y_test, LRPrediction)          # Calculate Logistic Regression confusion matrix

    print("\nLogistic Regression Confusion Matrix :")      # Display Logistic Regression heading
    print(LRcm)                                            # Display Logistic Regression confusion matrix

    ConfusionMatrixDisplay(                                # Create Logistic Regression confusion matrix display
        confusion_matrix=LRcm
    ).plot()                                               # Plot Logistic Regression confusion matrix

    plt.title("Confusion Matrix - Logistic Regression")    # Add title to Logistic Regression graph
    plt.show()                                             # Display Logistic Regression confusion matrix graph

    ModelNames = list(accuracies.keys())                   # Get model names
    ModelAccuracies = list(accuracies.values())            # Get model accuracy values

    plt.figure(figsize=(10, 6))                            # Create figure with specified size

    plt.bar(ModelNames, ModelAccuracies)                   # Create bar graph of model accuracies

    plt.title("Model Accuracy Comparison")                 # Add graph title
    plt.xlabel("Machine Learning Models")                  # Add X-axis label
    plt.ylabel("Accuracy")                                 # Add Y-axis label

    plt.xticks(rotation=45)                                # Rotate model names for better visibility

    plt.tight_layout()                                     # Adjust graph layout

    plt.show()                                             # Display accuracy comparison graph

def main():                                               # Main function of the program
    BreastCancerPrediction()                              # Call the Breast Cancer Prediction function


if __name__ == "__main__":                                
    main()                                                # Call the main function