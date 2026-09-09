# Iris Case Study – Decision Tree

## Description

This project is a Machine Learning case study based on the **Iris dataset**.
A **Decision Tree Classifier** is used to classify Iris flowers into different species based on their measurements.

The project demonstrates the complete Machine Learning workflow, starting from loading the dataset and performing exploratory data analysis to training, testing, and evaluating the model.

## Features

* Load Iris dataset from CSV file
* Display sample data
* Perform Exploratory Data Analysis
* Display dataset shape and column names
* Generate statistical summary
* Check for missing values
* Separate independent and dependent variables
* Split dataset into training and testing data
* Create and train a Decision Tree Classifier
* Predict flower species
* Evaluate the model using:

  * Confusion Matrix
  * Accuracy
  * Precision
  * Recall
  * F1 Score

## Technologies Used

* Python
* Pandas
* Scikit-learn

## Dataset

The dataset used in this project is `iris.csv`.

### Input Features

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

### Target

* Species

The model classifies the flowers into three species:

* Setosa
* Versicolor
* Virginica

## Machine Learning Algorithm

### Decision Tree Classifier

A Decision Tree is a supervised machine learning algorithm used for classification and regression tasks.

In this project, the Decision Tree Classifier learns patterns from the Iris flower measurements and predicts the species of a flower.

## Project Workflow

```text
Load Dataset
      ↓
Exploratory Data Analysis
      ↓
Data Cleaning
      ↓
Separate X and Y
      ↓
Train-Test Split
      ↓
Create Decision Tree Model
      ↓
Train Model
      ↓
Make Predictions
      ↓
Model Evaluation
      ↓
Confusion Matrix
Accuracy
Precision
Recall
F1 Score
```

## Train-Test Split

The dataset is divided into:

* **80% Training Data**
* **20% Testing Data**

The model is trained using the training data and evaluated using the testing data.

## Model Evaluation

The following evaluation metrics are used:

### Confusion Matrix

Shows the number of correctly and incorrectly classified samples for each Iris species.

### Accuracy

Measures the overall percentage of correct predictions.

### Precision

Measures how accurately the model predicts each class.

### Recall

Measures how well the model identifies samples belonging to each class.

### F1 Score

Provides a balance between precision and recall.

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project folder

```bash
cd <project-folder>
```

### 3. Install required libraries

```bash
pip install pandas scikit-learn
```

### 4. Keep the dataset in the same folder

Make sure `iris.csv` is present in the project directory.

### 5. Run the program

```bash
python IrisCaseStudy.py
```

## Expected Output

The program displays:

```text
Step 1 : Load the dataset
Step 2 : Exploratory data analysis
Step 3 : Data cleaning
Step 4 : Separate Independent and Dependent Variables
Step 5 : Split dataset for training and testing
Step 6 : Create the model
Step 7 : Train the model
Step 8 : Test the model
Step 9 : Model evaluation
```

It also displays the:

* Dataset information
* Independent variables
* Dependent variable
* Confusion matrix
* Accuracy
* Precision
* Recall
* F1 Score

## Project Structure

```text
Iris-Case-Study/
│
├── IrisCaseStudy.py
├── iris.csv
└── README.md
```

## Conclusion

This project demonstrates how to build a complete Machine Learning classification model using the Iris dataset and a Decision Tree Classifier. It covers data loading, analysis, preprocessing, model training, prediction, and performance evaluation.

