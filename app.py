import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.title("ANALYSIS SOLD VEHICLES")
st.write('**Exploratory Data Analysis**')

st.write('Firts rows of the dataframe:')
st.dataframe(car_data.head())


hist_button = st.button('Creating a histogram') # crear un botón de histograma
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creating a histogram for the car sales advertisements dataset')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

hist_button = st.button('Creating a bar chart') # crear un botón de barras

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creating a bar chart for the condition car of dataset')
    
    # crear un grafico de barras
    fig = px.bar(car_data, x="condition")
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación para crear el gráfico de dispersión
hist_checkbox = st.checkbox('Creating a scatter plot')  # Crear una casilla de verificación

if hist_checkbox:  # Si la casilla está marcada
    st.write('Creating a scatter plot for the car sales advertisements dataset')

    # Crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
    
    # Mostrar el gráfico interactivo de Plotly
    st.plotly_chart(fig, use_container_width=True)