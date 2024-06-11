#Cargando bibliotecas
import pandas as pd 
import streamlit as st
import openpyxl

#Agregar un titulo
st.title("Aplicacion para cargar archivos de Excel")

#Agregando una imagen (logo)
#st.image("",caption="Logo IC",use_column_width=True)

#Subir el archivo Excel
archivo_excel = st.file_uploader("Selecciona un archivo excel" , type="xlsx") 

if archivo_excel:
    try:
        df = pd.read_excel(archivo_excel)
        
        #Mostrar el contenido del DataFrame
        st.dataframe(df)
        
        #Opciones Adicionales
        #1. Informacion especifica del DataFrame
        st.write("Informacion del DataFrame: ")
        st.write("Numero de filas: ",df.shape[0])
        st.write("Numero de columnas: ",df.shape[1])
        st.write("Nombre de las colmunas: ",df.columns.to_list())
        
        #2.Select colmunas para mostrar
        columnas_seleccionadas = st.multiselect("Selecciona las columnas para mostrar: ",df.columns)
        if columnas_seleccionadas:
            st.dataframe(df[columnas_seleccionadas])
        #3. Filtrar por rangos de fechas
        if 'Fecha' in df.columns:
            if pd.api.types.is_datetime64_any_dtype(df['Fecha']):
                fecha_inicio = st.date_input("Fecha de inicio: ")
                fecha_fin = st.date_input("Fecha de fin: ")
                if fecha_inicio and fecha_fin:
                    fecha_inicio = pd.to_datetime(fecha_inicio)
                    fecha_fin = pd.to_datetime(fecha_fin)
                    
                    df_filtrado = df[(df['Fecha'] >= fecha_inicio)& (df["Fecha"]<= fecha_fin)]
                    st.dataframe(df_filtrado)
            else:
                st.write("La columna 'Fecha' no es de tipo datatime") 
        else:
            st.write("La columna 'Fecha' no esta presente en el archivo Excel")
        
    except Exception as e:
        st.error(f"Error al leer el archivo: {e}")