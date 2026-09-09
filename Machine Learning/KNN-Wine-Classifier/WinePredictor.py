import pandas as pd                         # Used to read and manipulate the dataset
import matplotlib.pyplot as plt             # Used to create graphs

from sklearn.neighbors import KNeighborsClassifier       # Used to create KNN classifier
from sklearn.model_selection import train_test_split     # Used to split data into training and testing
from sklearn.metrics import accuracy_score, confusion_matrix  # Used to calculate performance
from sklearn.preprocessing import StandardScaler         # Used for feature scaling


# This function loads the dataset, trains the KNN model, finds the best value of K and evaluates the model

def MarvellousClassifier(DataPath):

    border = "-"*40                      

    # Step 1 : Load the dataset from CSV file
    print(border)
    print("Step 1 : Load the dataset from CSV file")
    print(border)

    df = pd.read_csv(DataPath)            # Reads the CSV file and stores it in a DataFrame

    print(border)
    print("Some entries from dataset : ")
    print(df.head())                      # Displays the first five records from the dataset
    print(border)


    # Step 2 : Clean the dataset
    print(border)
    print("Step 2 : Clean the dataset")
    print(border)

    df.dropna(inplace=True)               # Removes rows containing missing values

    print("Shape of dataset : ",df.shape) # Displays number of rows and columns
    
    print("Total records : ",df.shape[0]) # Displays total number of records
    print("Total columns : ",df.shape[1]) # Displays total number of columns

    print(border)


    # Step 3 : Separate independent and dependent variables
    print(border)
    print("Step 3 : Separate independent and dependent variables")
    print(border)

    X = df.drop(columns=['Class'])        # Stores all input features except Class
    Y = df['Class']                       # Stores Class as the target/output variable

    print("Shape of X : ",X.shape)         # Displays the shape of input data
    print("Shape of Y : ",Y.shape)         # Displays the shape of output data

    print(border)
    print("Input columns : ",X.columns.tolist())  # Displays all input feature names
    print("Output column : Class")               # Displays the target column name
    print(border)


    # Step 4 : Split the dataset for training and testing
    print(border)
    print("Step 4 : Split the dataset for training and testing")
    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,Y,test_size=0.2,random_state=42,stratify=Y
    )                                     # Splits 80% data for training and 20% for testing

    print(border)
    print("Details of training and testing data")

    print("Shape of X_train : ",X_train.shape)  
    print("Shape of X_test : ",X_test.shape)    

    print("Shape of Y_train : ",Y_train.shape)  
    print("Shape of Y_test : ",Y_test.shape)    

    print(border)


    # Step 5 : Feature Scaling
    print(border)
    print("Step 5 : Feature Scaling")
    print(border)

    scaler = StandardScaler()             # Creates a StandardScaler object

    X_train_scaled = scaler.fit_transform(X_train)  # Learns scaling parameters from training data and transforms the training data

    X_test_scaled = scaler.transform(X_test)        # Applies the same scaling parameters to testing data

    print("Feature Scaling done")

    print(border)


    # Step 6 : Hyperparameter tuning
    print(border)
    print("Step 6 : Hyperparameter tuning")
    print(border)

    accuracy_scores = []                  # Stores accuracy for every K value

    K_values = range(1,21)                # Tests K values from 1 to 20


    # Tests the KNN model for every K value
    for k in K_values:

        model = KNeighborsClassifier(n_neighbors=k)     # Creates KNN model with current K value
        model = model.fit(X_train_scaled,Y_train)        # Trains the KNN model using training data
        Y_pred = model.predict(X_test_scaled)           # Predicts output for testing data
        accuracy = accuracy_score(Y_test,Y_pred)        # Calculates accuracy of the model
        accuracy_scores.append(accuracy)                 # Stores the accuracy in the list

    print("Accuracy report : ")

    # Displays accuracy for every K value
    for k,accuracy in zip(K_values,accuracy_scores):
        print("K =",k,"Accuracy =",accuracy)

    print(border)

    # Find the best K value
    Best_accuracy = max(accuracy_scores)        # Finds the highest accuracy

    Best_K = K_values[accuracy_scores.index(Best_accuracy)] # Finds the K value corresponding to highest accuracy

    print("Best K value : ",Best_K)
    print("Best Accuracy : ",Best_accuracy * 100,"%")

    print(border)


    # Step 7 : Train final model using best K
    print(border)
    print("Step 7 : Final KNN Model")
    print(border)

    model = KNeighborsClassifier(n_neighbors=Best_K)     # Creates final KNN model using best K value
    model.fit(X_train_scaled,Y_train)     # Trains the final KNN model
    Y_pred = model.predict(X_test_scaled)       # Predicts classes for testing data
    Final_accuracy = accuracy_score(Y_test,Y_pred)      # Calculates final model accuracy
    print("Final Accuracy : ",Final_accuracy * 100,"%")

    print(border)


    # Display confusion matrix
    print("Confusion Matrix : ")
    print(confusion_matrix(Y_test,Y_pred))      # Displays correct and incorrect predictions

    print(border)


    # Step 8 : Graphical representation
    print(border)
    print("Step 8 : Graphical representation")
    print(border)

    plt.figure(figsize=(8,5))              # Creates a figure with width 8 and height 5

    plt.plot(K_values,accuracy_scores,marker="o")       # Plots K values against their accuracy
    plt.title("K values vs Accuracy")      # Sets the graph title
    plt.xlabel("Value of K")               # Sets the X-axis label
    plt.ylabel("Accuracy")                 # Sets the Y-axis label
    plt.grid(True)                         # Displays grid lines on the graph
    plt.xticks(list(K_values))             # Displays all K values on the X-axis
    plt.show()                             # Displays the graph

# Main function
def main():

    MarvellousClassifier("WinePredictor.csv")       # Calls the classifier function and passes the CSV file name


# Program execution starts from here
if __name__ == "__main__":

    main()                                 # Calls the main function

