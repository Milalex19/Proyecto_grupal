import os
import pymysql

class DatabaseHandler:
    def __init__(self):
        db_host = os.environ["DB_HOST"]
        db_user = os.environ["DB_USER"]
        db_password = os.environ["DB_PASSWORD"]
        db_name = os.environ["DB_NAME"]

        self.connection = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )

    def insert_dataframe(self,dataframe, table_name):
        try:
            with self.connection.cursor() as cursor:
                for _, row in dataframe.iterrows():
                    pais = row['Pais']
                    año = row['Año']

                    select_query = f"SELECT COUNT(*) FROM `{table_name}` WHERE `Pais` = %s AND `Año` = %s"
                    cursor.execute(select_query, (pais, año))
                    existe_registro = cursor.fetchone()[0]

                    if 'Hombre_origen' in dataframe.columns:
                        if existe_registro == 0:
                            insert_query = f"INSERT INTO `{table_name}` (`Pais`, `Año`, `Hombre_origen`, `Mujer_origen`) VALUES (%s, %s, %s, %s)"
                            cursor.execute(insert_query, (pais, año, row['Hombre_origen'], row['Mujer_origen']))
                        else:
                            update_query = f"UPDATE `{table_name}` SET `Hombre_origen` = %s, `Mujer_origen` = %s WHERE `Pais` = %s AND `Año` = %s"
                            cursor.execute(update_query, (row['Hombre_origen'], row['Mujer_origen'], pais, año))
                    elif 'Hombre_destino' in dataframe.columns:
                        if existe_registro == 0:
                            insert_query = f"INSERT INTO `{table_name}` (`Pais`, `Año`, `Hombre_destino`, `Mujer_destino`) VALUES (%s, %s, %s, %s)"
                            cursor.execute(insert_query, (pais, año, row['Hombre_destino'], row['Mujer_destino']))
                        else:
                            update_query = f"UPDATE `{table_name}` SET `Hombre_destino` = %s, `Mujer_destino` = %s WHERE `Pais` = %s AND `Año` = %s"
                            cursor.execute(update_query, (row['Hombre_destino'], row['Mujer_destino'], pais, año))

            self.connection.commit()
            print("Datos insertados/actualizados correctamente en la base de datos.")
        except Exception as e:
            print(f"Error al insertar/actualizar datos en MySQL: {str(e)}")


    def close_connection(self):
        self.connection.close()
