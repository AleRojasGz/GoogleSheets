import pandas as pd  # pip install --upgrade pandas
import pypyodbc as obdc
from Google import Create_Service
from sqlalchemy import create_engine

CLIENT_SECRET_FILE = './json/cliente.json'
API_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


google_sheets_id = '' #ID DE LA HOJA DE CALCULO

response = service.spreadsheets().values().get(
    spreadsheetId=google_sheets_id,
    majorDimension='ROWS',
    range='' #Nombre de la hoja de calculos
).execute()

rows = response['values'][1:]
# print(response)
df_rows = pd.DataFrame(rows, columns=[""" Columnas de la hoja de calulo; 'A', 'B', 'C'... """])
print(df_rows)

#CADENA DE CONEXION A MYSQL 
cadena_conexion = 'mysql+pymysql://'
engine = create_engine(cadena_conexion)
df_rows.to_sql(name='', con=engine, if_exists="replace",index= False)
connection=engine.connect()
connection.execute=('ALTER TABLE licempleados ADD CONSTRAINT ID UNIQUE ()')
connection.close()