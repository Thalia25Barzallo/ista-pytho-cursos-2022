from asyncio.windows_events import NULL
from escuela_api import api

def test_lista_estudiante():
    assert api.login_cedula_primer_nombre('1111000011','THALIA') == 'correcto'