# Customer Churn Prediction

An end-to-end machine learning project that predicts whether a telecom customer is likely to churn based on customer demographics, services, contract details, and billing information.

## Problem Statement

Customer churn is an important business problem for telecom companies. Identifying customers who are likely to leave can help businesses take retention actions.

This project builds a machine learning pipeline that:

* Processes customer data
* Handles numerical and categorical features
* Trains classification models
* Evaluates model performance
* Predicts churn probability for a new customer
* Provides an interactive Streamlit web application

## Dataset

The project uses a Telco customer churn dataset containing customer demographic, service, contract, and billing information.

The target variable is:

* `Churn Value = 0` → Customer did not churn
* `Churn Value = 1` → Customer churned

The final model uses 19 input features.

### Features

* Gender
* Senior Citizen
* Partner
* Dependents
* Tenure Months
* Phone Service
* Multiple Lines
* Internet Service
* Online Security
* Online Backup
* Device Protection
* Tech Support
* Streaming TV
* Streaming Movies
* Contract
* Paperless Billing
* Payment Method
* Monthly Charges
* Total Charges

## Data Preprocessing

The preprocessing pipeline performs different operations for numerical and categorical features.

### Numerical Features

* Missing values are handled using median imputation.
* Features are standardized using `StandardScaler`.

### Categorical Features

* Missing values are handled using most-frequent imputation.
* Categorical values are converted using `OneHotEncoder`.
* `handle_unknown="ignore"` allows the application to handle previously unseen categorical values.

A `ColumnTransformer` combines both preprocessing pipelines.

## Models

Three classification approaches were evaluated:

1. Logistic Regression
2. Decision Tree
3. Random Forest with hyperparameter tuning

ROC-AUC was used as an important comparison metric.

### Model Performance

| Model               | ROC-AUC |
| ------------------- | ------: |
| Logistic Regression |  ~0.848 |
| Decision Tree       |  ~0.679 |
| Tuned Random Forest |  ~0.835 |

Logistic Regression was selected for the deployed application based on the evaluation performed in this project.

## Classification Performance

The Logistic Regression model achieved approximately:

* Accuracy: 80%
* Churn Precision: 64%
* Churn Recall: 57%
* Churn F1-score: 60%

Because identifying churners can be important, threshold tuning was also evaluated.

At a threshold of `0.40`:

* Churn Recall: 66%
* Churn Precision: 58%
* Accuracy: 78%

This demonstrates the trade-off between detecting more potential churners and generating more false positives.

## Project Structure

```text
Customer-Churn-Prediction/
│
├── app/
│   └── app.py
│
├── data/
│   └── Telco_customer_churn.xlsx
│
├── models/
│   └── churn_model.pkl
│
├── notebooks/
│   └── 01_eda.ipynb
│
├── src/
│   └── predict.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd Customer-Churn-Prediction
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app/app.py
```

The application will open in your browser.

## Application

The Streamlit application allows users to enter customer information such as:

* Tenure
* Contract type
* Internet service
* Payment method
* Monthly charges
* Total charges
* Additional services

The model then displays:

* Churn prediction
* Churn probability
* Decision threshold

## Machine Learning Pipeline

```text
Customer Data
      ↓
Data Cleaning
      ↓
Feature / Target Separation
      ↓
Train-Test Split
      ↓
Numerical + Categorical Preprocessing
      ↓
Logistic Regression
      ↓
Model Evaluation
      ↓
Saved Model
      ↓
Streamlit Application
      ↓
Customer Input
      ↓
Churn Prediction
```

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib
* Streamlit
* Jupyter Notebook

## Future Improvements

Possible improvements include:

* Hyperparameter optimization
* Better class-imbalance handling
* Probability calibration
* Feature importance and model interpretability
* Additional model comparison
* Model monitoring
* Cloud deployment
