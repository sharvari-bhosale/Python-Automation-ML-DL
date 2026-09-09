import pandas as pd                                      # Import Pandas for data handling

from sklearn.model_selection import train_test_split    # Import function to split dataset
from sklearn.ensemble import GradientBoostingRegressor  # Import Gradient Boosting Regressor
from sklearn.metrics import mean_squared_error, r2_score # Import evaluation metrics

#----------------------------------------------------------------------
# Step 1 : Load the data
#----------------------------------------------------------------------

df = pd.read_csv("california_housing.csv")               # Load California Housing dataset
print("Shape : ", df.shape)                              # Display rows and columns of dataset
print("First few records : ", df.head())                 # Display first five records


#----------------------------------------------------------------------
# Step 2 : Separate independent and dependent variables
#----------------------------------------------------------------------

X = df.drop("target", axis=1)                            # Store input features by removing target column
Y = df["target"]                                         # Store target/output column

print("Shape of X: ", X.shape)                           # Display shape of input features
print("Shape of Y : ", Y.shape)                          # Display shape of target variable


#----------------------------------------------------------------------
# Step 3 : Split dataset for training and testing
#----------------------------------------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(     # Split data into training and testing sets
    X, Y, test_size=0.2, random_state=42
)


#----------------------------------------------------------------------
# Step 4 : Create the boosting model
#----------------------------------------------------------------------

model = GradientBoostingRegressor(                       # Create Gradient Boosting Regression model
    n_estimators=100,                                    # Create 100 boosting stages
    learning_rate=0.1,                                   # Set the contribution of each tree
    max_depth=3,                                         # Set maximum depth of each tree
    random_state=42                                      # Ensure reproducible results
)


#----------------------------------------------------------------------
# Step 5 : Train the model
#----------------------------------------------------------------------

model = model.fit(X_train, Y_train)                       # Train the model using training data


#----------------------------------------------------------------------
# Step 6 : Test the model
#----------------------------------------------------------------------

y_pred = model.predict(X_test)                           # Predict house values using test data


#----------------------------------------------------------------------
# Step 7 : Evaluate the model
#----------------------------------------------------------------------

print("MSE : ", mean_squared_error(Y_test, y_pred))      # Calculate MSE; lower value is better
print("R2 : ", r2_score(Y_test, y_pred))                 # Calculate R2; value closer to 1 is better
