import csv
from datetime import datetime

def generar_sql_desde_csv(nombre_archivo_csv, nombre_archivo_sql):
    """
    Lee un archivo CSV línea por línea, convierte el formato de fecha y moneda,
    genera sentencias SQL para insertar transacciones y saldos,
    guarda las sentencias en un archivo SQL y muestra los errores en la consola.

    Args:
        nombre_archivo_csv (str): El nombre del archivo CSV de entrada.
        nombre_archivo_sql (str): El nombre del archivo SQL de salida.
    """

    try:
        with open(nombre_archivo_csv, 'r', newline='', encoding='utf-8') as archivo_csv, \
             open(nombre_archivo_sql, 'w', encoding='utf-8') as archivo_sql:

            lector_csv = csv.reader(archivo_csv)
            next(lector_csv)  # Omitir la primera línea (encabezados)

            for fila in lector_csv:
                fecha_ejecucion, fecha_valor, descripcion, importe, saldo = fila

                # Limpiar y formatear los datos
                fecha_ejecucion = fecha_ejecucion.strip()
                fecha_valor = fecha_valor.strip()
                descripcion = descripcion.strip().replace('"', '')  # Eliminar comillas dobles

                # Formatear importe y saldo (coma como decimal, punto como miles)
                importe = importe.strip().replace('.', '').replace(',', '.')
                saldo = saldo.strip().replace('.', '').replace(',', '.')

                # Convertir formato de fecha
                fecha_ejecucion = datetime.strptime(fecha_ejecucion, '%d/%m/%Y').strftime('%Y-%m-%d')
                fecha_valor = datetime.strptime(fecha_valor, '%d/%m/%Y').strftime('%Y-%m-%d')

                importe_float = float(importe)

                if importe_float >= 0:
                    # Generar sentencias SQL para importe positivo
                    sentencia_sql_transaccion = f"""
SET @saldo_actual = (SELECT saldo FROM Saldos ORDER BY id_saldo DESC LIMIT 1);
INSERT INTO Transacciones (fecha_ejecucion, fecha_valor, descripcion, importe, saldo) VALUES ('{fecha_ejecucion}', '{fecha_valor}', '{descripcion}', {importe_float}, @saldo_actual + {importe_float});
"""
                    sentencia_sql_saldo = f"""
INSERT INTO Saldos (fecha_saldo, saldo) VALUES ('{fecha_ejecucion}', @saldo_actual + {importe_float});
"""
                else:
                    # Generar sentencias SQL para importe negativo
                    sentencia_sql_transaccion = f"""
SET @saldo_actual = (SELECT saldo FROM Saldos ORDER BY id_saldo DESC LIMIT 1);
INSERT INTO Transacciones (fecha_ejecucion, fecha_valor, descripcion, importe, saldo) VALUES ('{fecha_ejecucion}', '{fecha_valor}', '{descripcion}', {importe_float}, @saldo_actual - {abs(importe_float)});
"""
                    sentencia_sql_saldo = f"""
INSERT INTO Saldos (fecha_saldo, saldo) VALUES ('{fecha_ejecucion}', @saldo_actual - {abs(importe_float)});
"""

                # Escribir sentencias SQL en el archivo
                archivo_sql.write(sentencia_sql_transaccion + '\n')
                archivo_sql.write(sentencia_sql_saldo + '\n')

    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo_csv}' no fue encontrado.")
    except ValueError as e:
        print(f"Error de formato en los datos: {e}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
generar_sql_desde_csv('transacciones.csv', 'transacciones.sql')