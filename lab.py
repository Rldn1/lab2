# Importando la libreria pandas
import pandas as pd
import numpy as np

# Cargando los datasets
df = pd.read_csv('zoo.csv')
df_class = pd.read_csv('class.csv')

# describe() para resumir la información
print("RESUMEN ESTADÍSTICO CON describe():")
print(df.describe())

# Identificar tipos de datos
print("\n3. TIPOS DE DATOS CON dtypes:")
print(df.dtypes)
print("\nAnálisis: Las columnas numéricas representan características binarias (0/1) o contadores como 'legs'")

# Mostrar primeros y últimos registros
print("\n4. PRIMEROS REGISTROS CON head():")
print(df.head())
print("\nÚLTIMOS REGISTROS CON tail():")
print(df.tail())

# Ordenar resultados
print("\n5. ORDENADO POR PATAS (DESCENDENTE) CON sort_values():")
print(df.sort_values('legs', ascending=False)[['animal_name', 'legs']].head())
print("\nORDENADO POR TIPO DE CLASE:")
print(df.sort_values('class_type')[['animal_name', 'class_type']].head())

# medidas estadísticas 
print("\n6. MEDIDAS ESTADÍSTICAS:")
print("Columna 'legs':")
print(f"a. Media: {np.mean(df['legs']):.2f}")
print(f"b. Mediana: {np.median(df['legs'])}")
print(f"c. Desviación estándar: {np.std(df['legs']):.2f}")

print("\nColumna 'hair':")
print(f"a. Media: {np.mean(df['hair']):.2f}")
print(f"b. Mediana: {np.median(df['hair'])}")
print(f"c. Desviación estándar: {np.std(df['hair']):.2f}")
