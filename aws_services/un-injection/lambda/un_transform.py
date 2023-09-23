# from lambda import df
import pandas as pd


codigo_regiones = [
        900, 947, 1833, 921, 1832, 1830, 1835, 927, 1829, 901, 902, 934, 948, 941, 1636, 1637, 1503, 1517, 1502, 1501, 1500,
        903, 910, 911, 912, 913, 914, 935, 5500, 906, 920, 5501, 922, 908, 923, 924, 925, 926, 904, 915, 916, 931, 905, 909,
        927, 928, 954, 957, 2003
    ]

def transform_destino(data):

    data = data.drop(columns=["Unnamed: 0", 'Notes', 'Type of data', 1990, 1995, 2000, 2005, 2010, 2015, 2020, '1990.1', '1990.2', '1995.1', '1995.2'])
    data.rename(columns={'Region, development group, country or area': 'Pais'}, inplace=True)
    filas_a_eliminar = data['Location code'].isin(codigo_regiones)
    data = data.drop(data[filas_a_eliminar].index)
    data = data.drop(columns=["Location code"])
    columnas_hombres = data.filter(like='.1', axis=1)
    columnas_mujeres = data.filter(like='.2', axis=1)

    data_hombres = pd.melt(data, id_vars=['Pais'], value_vars=columnas_hombres, var_name='Año', value_name='Hombres_destino')
    data_mujeres = pd.melt(data, id_vars=['Pais'], value_vars=columnas_mujeres, var_name='Año', value_name='Mujeres_destino')

    data_hombres['Año'] = data_hombres['Año'].astype(str).str.split('.').str[0]
    data_hombres['Año'] = data_hombres['Año'].astype(int)
    data_mujeres['Año'] = data_mujeres['Año'].astype(str).str.split('.').str[0]
    data_mujeres['Año'] = data_mujeres['Año'].astype(int)

    data_final = pd.merge(data_hombres, data_mujeres, on=['Pais', 'Año'])

    return data_final

    
def transform_origen(data):

    data = data.drop(columns=["Index", 'Notes', 'Type of data', 1990, 1995, 2000, 2005, 2010, 2015, 2020, '1990.1', '1990.2', '1995.1', '1995.2'])
    data.rename(columns={'Region, development group, country or area': 'Pais'}, inplace=True)
    filas_a_eliminar = data['Location code'].isin(codigo_regiones)
    data = data.drop(data[filas_a_eliminar].index)
    data = data.drop(columns=["Location code"])
    columnas_hombres = data.filter(like='.1', axis=1)
    columnas_mujeres = data.filter(like='.2', axis=1)

    data_hombres = pd.melt(data, id_vars=['Pais'], value_vars=columnas_hombres, var_name='Año', value_name='Hombres_origen')
    data_mujeres = pd.melt(data, id_vars=['Pais'], value_vars=columnas_mujeres, var_name='Año', value_name='Mujeres_origen')

    data_hombres['Año'] = data_hombres['Año'].astype(str).str.split('.').str[0]
    data_hombres['Año'] = data_hombres['Año'].astype(int)
    data_mujeres['Año'] = data_mujeres['Año'].astype(str).str.split('.').str[0]
    data_mujeres['Año'] = data_mujeres['Año'].astype(int)

    data_final = pd.merge(data_hombres, data_mujeres, on=['Pais', 'Año'])

    return data_final