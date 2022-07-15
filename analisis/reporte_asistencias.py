import pandas as pd
import matplotlib.pyplot as plt
import csv

datos_del_estudiate = pd.read_csv('datos\estudiante.csv')
print('ESTUDIANTES')

print(datos_del_estudiate)

datos_de_asistencia = pd.read_csv('datos\datos_asistencia.csv')

print('ASISTENCIAS')

print(datos_de_asistencia)

uniton_tablas_estudiante = pd.merge(datos_del_estudiate,datos_de_asistencia, how='right')

print(uniton_tablas_estudiante)

print('ESTUDIANTES POR CEDULA = 1111000011')

print(uniton_tablas_estudiante[uniton_tablas_estudiante.cedula == 1111000011])

uniton_tablas_estudiante[uniton_tablas_estudiante.cedula == 1111000011].to_csv('datos\datos_reporte_1111000011.csv', index=True)

uniton_tablas_estudiante[uniton_tablas_estudiante.cedula == 1111000011]['fecha_año'].value_counts().plot(kind='bar')

plt.show()

