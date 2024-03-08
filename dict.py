import os
import pandas as pd

script_dir = os.path.dirname(__file__)
model_path = os.path.join(script_dir, 'data', 'Medicamentos.xlsx')

# Lee el archivo Excel
df = pd.read_excel(model_path)

# Leer linea por linea del excel
for index, row in df.iterrows():
    if 'MIRCERA' in row['medicamento']:
        print(row['nregistro'])