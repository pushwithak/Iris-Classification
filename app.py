import streamlit as st
import pickle 
import pandas as pd

#reading the encoder, model and scaler object files
encoder = pickle.load(open("encoder.pkl", 'rb'))
# model = pickle.load(open("model.pkl", 'rb'))
import pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f, protocol=pickle.HIGHEST_PROTOCOL)

scaler = pickle.load(open("scaler.pkl", 'rb'))

#setting the title and text
st.title("Iris Flower Classification")

# Constraints are added based on the min and max values mentioned
newSL = st.number_input("Sepal Length (cm):", min_value=4.3, max_value=7.9)
newSW = st.number_input("Sepal Width (cm):", min_value=2.0, max_value=4.4)
newPL = st.number_input("Petal Length (cm):", min_value=1.0, max_value=6.9)
newPW = st.number_input("Petal Width (cm):", min_value=0.1, max_value=2.5)

# Button to classify data
if st.button("Classify"):
    # Create a DataFrame with the user inputs
    input_data = pd.DataFrame([[newSL, newSW, newPL, newPW]], 
                              columns=['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'])
    
    # Scaling the input data
    input_scaled = scaler.transform(input_data)
    
    # Make prediction
    prediction = model.predict(input_scaled)
    
    # Decode the prediction result
    predicted_species = encoder.inverse_transform(prediction)
    
    # Display the prediction result
    st.success(f"The Iris flower is classified as: **{predicted_species[0]}**")
