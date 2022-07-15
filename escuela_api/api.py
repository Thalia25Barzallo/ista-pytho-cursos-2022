from calendar import c
from cmath import pi
from doctest import OutputChecker
from flask import Flask, request
import csv
import json

app = Flask(__name__)

@app.route('/leer_los_estudiates')
def leer_los_estudiates():
    with open('datos\estudiante.csv') as archivo:
        lectura = csv.reader(archivo)
        next(lectura)
        estudiante_lista = []
        for fila in lectura:
            estudiante_lista.append(
                {'cedula': fila[0],
                'primer_apellido': fila[1],
                'segundo_apellido': fila[2],
                'primer_nombre': fila[3],
                'segundo_nombre': fila[4]
                })
    return json.dumps(sorted(estudiante_lista, key=lambda c: c['cedula']))

@app.route('/asistencia_del_estudiante', methods=['POST'])
def asistencia_del_estudiante():
    with open('datos\datos_asistencia.csv', 'a' , newline='') as archivo:
        escritor = csv.writer(archivo,delimiter=',')
        escritor.writerow([
            request.json['cedula'],
            request.json['materia'],
            request.json['fecha_anio'],
            request.json['fecha_mes'],
            request.json['fecha_dia']])
    return 'asistencia creada con satisfacción ' + request.json['cedula']

@app.route('/login_cedula_primer_nombre/<cedula>/<primer_nombre>')
def login_cedula_primer_nombre(cedula,primer_nombre):
    with open('datos\estudiante.csv') as archivo:
        lectura = csv.reader(archivo)
        next(lectura)
        estudiante_lista = []
        for fila in lectura:
            if fila[0] == cedula and fila[3] == primer_nombre:
                estudiante_lista.append(
                {'cedula': fila[0],
                'primer_apellido': fila[1],
                'segundo_apellido': fila[2],
                'primer_nombre': fila[3],
                'segundo_nombre': fila[4]
                })
    return 'correcto'

if __name__ == '__main__':
    app.run(debug=True)