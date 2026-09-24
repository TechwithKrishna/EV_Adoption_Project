import streamlit as st
import requests


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="EV Adoption Predictor",
    page_icon="🚗",
    layout="centered"
)


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🚗 EV Adoption Prediction")
st.write(
    "Enter the customer details below to predict EV adoption."
)


# --------------------------------------------------
# FastAPI URL
# --------------------------------------------------

API_URL = "http://127.0.0.1:8000/predict"


# --------------------------------------------------
# Numerical inputs
# --------------------------------------------------

st.header("Customer Information")

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=35
)

annual_income = st.number_input(
    "Annual Income (USD)",
    min_value=0.0,
    value=75000.0,
    step=1000.0
)

daily_commute = st.number_input(
    "Daily Commute (km)",
    min_value=0.0,
    value=25.0,
    step=1.0
)

cars_owned = st.number_input(
    "Number of Cars Owned",
    min_value=0,
    max_value=10,
    value=1,
    step=1
)

charging_home = st.number_input(
    "Charging Stations Near Home",
    min_value=0,
    value=2,
    step=1
)

charging_work = st.number_input(
    "Charging Stations Near Work",
    min_value=0,
    value=3,
    step=1
)

environmental_concern = st.slider(
    "Environmental Concern Level",
    min_value=1,
    max_value=5,
    value=4
)


# --------------------------------------------------
# Categorical inputs
# --------------------------------------------------

st.header("Categorical Information")

gender = st.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)

city_type = st.selectbox(
    "City Type",
    ["Urban", "Suburban", "Rural"]
)

current_car_type = st.selectbox(
    "Current Car Type",
    ["SUV", "Sedan", "Truck", "Other"]
)

home_charging = st.selectbox(
    "Home Charging Possible",
    ["Yes", "No"]
)

subsidy = st.selectbox(
    "Subsidy Available",
    ["Yes", "No"]
)

range_anxiety = st.selectbox(
    "Range Anxiety Level",
    ["Low", "Medium", "High"]
)


# --------------------------------------------------
# Create processed payload
# --------------------------------------------------

def create_payload():

    payload = {

        # Numerical features
        "Age": age,
        "Annual_Income_USD": annual_income,
        "Daily_Commute_km": daily_commute,
        "Number_of_Cars_Owned": cars_owned,
        "Charging_Stations_Near_Home": charging_home,
        "Charging_Stations_Near_Work": charging_work,
        "Environmental_Concern_Level": environmental_concern,

        # Gender
        "Gender_Male": 1 if gender == "Male" else 0,
        "Gender_Other": 1 if gender == "Other" else 0,

        # City
        "City_Type_Suburban": 1 if city_type == "Suburban" else 0,
        "City_Type_Urban": 1 if city_type == "Urban" else 0,

        # Current car
        "Current_Car_Type_SUV": (
            1 if current_car_type == "SUV" else 0
        ),
        "Current_Car_Type_Sedan": (
            1 if current_car_type == "Sedan" else 0
        ),
        "Current_Car_Type_Truck": (
            1 if current_car_type == "Truck" else 0
        ),

        # Home charging
        "Home_Charging_Possible_Yes": (
            1 if home_charging == "Yes" else 0
        ),

        # Subsidy
        "Subsidy_Available_Yes": (
            1 if subsidy == "Yes" else 0
        ),

        # Range anxiety
        "Range_Anxiety_Level_Low": (
            1 if range_anxiety == "Low" else 0
        ),
        "Range_Anxiety_Level_Medium": (
            1 if range_anxiety == "Medium" else 0
        )
    }

    return payload


# --------------------------------------------------
# Prediction
# --------------------------------------------------

if st.button(
    "🔮 Predict EV Adoption",
    use_container_width=True
):

    payload = create_payload()

    try:

        with st.spinner("Getting prediction..."):

            response = requests.post(
                API_URL,
                json=payload,
                timeout=10
            )

        if response.status_code == 200:

            result = response.json()

            prediction = result["prediction"]
            probability = result.get("probability")

            st.success("Prediction completed!")

            st.subheader("Prediction")

            st.info(
                f"Prediction: **{prediction}**"
            )

            if probability is not None:

                st.metric(
                    "Prediction Probability",
                    f"{probability * 100:.2f}%"
                )

        else:

            st.error(
                f"API Error: {response.status_code}\n\n"
                f"{response.text}"
            )

    except requests.exceptions.ConnectionError:

        st.error(
            "Could not connect to FastAPI. "
            "Please start the API server first."
        )

    except requests.exceptions.Timeout:

        st.error(
            "The API request timed out."
        )

    except Exception as e:

        st.error(
            f"Unexpected error: {str(e)}"
        )
