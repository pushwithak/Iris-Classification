# Iris Flower Classification

This repository hosts a machine learning project designed to classify Iris flowers into one of three species based on their sepal and petal dimensions: Setosa, Versicolor, and Virginica. This project leverages the Iris Flower Dataset in a user-friendly web application developed with Streamlit, enabling easy interaction and visualization.

## Project Overview

The Iris Flower Classification model utilizes the [Iris Flower Dataset](https://archive.ics.uci.edu/dataset/53/iris), which comprises 150 samples from three species of Iris (Iris setosa, Iris virginica, and Iris versicolor). Four features were measured from each sample: the lengths and the widths of the sepals and petals.

This application allows users to input the sepal and petal measurements and receive predictions of the Iris species, along with decision boundary visualizations based on the classification model used.

## Project Steps
### Data Preprocessing:
+ Load the Iris dataset and inspect its structure.
+ Remove unnecessary columns, such as an ID column.
+ Perform any necessary data cleaning or handling of missing values.

### Exploratory Data Analysis (EDA):
+ Explore the dataset by visualizing the relationships between different features.
+ Use plots to understand the distributions and characteristics of each feature.
+ Analyze any correlations or patterns in the data.

### Data Splitting:
+ Split the dataset into training and testing sets.
+ The training set will be used to train the machine learning models, while the testing set will be used for evaluating their performance.

### Model Training:
+ Select multiple machine learning algorithms suitable for classification tasks such as:
    - Logistic Regression
    - Decision Tree
    - Random Forest
    - Naive Bayes (GaussianNB)
    - Support Vector Machine (SVC)
+ Train each model using the training data.
+ Tune hyperparameters, if necessary, using techniques like cross-validation or grid search.

### Model Evaluation:
+ Evaluate the trained models using the testing data.
+ Calculate relevant evaluation metrics to assess the performance of each model.
+ Compare the models and identify the best-performing one for further use.

### Model Selection
The **Random Forest Classifier** was selected for the final deployment due to its superior performance on the provided dataset, particularly in handling the multi-class classification problem inherent to this dataset.

### Model Deployment:
+ Extract the best-performing model along with any necessary preprocessing components, such as the label encoder and scaler.
+ Use the Streamlit library to create a web-based GUI for the Iris flower classification model.
+ Allow users to enter the sepal and petal measurements as input.
+ Utilize the deployed model to predict the species of the Iris flower based on the user input.
+ Display the prediction result to the user.

## Built With
- **Python** - For machine learning logic and calculations.
- **Streamlit** - For creating the web application.
- **Scikit-Learn** - Used for training the machine learning models.
- **Matplotlib** & **Seaborn** - Used for generating interactive visualizations.

## Getting Started
To run this application locally, follow these steps:

### Prerequisites
- Python 3.8 or later
- Pip

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/iris-classification.git](https://github.com/pushwithak/Iris-Classification.git)
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Launch the Streamlit application:
   ```bash
   streamlit run app.py
   ```

Navigate to `http://localhost:8501` in your web browser to use the app.

## Usage
Input the sepal length, sepal width, petal length, and petal width into the app to predict the Iris species. The interface guides the user through the process, from data entry to classification and result visualization.
