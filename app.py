import streamlit as st
import joblib

# Load the model
model = joblib.load('Pickle_RL_Model.pkl')

# Define the Streamlit app
def main():
    st.title('Crop Prediction App')
    st.markdown('This app predicts the suitable crop based on input parameters.')

    # Input form
    st.sidebar.header('Input Parameters')
    nitrogen = st.sidebar.number_input('Nitrogen', min_value=0.0, max_value=1000.0, step=1.0, value=100.0)
    phosphorus = st.sidebar.number_input('Phosphorus', min_value=0.0, max_value=1000.0, step=1.0, value=40.0)
    potassium = st.sidebar.number_input('Potassium', min_value=0.0, max_value=1000.0, step=1.0, value=300.0)
    temperature = st.sidebar.number_input('Temperature (in Celsius)', min_value=-50.0, max_value=50.0, step=1.0, value=25.0)
    humidity = st.sidebar.number_input('Humidity (in %)', min_value=0.0, max_value=100.0, step=1.0, value=50.0)
    ph = st.sidebar.number_input('pH', min_value=0.0, max_value=14.0, step=0.1, value=7.0)
    rainfall = st.sidebar.number_input('Rainfall (in mm)', min_value=0.0, max_value=1000.0, step=1.0, value=100.0)

    # Prediction button
    if st.sidebar.button('Predict'):
        if 0 < ph <= 14 and temperature < 100 and humidity > 0:
            input_data = [[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]]
            prediction = model.predict(input_data)
            st.success(f'The predicted crop is {prediction[0]}')
        else:
            st.error('Error in entered values in the form. Please check the values and fill it again.')

if __name__ == '__main__':
    main()
