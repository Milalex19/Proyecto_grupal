from constant import todos_los_indicadores
from database_handler import DatabaseHandler
from worldbank import WorldBankDataFetcher

def handler(event, context):
  db_handler = DatabaseHandler()
  worldbank = WorldBankDataFetcher()
  try:
    indicadores_df = worldbank.transformacion(todos_los_indicadores)
    db_handler.insert_dataframe(indicadores_df, "indicadores")
    db_handler.close_connection()

  except Exception as e:
      print(f"Hubo un error en la lambda: {str(e)}")
