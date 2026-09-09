import pandas as pd                         # Import Pandas for creating DataFrame
import joblib                               # Import Joblib for loading the trained model


def LoadModel(Filename):                    # Define function to load the saved model
    model = joblib.load(Filename)           # Load the trained model from the PKL file

    print("Model loaded succesfully")       

    print(model.feature_names_in_)          # Display the features used during model training

    return model                            # Return the loaded model


def PredictPassenger(model):                # Define function to predict passenger survival
    print("Enter the information")          

    Pclass = int(input("Enter Pclass (1/2/3)"))          # Accept passenger class
    Sex = int(input("Enter Sex : (0 - M / 1 : F)"))      # Accept passenger gender
    Age = float(input("Enter Age : "))                    # Accept passenger age
    sibsp = int(input("Enter sibsp : "))                  # Accept number of siblings or spouses
    Parch = int(input("Enter Parch : "))                  # Accept number of parents or children
    Fare = int(input("Enter Fare : "))                    # Accept passenger fare
    Embarked = float(input("Enter embarked : (0/1/2)"))   # Accept embarkation value

    passenger = pd.DataFrame([{                         # Create DataFrame for new passenger
        "Pclass" : Pclass,                              # Store passenger class
        "Sex" : Sex,                                    # Store passenger gender
        "Age" : Age,                                    # Store passenger age
        "sibsp" : sibsp,                                # Store number of siblings or spouses
        "Parch" : Parch,                                # Store number of parents or children
        "Fare" : Fare,                                  # Store passenger fare
        "Embarked_1.0" : 1 if Embarked == 1 else 0,     # Create dummy value for Embarked 1
        "Embarked_2.0" : 1 if Embarked == 2 else 0      # Create dummy value for Embarked 2
    }])

    passenger = passenger[model.feature_names_in_]      # Arrange features in the same order as training

    result = model.predict(passenger)                   # Predict passenger survival

    if result[0] == 1:
        print("Passenger Survived")
    else:
        print("Passenger Did Not Survive")


def main():                                             # Define the main function
    model = LoadModel("MarvellousTitanic.pkl")          # Load the saved Titanic model

    PredictPassenger(model)                             # Predict survival for a new passenger


if __name__ == "__main__":                              
    main()                                              # Call the main function