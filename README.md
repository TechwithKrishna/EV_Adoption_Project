
# 🚗 Electric Vehicle Adoption Prediction

 A machine learning project that predicts **Electric Vehicle (EV) adoption** based on customer demographics, income, commuting behavior, charging infrastructure, environmental concern, current vehicle type, subsidy availability, and range anxiety.

 The project includes:

 - 🤖 Random Forest machine learning model
- ⚖️ Balanced Random Forest model for classification
- 🚀 FastAPI REST API
- 🎨 Streamlit web application
- 📊 One-hot encoded categorical features
- 🔮 Real-time EV adoption prediction

---

 ## 📁 Project Structure

```
EV-Adoption-Prediction/
│
├── .venv/
│
├── api.py
├── app.py
├── requirements.txt
├── README.md
│
├── random_forest_balanced_model.joblib
│
├── Predicting_Electric_Vehicle_Purchases.ipynb
│
├── train.csv
├── test.csv
│
├── sample_submission.csv
├── submission.csv
└── submission (1).csv
```

---

 ## 🧠 Machine Learning Model

 The trained model is stored in:

```
random_forest_balanced_model.joblib
```

 The model uses numerical and one-hot encoded categorical features.

 ### Numerical Features

```
Age
Annual_Income_USD
Daily_Commute_km
Number_of_Cars_Owned
Charging_Stations_Near_Home
Charging_Stations_Near_Work
Environmental_Concern_Level
```

 ### Categorical Features

```
Gender
City_Type
Current_Car_Type
Home_Charging_Possible
Subsidy_Available
Range_Anxiety_Level
```

 After one-hot encoding, the API expects the following 18 features:

```
Age
Annual_Income_USD
Daily_Commute_km
Number_of_Cars_Owned
Charging_Stations_Near_Home
Charging_Stations_Near_Work
Environmental_Concern_Level
Gender_Male
Gender_Other
City_Type_Suburban
City_Type_Urban
Current_Car_Type_SUV
Current_Car_Type_Sedan
Current_Car_Type_Truck
Home_Charging_Possible_Yes
Subsidy_Available_Yes
Range_Anxiety_Level_Low
Range_Anxiety_Level_Medium
```

---

 ## ⚙️ Requirements

 The project uses Python and the following libraries:

```
fastapi
uvicorn
streamlit
requests
pandas
scikit-learn
joblib
pydantic
```

 Install all dependencies with:

```
pip install -r requirements.txt
```

---

 ## 🛠️ Virtual Environment Setup

 ### Windows PowerShell

 Create a virtual environment:

```
python -m venv .venv
```

 Activate it:

```
.\.venv\Scripts\Activate.ps1
```

 You should see:

```
(.venv)
```

 at the beginning of your terminal.

 Install dependencies:

```
pip install -r requirements.txt
```

---

 # 🚀 Running the Application

 The application consists of two components:

 1. FastAPI backend
2. Streamlit frontend

 Both need to be running.

---

 ## 1️⃣ Start FastAPI

 Open a terminal and activate the virtual environment:

```
.\.venv\Scripts\Activate.ps1
```

 Start FastAPI:

```
uvicorn api:app --reload
```

 The API will run at:

```
http://127.0.0.1:8000
```

 ### FastAPI Swagger Documentation

 Open:

```
http://127.0.0.1:8000/docs
```

 You can use Swagger UI to test the `/predict` endpoint.

---

 ## 2️⃣ Start Streamlit

 Open a **second terminal** in the project directory.

 Activate the virtual environment:

```
.\.venv\Scripts\Activate.ps1
```

 Run:

```
streamlit run app.py
```

 If the `streamlit` command is not recognized, use:

```
python -m streamlit run app.py
```

 The Streamlit application will normally be available at:

```
http://localhost:8501
```

---

 # 🔄 Application Architecture

```
                 User
                  │
                  ▼
        ┌─────────────────────┐
        │     Streamlit       │
        │       app.py        │
        │      Port 8501      │
        └──────────┬──────────┘
                   │
                   │ HTTP POST
                   ▼
        ┌─────────────────────┐
        │      FastAPI        │
        │       api.py        │
        │      Port 8000      │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │   Random Forest     │
        │   Balanced Model    │
        │      .joblib        │
        └──────────┬──────────┘
                   │
                   ▼
             Prediction
```

---

 # 🔌 API Endpoint

 ## `POST /predict`

 The API accepts customer information and returns the model prediction and probability.

 ### Example Request

```
{
  "Age": 28,
  "Annual_Income_USD": 90000,
  "Daily_Commute_km": 15,
  "Number_of_Cars_Owned": 1,
  "Charging_Stations_Near_Home": 5,
  "Charging_Stations_Near_Work": 4,
  "Environmental_Concern_Level": 5,
  "Gender_Male": 0,
  "Gender_Other": 1,
  "City_Type_Suburban": 0,
  "City_Type_Urban": 1,
  "Current_Car_Type_SUV": 0,
  "Current_Car_Type_Sedan": 0,
  "Current_Car_Type_Truck": 1,
  "Home_Charging_Possible_Yes": 1,
  "Subsidy_Available_Yes": 1,
  "Range_Anxiety_Level_Low": 1,
  "Range_Anxiety_Level_Medium": 0
}
```

 ### Example Response

```
{
  "prediction": 0,
  "probability": 0.8031314489227954
}
```

 The exact prediction depends on the trained model and input values.

 > **Note:** The meaning of `0` and `1` depends on how the target variable was encoded during model training. Check the notebook to determine which class corresponds to EV adoption.

---

 # 📊 Streamlit Features

 The Streamlit application provides input controls for:

 ### Customer Information

 - Age
- Annual Income
- Daily Commute
- Number of Cars Owned
- Charging Stations Near Home
- Charging Stations Near Work
- Environmental Concern Level

 ### Categorical Information

 - Gender
- City Type
- Current Car Type
- Home Charging Possible
- Subsidy Available
- Range Anxiety Level

 After entering the information, click:

```
🔮 Predict EV Adoption
```

 The application sends the processed features to the FastAPI backend and displays the prediction.

---

 # 🔢 One-Hot Encoding

 Categorical variables are converted into numerical values using one-hot encoding.

 For example:

```
Current_Car_Type = SUV
```

 becomes:

```
Current_Car_Type_SUV    = 1
Current_Car_Type_Sedan  = 0
Current_Car_Type_Truck  = 0
```

 Similarly:

```
Range_Anxiety_Level = Medium
```

 becomes:

```
Range_Anxiety_Level_Low     = 0
Range_Anxiety_Level_Medium  = 1
```

 The omitted category acts as the reference category.

---

 # 🧪 Testing the API

 After starting FastAPI, open:

```
http://127.0.0.1:8000/docs
```

 Select:

```
POST /predict
```

 Click:

```
Try it out
```

 Paste the JSON request and click:

```
Execute
```

 The response will contain the prediction.

---

 # ⚠️ Troubleshooting

 ## FastAPI connection error

 Make sure FastAPI is running:

```
uvicorn api:app --reload
```

---

 ## Streamlit cannot connect to API

 Make sure `app.py` contains:

```
API_URL = "http://127.0.0.1:8000/predict"
```

 Also make sure FastAPI is running before using Streamlit.

---

 ## Streamlit command not found

 Use:

```
python -m streamlit run app.py
```

---

 ## Model file not found

 Make sure this file is in the same directory as `api.py`:

```
random_forest_balanced_model.joblib
```

 The API should load it using:

```
MODEL_PATH = "random_forest_balanced_model.joblib"
```

---

 ## Feature mismatch error

 If you see an error such as:

```
ValueError: X has 18 features, but RandomForestClassifier is expecting 16 features
```

 check the model:

```
import joblib

model = joblib.load(
    "random_forest_balanced_model.joblib"
)

print(model.n_features_in_)
print(model.feature_names_in_)
```

 The API feature list must match the features used during model training.

---

 # 📦 Dataset

 The project contains:

```
train.csv
test.csv
```

 The machine learning workflow and model development are documented in:

```
Predicting_Electric_Vehicle_Purchases.ipynb
```

---

 # 🎯 Project Goal

 The goal of this project is to build an end-to-end machine learning application that can:

 1. Process customer and vehicle data.
2. Encode categorical variables.
3. Train a Random Forest classification model.
4. Save the trained model.
5. Expose the model through a FastAPI REST API.
6. Provide a user-friendly Streamlit interface.
7. Generate real-time EV adoption predictions.

---

 # 👨‍💻 Technologies Used

 - **Python**
- **Pandas**
- **Scikit-learn**
- **Random Forest**
- **Joblib**
- **FastAPI**
- **Uvicorn**
- **Streamlit**
- **Pydantic**
- **REST API**

---

 # 📌 Quick Start

 After cloning/downloading the project:

```
python -m venv .venv

.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

 Start the backend:

```
uvicorn api:app --reload
```

 In another terminal, start the frontend:

```
python -m streamlit run app.py
```

 Then open:

```
Streamlit:
http://localhost:8501

FastAPI:
http://127.0.0.1:8000

Swagger:
http://127.0.0.1:8000/docs
```

---

 ## ✅ Project Status

 **Status:** Completed

 The project provides an end-to-end deployment pipeline from a trained machine learning model to a REST API and interactive web interface.
