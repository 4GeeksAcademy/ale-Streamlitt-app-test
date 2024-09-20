import streamlit as st
import random

def main():
    st.title("Predict your insurance price")

    age = st.number_input("Enter your age", min_value=0, max_value=120, value=25)

    sex = st.selectbox("Select your sex", ("Male", "Female"))

    bmi = st.number_input("Enter your BMI", min_value=0.0, max_value=100.0, value=22.5, format="%.1f")

    has_children = st.radio("Do you have children?", ('Yes', 'No'))
    children = 1 if has_children == 'Yes' else 0

    is_smoker = st.radio("Are you a smoker?", ('Yes', 'No'))
    smoker = 1 if is_smoker == 'Yes' else 0

    if st.button("Predict Insurance Price"):
        insurance_price = random.randint(499, 4999)
    
        st.write(f"Predicted Insurance Price: ${insurance_price} $")

if __name__ == "__main__":
    main()