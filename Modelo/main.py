import pandas as pd
from fastapi import FastAPI
import uvicorn
import joblib
from enum import Enum

indicadores = pd.read_csv('indicadores.csv')

modelo = joblib.load('modelo_migracion.pkl')

app = FastAPI()

class Pais(str, Enum):
    Argentina = "Argentina"
    Australia = "Australia"
    Brazil = "Brazil"
    China = "China"
    France = "France"
    Germany = "Germany"
    India = "India"
    Indonesia = "Indonesia"
    Italy = "Italy"
    Japan = "Japan"
    Korea_Rep = "Korea, Rep."
    Mexico = "Mexico"
    Netherlands = "Netherlands"
    Russian_Federation = "Russian Federation"
    Saudi_Arabia = "Saudi Arabia"
    Spain = "Spain"
    Switzerland = "Switzerland"
    Turkiye = "Turkiye"
    United_Kingdom = "United Kingdom"
    United_States = "United States"
    Afghanistan = "Afghanistan"
    Albania = "Albania"
    Algeria = "Algeria"
    American_Samoa = "American Samoa"
    Andorra = "Andorra"
    Angola = "Angola"
    Antigua_and_Barbuda = "Antigua and Barbuda"
    Armenia = "Armenia"
    Aruba = "Aruba"
    Austria = "Austria"
    Azerbaijan = "Azerbaijan"
    Bahamas_The = "Bahamas, The"
    Bahrain = "Bahrain"
    Bangladesh = "Bangladesh"
    Barbados = "Barbados"
    Belarus = "Belarus"
    Belgium = "Belgium"
    Belize = "Belize"
    Benin = "Benin"
    Bermuda = "Bermuda"
    Bhutan = "Bhutan"
    Bolivia = "Bolivia"
    Bosnia_and_Herzegovina = "Bosnia and Herzegovina"
    Botswana = "Botswana"
    British_Virgin_Islands = "British Virgin Islands"
    Brunei_Darussalam = "Brunei Darussalam"
    Bulgaria = "Bulgaria"
    Burkina_Faso = "Burkina Faso"
    Burundi = "Burundi"
    Cabo_Verde = "Cabo Verde"
    Cambodia = "Cambodia"
    Cameroon = "Cameroon"
    Canada = "Canada"
    Cayman_Islands = "Cayman Islands"
    Central_African_Republic = "Central African Republic"
    Chad = "Chad"
    Channel_Islands = "Channel Islands"
    Chile = "Chile"
    Colombia = "Colombia"
    Comoros = "Comoros"
    Congo_Dem_Rep = "Congo, Dem. Rep."
    Congo_Rep = "Congo, Rep."
    Costa_Rica = "Costa Rica"
    Cote_dIvoire = "Cote d'Ivoire"
    Croatia = "Croatia"
    Cuba = "Cuba"
    Curacao = "Curacao"
    Cyprus = "Cyprus"
    Czechia = "Czechia"
    Denmark = "Denmark"
    Djibouti = "Djibouti"
    Dominica = "Dominica"
    Dominican_Republic = "Dominican Republic"
    Ecuador = "Ecuador"
    Egypt_Arab_Rep = "Egypt, Arab Rep."
    El_Salvador = "El Salvador"
    Equatorial_Guinea = "Equatorial Guinea"
    Eritrea = "Eritrea"
    Estonia = "Estonia"
    Eswatini = "Eswatini"
    Ethiopia = "Ethiopia"
    Faroe_Islands = "Faroe Islands"
    Fiji = "Fiji"
    Finland = "Finland"
    French_Polynesia = "French Polynesia"
    Gabon = "Gabon"
    Gambia_The = "Gambia, The"
    Georgia = "Georgia"
    Ghana = "Ghana"
    Gibraltar = "Gibraltar"
    Greece = "Greece"
    Greenland = "Greenland"
    Grenada = "Grenada"
    Guam = "Guam"
    Guatemala = "Guatemala"
    Guinea = "Guinea"
    Guinea_Bissau = "Guinea-Bissau"
    Guyana = "Guyana"
    Haiti = "Haiti"
    Honduras = "Honduras"
    Hong_Kong_SAR_China = "Hong Kong SAR, China"
    Hungary = "Hungary"
    Iceland = "Iceland"
    Iran_Islamic_Rep = "Iran, Islamic Rep."
    Iraq = "Iraq"
    Ireland = "Ireland"
    Isle_of_Man = "Isle of Man"
    Israel = "Israel"
    Jamaica = "Jamaica"
    Jordan = "Jordan"
    Kazakhstan = "Kazakhstan"
    Kenya = "Kenya"
    Kiribati = "Kiribati"
    Korea_Dem_Peoples_Rep = "Korea, Dem. People's Rep."
    Kosovo = "Kosovo"
    Kuwait = "Kuwait"
    Kyrgyz_Republic = "Kyrgyz Republic"
    Lao_PDR = "Lao PDR"
    Latvia = "Latvia"
    Lebanon = "Lebanon"
    Lesotho = "Lesotho"
    Liberia = "Liberia"
    Libya = "Libya"
    Liechtenstein = "Liechtenstein"
    Lithuania = "Lithuania"
    Luxembourg = "Luxembourg"
    Macao_SAR_China = "Macao SAR, China"
    Madagascar = "Madagascar"
    Malawi = "Malawi"
    Malaysia = "Malaysia"
    Maldives = "Maldives"
    Mali = "Mali"
    Malta = "Malta"
    Marshall_Islands = "Marshall Islands"
    Mauritania = "Mauritania"
    Mauritius = "Mauritius"
    Micronesia_Fed_Sts = "Micronesia, Fed. Sts."
    Moldova = "Moldova"
    Monaco = "Monaco"
    Mongolia = "Mongolia"
    Montenegro = "Montenegro"
    Morocco = "Morocco"
    Mozambique = "Mozambique"
    Myanmar = "Myanmar"
    Namibia = "Namibia"
    Nauru = "Nauru"
    Nepal = "Nepal"
    New_Caledonia = "New Caledonia"
    New_Zealand = "New Zealand"
    Nicaragua = "Nicaragua"
    Niger = "Niger"
    Nigeria = "Nigeria"
    North_Macedonia = "North Macedonia"
    Northern_Mariana_Islands = "Northern Mariana Islands"
    Norway = "Norway"
    Oman = "Oman"
    Pakistan = "Pakistan"
    Palau = "Palau"
    Panama = "Panama"
    Papua_New_Guinea = "Papua New Guinea"
    Paraguay = "Paraguay"
    Peru = "Peru"
    Philippines = "Philippines"
    Poland = "Poland"
    Portugal = "Portugal"
    Puerto_Rico = "Puerto Rico"
    Qatar = "Qatar"

def obtener_datos_por_pais(pais):
    fila_buscada = indicadores[indicadores['Pais'] == pais]
    if not fila_buscada.empty:
        lista_fila = fila_buscada.iloc[0].drop('Pais').tolist()
    return lista_fila

ind = indicadores

@app.get("/Modelo de prediccion/Predice con datos del 2019")
def prediccion_flujo(pais: Pais):
    datos_prediccion = obtener_datos_por_pais(pais)
    df = pd.DataFrame([datos_prediccion])
    prediccion = modelo.predict(df)
    prediccion_entero = int(prediccion[0])
    return {'prediccion': prediccion_entero}

@app.get("/Modelo de prediccion/Lista de predicciones del 2019")
def lista_predicciones():
    global ind
    datos_prediccion = ind[['Pais', 'Crecimiento_PIB', 'Tasa_desempleo', 'Muertes_Conflicto', 'Control_Corrupcion']]  # Asegúrate de incluir 'Pais' en los datos
    prediccion = modelo.predict(datos_prediccion.iloc[:, 1:])  # Excluye la columna 'Pais' en la predicción
    prediccion_entero = [int(valor) for valor in prediccion]
    #Crea una lista de diccionarios con los datos
    lista_datos = []
    for index, row in datos_prediccion.iterrows():
        pais = row['Pais']
        diccionario = {'Pais': pais, 'Prediccion': prediccion_entero[index]}
        lista_datos.append(diccionario)

    return {'Respuesta':lista_datos}

@app.get("/Modelo de prediccion/Insercion de datos manual")
def prediccion_flujo(crecimiento_pib,tasa_desempleo,muertes_conflicto,control_corrupcion):
    datos_prediccion = {}
    datos_prediccion = [[crecimiento_pib, tasa_desempleo, muertes_conflicto, control_corrupcion,]]
    df = pd.DataFrame(datos_prediccion)
    prediccion = modelo.predict(df)
    prediccion_entero = int(prediccion[0])
    return {'prediccion': prediccion_entero}