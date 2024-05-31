import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title="PrediccionPrecioCarros",
                   page_icon='perrito fachero.jpeg',
                   layout="centered",
                   initial_sidebar_state="auto")

st.title("Prediccion de precios en carros de 2do uso")
st.markdown("""Esta aplicacion se basa en la prediccion de precios de distintos modelos de autos que ingreses :) """)
st.markdown("""---""")

logo="CARRO.jpg"
st.sidebar.image(logo,width=250)
image="perrito fachero.jpeg"    
st.sidebar.image(image,width=150)
st.sidebar.header('Datos Ingresados por el usuario')

uploaded_file = st.sidebar.file_uploader('cargue su archivo CSV', type=["csv"])

if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_features():
        Brand = st.sidebar.select_slider("Marca del Auto",
                                         options=["Toyota","Honda","Ford","Maruti","Hyundai","Tata","Mahindra","Volkswagen","Audi","BMW","Mercedes"])
        if Brand=="Toyota":
            Brand=1
        if Brand=="Honda":
            Brand=2
        if Brand=="Ford":
            Brand=3
        if Brand=="Maruti":
            Brand=4
        if Brand=="Hyundai":
            Brand=5
        if Brand=="Tata":
            Brand=6
        if Brand=="Mahindra":
            Brand=7
        if Brand=="Volkswagen":
            Brand=8    
        if Brand=="Audi":
            Brand=9
        if Brand=="BMW":
            Brand=10
        if Brand=="Mercedes":
            Brand=11
        Year = st.sidebar.slider('Ponga el año del vehiculo',1990,2024,2005)
        Kilometers_Driven = st.sidebar.slider('Inserte el kilometraje del vehiculo',20000,100000,50000)
        Fuel_Type = st.sidebar.select_slider('Ponga el tipo de combustible que usa',
                                             options=["Petroleo","Diesel"])
        if Fuel_Type=="Petroleo":
            Fuel_Type=0
        if Fuel_Type=="Diesel":
            Fuel_Type=1
        Transmission = st.sidebar.slider("Inserte el tipo de transmision que tiene el carro\n"
                                         "manual=1, automatic = 0",0,1,0)
        data = {'Brand':Brand,
                'Year':Year,
                'Kilometers_Driven':Kilometers_Driven,
                'Fuel_Type':Fuel_Type,
                'Transmission':Transmission
                }


        features = pd.DataFrame(data,index=[0])  
        return features
    
    input_df = user_input_features()

input_df = input_df[:1]

st.subheader('datos ingresados por el usuario')

if uploaded_file is not None:
    st.write(input_df)
else:
    st.write('Esperando el archivo CSV. Actualmente solo datos manuales')
    st.write(input_df)


load_clf = pickle.load(open('DatasetCarros.pkl','rb'))
prediccion = load_clf.predict(input_df)

st.subheader("Probable Precio en Soles S/.")
st.subheader(prediccion)

st.markdown("""---""")

