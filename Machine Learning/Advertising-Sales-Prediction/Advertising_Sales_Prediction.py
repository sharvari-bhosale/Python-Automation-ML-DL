import numpy as np                         # used for numerical calculations
import pandas as pd                        # data handling and DataFrame operations
import matplotlib.pyplot as plt            # for data visualization

from sklearn.linear_model import LinearRegression        # Import Linear Regression algorithm
from sklearn.model_selection import train_test_split     # split data into training and testing sets
from sklearn.metrics import mean_squared_error, r2_score     # Used metrics to evaluate the regression model

# This function performs Multiple Linear Regression on the given dataset

def MarvellousRegression(Datapath):

    border = "-"*40                        

    # Step 1 : Load the data

    print(border)                          
    print("Step 1 : Load the data")       
    print(border)                          

    df = pd.read_csv(Datapath)             # Read the CSV file and store data in DataFrame
    print(df.head())                       # Display the first five records

    # Step 2 : Remove unwanted columns(EDA)

    print(border)                          
    print("Step 2 : Remove unwanted columns(EDA)") 
    print(border)                          

    if "Unnamed: 0" in df.columns:         # Check whether the unwanted column exists
        df = df.drop(columns=["Unnamed: 0"]) # Remove the unwanted column

    print(df.head())                       # Display the first five records after removing the column

    # Step 3 : Check missing values

    print(border)                          
    print("Step 3 : Check missing values") 
    print(border)                         

    print("Total missing values : ")       
    print(border)                          
    print(df.isnull().sum())               # Count and display missing values in each column
    print(border)                          

    # Step 4 : Statistical summary

    print(border)                          
    print("Step 4 : Statistical summary") 
    print(border)                         

    print(df.describe())                   # Display statistical summary of numerical columns

    # Step 5 : Correlation

    print(border)                          
    print("Step 5 : Correlation")          
    print(border)                        

    print(df.corr())                       # Calculate and display correlation between numerical columns

    # Step 6 : Separate Independent and Dependent variables

    print(border)                         
    print("Step 6 : Separate Indepedent and Dependent variables") 
    print(border)                       

    X = df[["TV","radio","newspaper"]]     # Store independent variables in X
    Y = df["sales"]                        # Store dependent variable in Y

    print("Independent variables : ")     
    print(X.head())                       

    print("Dependent variables : ")        
    print(Y.head())                        

    # Step 7 : Split the dataset

    print(border)                         
    print("Step 7 : Split the dataset")   
    print(border)                          

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)   # Split data into 80% training and 20% testing

    print("Training data : ",X_train.shape) # Display the shape of training data

    print("Testing data : ",X_test.shape)   # Display the shape of testing data

    # Step 8 : Create and train the model

    print(border)                          
    print("Step 8 : Create and train the model ") 
    print(border)                          

    model = LinearRegression()             # Create a Linear Regression model

    model = model.fit(X_train, Y_train)    # Train the model using training data
    print("Model trained successfully")    

    # Step 9 : Test the model

    print(border)                          
    print("Step 9 : Test the model ")      
    print(border)                         

    y_Pred = model.predict(X_test)         # Predict sales values using testing data

    print("Expected answers : ")           # Display actual sales values
    print(Y_test[:3])                      # Display first three actual values

    print("Predicted answers : ")          # Display predicted sales values
    print(y_Pred[:3])                      # Display first three predicted values

    # Step 10 : Evaluate the model

    print(border)                          
    print("Step 10 : Evaluate the model ") 
    print(border)                          

    MSE = mean_squared_error(Y_test, y_Pred)        # Calculate Mean Squared Error between actual and predicted values
    RMSE = np.sqrt(MSE)                    # Calculate Root Mean Squared Error from MSE

    R2 = r2_score(Y_test, y_Pred)          # Calculate R-squared score to measure model performance

    print("MSE : ",MSE)                    # Display Mean Squared Error
    print("RMSE : ",RMSE)                  # Display Root Mean Squared Error
    print("R2 : ",R2)                      # Display R-squared score

    # Step 11 : Display Coefficient and Intercept

    print(border)                          
    print("Step 11 : Display Coefficient") 
    print(border)                          

    print("TV coefficient : ", model.coef_[0])          # Display coefficient of TV
    print("Radio coefficient : ", model.coef_[1])           # Display coefficient of Radio
    print("Newspaper coefficient : ", model.coef_[2])        # Display coefficient of Newspaper

    print("Intercept : ", model.intercept_)             # Display the intercept of the regression model

# This is the main function that starts the execution of the program

def main():
    MarvellousRegression("Advertising.csv")         # Call the regression function with the dataset path

# This ensures that main() runs only when this file is executed directly
if __name__ == "__main__":
    main()