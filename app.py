import pandas as pd
import plotly.express as px
import streamlit as st
import sidetable as stb

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

# Título de la aplicación
st.title("ANALYSIS SOLD VEHICLES")
st.write('### Exploratory Data Analysis')

# Crear la función EDA para mostrar resultados en Streamlit
def EDA(data): 
    # Mostrar las primeras filas
    st.write('**First 5 rows of the data:**')
    st.dataframe(data.head())
    
    # Mostrar información del DataFrame en formato de tabla
    st.write('**Dataframe Information:**')
    info_data = {
        "Number of Entries": [data.shape[0]],
        "Number of Columns": [data.shape[1]],
    }
    info_df = pd.DataFrame(info_data)
    st.dataframe(info_df)  # Mostrar el tamaño del DataFrame como tabla
    
    # Mostrar tipos de datos de las columnas
    st.write("**Column Data Types:**")
    dtype_df = pd.DataFrame(data.dtypes, columns=['Data Type']).reset_index()
    dtype_df.columns = ['Column Name', 'Data Type']
    st.dataframe(dtype_df)  # Mostrar tipos de datos de cada columna
    
    # Valores nulos
    st.write('**Null Values:**')
    st.dataframe(data.stb.missing(style=True))  # Mostrar valores nulos por columna
    
    # Valores duplicados
    st.write('**Duplicated Values:**')
    duplicated_data = pd.DataFrame({'Duplicated Rows': [data.duplicated().sum()]})
    st.dataframe(duplicated_data)  # Mostrar valores duplicados

# Llamar a la función EDA para mostrar los resultados
EDA(car_data)

# Crear botones para los gráficos

# Botón para histograma
hist_button = st.button('**Creating a histogram**') # crear un botón de histograma
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creating a histogram for the car sales advertisements dataset')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Botón para gráfico de barras
hist_button = st.button('**Creating a bar chart**') # crear un botón de barras

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creating a bar chart for the condition car of dataset')
    
    # crear un grafico de barras
    fig = px.bar(car_data, x="condition")
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación para gráfico de dispersión
hist_checkbox = st.checkbox('**Creating a scatter plot**')  # Crear una casilla de verificación

if hist_checkbox:  # Si la casilla está marcada
    st.write('Creating a scatter plot for the car sales advertisements dataset')

    # Crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
    
    # Mostrar el gráfico interactivo de Plotly
    st.plotly_chart(fig, use_container_width=True)