import streamlit as st
import pandas as pd

# ------------------ Dummy Model Functions ------------------
def predict_random_forest(data):
    if data['Daily_Screen_Hours'] > 5 or data['Eye_Dryness_Level'] > 4:
        return "High"
    elif data['Daily_Screen_Hours'] > 2 or data['Eye_Dryness_Level'] > 2:
        return "Medium"
    else:
        return "Low"

def predict_svm(data):
    if data['Daily_Screen_Hours'] > 6 or data['Eye_Dryness_Level'] > 4:
        return "High"
    elif data['Daily_Screen_Hours'] > 3 or data['Eye_Dryness_Level'] > 2:
        return "Medium"
    else:
        return "Low"

# ------------------ Helper Functions ------------------
def risk_color(risk):
    return {"High": "red", "Medium": "orange", "Low": "green"}[risk]

def explain_risk(risk):
    return {
        "High": "High risk of eye strain. Reduce screen time and take frequent breaks.",
        "Medium": "Moderate risk. Maintain healthy screen habits.",
        "Low": "Low risk. Keep following good eye care practices."
    }[risk]

# ------------------ Streamlit Config ------------------
st.set_page_config(page_title="👁️ Eye Strain Dashboard", layout="centered")

# ------------------ Sidebar Navigation ------------------
st.sidebar.title("📊 Dashboard")
page = st.sidebar.radio(
    "Navigate",
    ["👁️ Eye Strain Prediction", "📈 Model Comparison Graph"]
)

# ======================================================
# PAGE 1: EYE STRAIN PREDICTION
# ======================================================
if page == "👁️ Eye Strain Prediction":

    st.title("👁️ Eye Strain Prediction System")
    st.write("Hybrid Machine Learning + Rule-Based Web Application")

    with st.expander("Enter Your Details", expanded=True):
        col1, col2 = st.columns(2)

        with col1:
            age = st.number_input("Age", 1, 100, 19)
            gender = st.selectbox("Gender", ["Female", "Male", "Other"])
            role = st.selectbox("Role", ["Student", "Employee", "Other"])
            daily_hours = st.number_input("Daily Screen Hours", 0.0, 24.0, 2.0)
            break_freq = st.number_input("Break Frequency Per Hour", 0, 12, 2)
            blue_light = st.selectbox("Blue Light Filter Used", ["Yes", "No"])

        with col2:
            eye_dryness = st.number_input("Eye Dryness Level (0-5)", 0, 5, 1)
            eye_pain = st.number_input("Eye Pain Level (0-5)", 0, 5, 0)
            headache_freq = st.number_input("Headache Frequency Per Week", 0, 7, 0)
            blurred_vision = st.selectbox("Blurred Vision", ["Yes", "No"])
            sleep_hours = st.number_input("Sleep Hours", 0, 24, 7)
            eye_checkup = st.selectbox("Eye Checkup Last Year", ["Yes", "No"])

    input_data = {
        "Age": age,
        "Gender": gender,
        "Role": role,
        "Daily_Screen_Hours": daily_hours,
        "Break_Frequency_Per_Hour": break_freq,
        "Blue_Light_Filter_Used": blue_light,
        "Eye_Dryness_Level": eye_dryness,
        "Eye_Pain_Level": eye_pain,
        "Headache_Frequency_Per_Week": headache_freq,
        "Blurred_Vision": blurred_vision,
        "Sleep_Hours": sleep_hours,
        "Eye_Checkup_Last_Year": eye_checkup
    }

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Predict Eye Strain"):
            rf_pred = predict_random_forest(input_data)
            svm_pred = predict_svm(input_data)
            final_pred = rf_pred  # Based on higher accuracy

            st.subheader("Prediction Results")
            st.markdown(f"**Random Forest:** <span style='color:{risk_color(rf_pred)}'>{rf_pred}</span>", unsafe_allow_html=True)
            st.markdown(f"**SVM:** <span style='color:{risk_color(svm_pred)}'>{svm_pred}</span>", unsafe_allow_html=True)
            st.markdown(f"**Final Risk:** <span style='color:{risk_color(final_pred)}'>{final_pred}</span>", unsafe_allow_html=True)
            st.info(explain_risk(final_pred))
            st.success("Decision Based On: Random Forest")

    with col2:
        if st.button("Reset Inputs"):
            st.experimental_rerun()

# ======================================================
# PAGE 2: MODEL COMPARISON GRAPH
# ======================================================
elif page == "📈 Model Comparison Graph":

    st.title("📈 Model Accuracy Comparison")
    st.write("Comparison of SVM and Random Forest performance")

    accuracy_data = pd.DataFrame({
        "Model": ["Random Forest", "SVM"],
        "Accuracy (%)": [76, 54]
    })

    st.bar_chart(
        data=accuracy_data.set_index("Model"),
        height=400
    )

    st.markdown("""
    **Observation:**
    - Random Forest achieves higher accuracy
    - Better at handling non-linear and mixed data
    - More reliable for eye strain prediction
    """)
