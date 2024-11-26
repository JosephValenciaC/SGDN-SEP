# mi_aplicacion/utils.py

import pandas as pd

def convertir_csv_a_excel(csv_path, excel_path):
    try:
        df = pd.read_csv(csv_path, encoding='utf-8')
        df.to_excel(excel_path, index=False, engine='openpyxl')
        return f"Archivo convertido correctamente: {excel_path}"
    except Exception as e:
        return f"Error al convertir el archivo: {e}"
