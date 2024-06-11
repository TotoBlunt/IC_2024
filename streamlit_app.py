#Cargando bibliotecas
import pandas as pd 
import streamlit as st

#Subir el archivo Excel
archivo_excel = st.file_uploader("Selecciona un archivo excel" , type="xlsx") 