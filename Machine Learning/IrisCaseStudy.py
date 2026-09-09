import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score

def IrisCaseStudy():

    border = "-"*50

    ############################################################
    #   Step 1 : Load the dataset
    ############################################################
    
    print(border)
    print("Step 1 : Load the dataset")
    print(border)

    df = pd.read_csv("iris.csv")

    print("Some few data from iris : ")
    print(df.head(10))

    ############################################################
    #   Step 2 : Exploratory data analysis
    ############################################################

    print(border)
    print("Step 2 : Exploratory data analysis")
    print(border)

    print("Shape of the dataset : ", df.shape)

    print("Column names : ", list(df.columns))

    print("Statistical report of dataset : ")
    print(df.describe())  

    ############################################################
    #   Step 3 : Data cleaning
    ############################################################

    print(border)
    print("Step 3 : Data cleaning")
    print(border)

    print("Missing values per column : ")
    print(df.isnull().sum())

    ############################################################
    #   Step 4 : Separate Independent and Dependent Variables
    ############################################################

    print(border)
    print("Step 4 : Separate Independent and Dependent Variables")
    print(border)

    X = df.drop("species",axis=1)       #axis=1 means column
    Y = df["species"]

    print("Independent variables (features) are : ")
    print(X)

    print("Dependent variables (labels) are : ")
    print(Y)

    ############################################################
    #   Step 5 : Split dataset for training and testing
    ############################################################

    print(border)
    print("Step 5 : Split dataset for training and testing")
    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    print("Dataset splitted successfully...")

    ############################################################
    #   Step 6 : Create the model
    ############################################################

    print(border)
    print("Step 6 : Create the model")
    print(border)

    model = DecisionTreeClassifier()

    print("Model created...")

    ############################################################
    #   Step 7 : Train the model
    ############################################################

    print(border)
    print("Step 7 : Train the model")
    print(border)

    model = model.fit(X_train, Y_train)

    print("Model trained...")

    ############################################################
    #   Step 8 : Test the model
    ############################################################

    print(border)
    print("Step 8 : Test the model")
    print(border)

    y_Pred = model.predict(X_test)

    print("Model test...")

    ############################################################
    #   Step 9 : Model evaluation
    ############################################################

    print(border)
    print("Step 9 : Model evaluation")
    print(border)

    confusionMatrix = confusion_matrix(Y_test, y_Pred)
    print("Confusion matrix of the model : ")
    print(confusionMatrix)

    accuracyScore = accuracy_score(Y_test, y_Pred)
    print("Accuracy score of the matrix : ")
    print(accuracyScore)

    precision = precision_score(Y_test, y_Pred, average="weighted")
    print("Precision : ")
    print(precision)

    recall = recall_score(Y_test, y_Pred, average="weighted")
    print("Recall : ")
    print(recall)

    f1Score = f1_score(Y_test, y_Pred, average="weighted")
    print("F1 score : ")
    print(f1Score)

def main():
    IrisCaseStudy()


if __name__ == "__main__":
    main()