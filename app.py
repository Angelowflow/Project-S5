import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Graficar información de venta de autos')
car_data = pd.read_csv('vehicles_us.csv')

hist_button = st.button('Construir histograma') #crear botón histograma

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer") # crear un histograma
    st.plotly_chart(fig, use_container_width=True) # mostrar un gráfico Plotly interactivo

scatter_button = st.button('Construir gráfico de dispersión') #crear botón dispersión

if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y='price') # crear un gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True) # mostrar un gráfico Plotly interactivo
