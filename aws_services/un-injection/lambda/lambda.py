import boto3
import pandas as pd
import openpyxl
from io import BytesIO
from database_handler import DatabaseHandler
from un_transform import transform_destino
from un_transform import transform_origen

def handler(event, context):
    records = event.get('Records', [])
    if not records:
        print("No se encontraron registros en el evento.")
        return

    record = records[0] 
    s3_info = record.get('s3', {})
    bucket_name = s3_info.get('bucket', {}).get('name')
    object_key = s3_info.get('object', {}).get('key')

    s3_client = boto3.client('s3')
    db_handler = DatabaseHandler()

    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=object_key)

        content = response['Body'].read()
        content_bytesio = BytesIO(content)

        df = pd.read_excel(content_bytesio, sheet_name='Table 1', skiprows=lambda x: x < 10)

        df_final = pd.DataFrame()

        if 'origin' in object_key:
            df_final = transform_origen(df)
        else:
            df_final = transform_destino(df)

        db_handler.insert_dataframe(df_final, "migracion_origen_destino")
        db_handler.close_connection()

    except Exception as e:
        print(f"Error al descargar y leer el archivo .xlsx: {e}")

