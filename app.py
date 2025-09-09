import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Laptop Price Predictor", layout="centered")

# Load the trained model
model = joblib.load('model/laptop_price_model.pkl')

st.title('💻 Laptop Price Predictor')
st.markdown('Enter the specifications of the laptop to predict its price.')

with st.form("predict_form"):
    st.subheader("Laptop Specifications")
    col1, col2 = st.columns(2)
    with col1:
        company = st.selectbox('Company', ['Dell', 'HP', 'Lenovo', 'Apple', 'Acer', 'Asus', 'MSI', 'Other'])
        typename = st.selectbox('TypeName', ['Notebook', 'Ultrabook', 'Gaming', '2 in 1', 'Workstation', 'Netbook', 'Other'])
        inches = st.slider("Screen Size (inches)", 10.0, 20.0, 15.6, 0.1)
        screenwidth = st.number_input('Screen Width (cm)', value=35.0)
        screenheight = st.number_input('Screen Height (cm)', value=20.0)
        weight = st.number_input('Weight (kg)', value=2.0)
        ram = st.slider("RAM (GB)", 2, 128, 8, 2)
    with col2:
        cpu_brand = st.selectbox('CPU Brand', ['Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'Intel Core i9', 'AMD Ryzen 3', 'AMD Ryzen 5', 'AMD Ryzen 7', 'Other'])
        cpu_speed = st.number_input('CPU Speed (GHz)', min_value=1.0, max_value=5.0, value=2.5)
        ssd = st.number_input("SSD Size (GB)", min_value=0, value=256, step=128)
        hdd = st.number_input("HDD Size (GB)", min_value=0, value=0, step=500)
        hybrid = st.number_input('Hybrid (GB)', min_value=0, max_value=2048, value=0)
        flash_storage = st.number_input('Flash Storage (GB)', min_value=0, max_value=2048, value=0)
        gpu = st.selectbox('GPU', ['Integrated', 'NVIDIA', 'AMD', 'Other'])
        opsys = st.selectbox('Operating System', ['Windows', 'MacOS', 'Linux', 'Other'])

    submitted = st.form_submit_button("Predict Price")

input_dict = {
    'Company': company,
    'TypeName': typename,
    'Inches': inches,
    'ScreenWidth': screenwidth,
    'ScreenHeight': screenheight,
    'Weight': weight,
    'Cpu_brand': cpu_brand,
    'Cpu_speed': cpu_speed,
    'Ram': ram,
    'HDD': hdd,
    'SSD': ssd,
    'Hybrid': hybrid,
    'Flash_Storage': flash_storage,
    'Gpu': gpu,
    'OpSys': opsys
}
input_df = pd.DataFrame([input_dict])

if submitted:
    try:
        prediction = model.predict(input_df)[0]
        st.success(f'Estimated Laptop Price: ₹{prediction:,.0f}')
    except Exception as e:
        st.error(f'Error in prediction: {e}')
