import streamlit as st
import requests

# Título principal de la aplicación
st.title('BAMK Data Solutions')
st.write("Datos inteligentes para decisiones inteligentes")
st.markdown('***')
st.sidebar.markdown('')

# Título secundario de la aplicación
st.title("Predicción de Flujos Migratorios")

# Define las opciones del menú
options = ["Home", "Seleccionar País", "Información Automática", "Consulta Manual"]

# Crear una barra lateral con el menú de opciones
selected_option = st.sidebar.radio("Seleccione una opción", options)

# Función para obtener información de la API
def obtener_informacion(api_url, params=None):
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f'Error al obtener la información desde la API. Código de estado: {response.status_code}')
        st.error(response.text)

if selected_option == "Home":
    st.write("Esta es la página de inicio de la aplicación. Seleccione una opción en el menú lateral para comenzar.")

# Página para seleccionar el país
elif selected_option == "Seleccionar País":
    st.title("Seleccionar País")
    
    # Añade elementos de entrada para las características necesarias para hacer predicciones
    option = st.selectbox(
        'País',
        ("Argentina", "Australia", "Brazil", "China", "France", "Germany", "India", "Indonesia", "Italy", "Japan", "Korea, Rep.", "Mexico",
         "Netherlands", "Russian Federation", "Saudi Arabia", "Spain", "Switzerland", "Turkiye", "United Kingdom", "United States","Afghanistan",
         "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Antigua and Barbuda", "Armenia", "Aruba", "Austria", "Azerbaijan", "Bahamas, The",
         "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia and Herzegovina",
         "Botswana", "British Virgin Islands", "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon",
         "Canada", "Cayman Islands", "Central African Republic", "Chad", "Channel Islands", "Chile", "Colombia", "Comoros", "Congo, Dem. Rep.",
         "Congo, Rep.", "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Curacao", "Cyprus", "Czechia", "Denmark", "Djibouti", "Dominica",
         "Dominican Republic", "Ecuador", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Egypt, Arab Rep.", "Eswatini", "Ethiopia",
         "Faroe Islands", "Fiji", "Finland", "French Polynesia", "Gabon", "Gambia, The", "Georgia", "Ghana", "Gibraltar", "Greece", "Greenland",
         "Grenada", "Guam", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hong Kong SAR, China", "Hungary", "Iceland",
         "Iran, Islamic Rep.", "Iraq", "Ireland", "Isle of Man", "Israel", "Jamaica", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, Dem. People's Rep.",
         "Kosovo", "Kuwait", "Kyrgyz Republic", "Lao PDR", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg",
         "Macao SAR, China", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Micronesia, Fed. Sts.",
         "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "New Caledonia", "New Zealand",
         "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Northern Mariana Islands", "Norway", "Oman", "Pakistan", "Palau","Panama", "Papua New Guinea",
         "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Puerto Rico", "Qatar"))
    
    # Agrega un botón para realizar la petición a la API cuando el usuario lo presiona
    if st.button('Realizar Predicción'):
        # Verifica si el campo del país está completo antes de realizar la petición
        if option:
            # Construye los datos para enviar a la API
            params = {'pais': option}
            # Realiza la petición a la API y obtiene la respuesta
            api_url = "https://prediccion-migracion.onrender.com/Modelo de prediccion/Predice con datos del 2019"
            response = requests.get(api_url, params=params)
            if response.status_code == 200:
                result = response.json()
                prediction = result['prediccion']
                st.write(f'Predicción: {prediction}')
            else:
                st.error(f'Error al obtener la predicción desde la API. Código de estado: {response.status_code}')
                st.error(response.text)  # Imprime la respuesta de la API para obtener más detalles
        else:
            st.warning('Por favor seleccione un país antes de obtener la predicción.')

# Página de Información Automática
elif selected_option == "Información Automática":
    st.title("Información Automática")
    # Define la URL de la API correspondiente para la información automática
    api_url = "https://prediccion-migracion.onrender.com/Modelo de prediccion/Lista de predicciones del 2019"
    
    # Verifica si se ha seleccionado un país y agrega un botón para obtener información automática
    if st.button("Obtener Información Automática"):
        # Realiza la petición a la API y obtiene la respuesta
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            # Puedes mostrar la información en la página
            st.write(data)
        else:
            st.error(f'Error al obtener la información automática desde la API. Código de estado: {response.status_code}')
            st.error(response.text)  # Imprime la respuesta de la API para obtener más detalles
            
# Página de Consulta Manual
elif selected_option == "Consulta Manual":
    st.title("Consulta Manual")
    # Define la URL de la API correspondiente para la consulta manual
    api_url_manual = "https://prediccion-migracion.onrender.com/Modelo de prediccion/Insercion de datos manual"
    
    # Agrega elementos de entrada para las características necesarias
    feature1 = st.number_input('Muertes por conflicto', step=1)
    feature2 = st.number_input('Control de corrupción')
    feature3 = st.slider('Crecimiento PIB (%)', min_value=0.0, max_value=20.0)
    feature4 = st.slider('Tasa desempleo (%)', min_value=0.0, max_value=30.0)
    
    # Agrega un botón para realizar la consulta manual
    if st.button('Realizar Consulta Manual'):
        # Verifica si todos los campos están completos antes de realizar la consulta
        if feature1 is not None and feature2 is not None and feature3 is not None and feature4 is not None:
            # Construye los datos para enviar a la API
            params = {
                'crecimiento_pib': feature3,
                'tasa_desempleo': feature4,
                'muertes_conflicto': feature1,
                'control_corrupcion': feature2
            }
            # Realiza la petición a la API y obtiene la respuesta
            response_manual = requests.get(api_url_manual, params=params)
            if response_manual.status_code == 200:
                result_manual = response_manual.json()
                prediction_manual = result_manual['prediccion']
                st.write(f'Predicción: {prediction_manual}')
            else:
                st.error(f'Error al obtener la predicción desde la API. Código de estado: {response_manual.status_code}')
                st.error(response_manual.text)
        else:
            st.warning('Por favor complete todos los campos antes de realizar la consulta manual.')



