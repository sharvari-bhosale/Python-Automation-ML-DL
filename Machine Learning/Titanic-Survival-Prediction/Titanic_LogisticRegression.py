import pandas as pd                         # Import Pandas for data handling
import numpy as np                          # Import NumPy for numerical operations
import joblib                               # Import Joblib for saving and loading ML models

from sklearn.model_selection import train_test_split          # Import function to split dataset
from sklearn.linear_model import LogisticRegression           # Import Logistic Regression algorithm
from sklearn.metrics import accuracy_score, confusion_matrix  # Import evaluation metrics


# Step 1 : Load Data

def LoadData(filename):                     # Define function to load CSV data
    df = pd.read_csv(filename)              # Read CSV file and store data in DataFrame

    print("Dataset loaded succesfully")     
    print(df.head())                        # Display first five records of the dataset

    return df                               # Return the DataFrame


# Step 2 : Data Preprocessing

def PreprocessData(df):                     # Define function for data preprocessing
    df = df.drop(                           # Remove unwanted columns from DataFrame
    columns=[
        "Passengerid",                      # Remove Passengerid column
        "zero",                             # Remove zero column
        "name"                              # Remove name column
    ],
    errors="ignore"                         # Ignore columns if they do not exist
)

    # Handle missing values
    df["Age"] = df["Age"].fillna(df["Age"].median())             # Replace missing Age with median
    df["Fare"] = df["Fare"].fillna(df["Fare"].median())         # Replace missing Fare with median

    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])  # Replace missing Embarked with mode

    # Convert categorical to numeric data
    df = pd.get_dummies(                    # Convert categorical data into dummy variables
        df,
        columns=["Embarked"],               # Convert Embarked column
        drop_first= True,                   # Remove first dummy column
        dtype=int                            # Store dummy values as integers
    )

    print(df.head())                        # Display first five rows after preprocessing

    print("Data prepsocessing completed")   

    return df                               # Return the preprocessed DataFrame


# Step 3 : Split Data

def SplitData(df):                          # Define function to split the dataset
    X = df.drop("Survived", axis = 1)       # Store feature columns in X
    Y = df["Survived"]                      # Store target column in Y

    X_train, X_test, Y_train, Y_test = train_test_split(        # Split data into training and testing sets
        X,                                  # Feature data
        Y,                                  # Target data
        test_size=0.2,                      # Use 20 percent data for testing
        random_state=42                     # Set random state for reproducible results
    )

    print("Dataset Splitting completed succesfully")            # Display splitting completion message

    return X_train, X_test, Y_train, Y_test                     # Return four datasets


# Step 4 : Train the model

def TrainModel(X_train, Y_train):           # Define function to train the model
    model = LogisticRegression(max_iter=1000) # Create Logistic Regression model

    model = model.fit(X_train, Y_train)     # Train the model using training data

    print("Model trained succesfully")      

    return model                            # Return the trained model


# Step 5 : Evaluate model

def EvaluateModel(model, X_test, Y_test):   # Define function to evaluate the model
    Y_pred = model.predict(X_test)          # Predict values using testing data

    accuracy = accuracy_score(Y_test,Y_pred) # Calculate model accuracy

    print("Accuracy is : ",accuracy)        # Display accuracy

    print("Confusion matrix : ")         # Display confusion matrix
    print(confusion_matrix(Y_test,Y_pred)) 


# Step 6 : Preserve Model

def PreserveModel(model,filename):          # Define function to save the model
    joblib.dump(model,filename)              # Save trained model into PKL file

    print("Model preserved with name : ",filename)  # Display saved model filename


def main():                                 # Define the main function

    # Step 1
    df = LoadData("MarvellousTitanicDataset.csv")               # Load Titanic dataset

    # Step 2
    df = PreprocessData(df)                                     # Perform data preprocessing

    # Step 3
    X_train, X_test, Y_train, Y_test = SplitData(df)             # Split dataset

    # Step 4
    model = TrainModel(X_train, Y_train)                        # Train Logistic Regression model

    # Step 5
    EvaluateModel(model,X_test,Y_test)                          # Evaluate trained model

    # Step 6
    PreserveModel(model,"MarvellousTitanic.pkl")                # Save trained model


if __name__ == "__main__":                   
    main()                                   # Call the main function