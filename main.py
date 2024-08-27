from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/lista-ordenada")
async def lista_ordenada(lista_no_ordenada: str):
    # Convertir la cadena de texto a una lista de enteros
    lista_no_ordenada = [int(x) for x in lista_no_ordenada.strip('[]').split(',')]
    # URL para probar: http://localhost:8000/lista-ordenada?lista_no_ordenada=[5,4,7,2,3,2]

    # Ordenar la lista
    lista_ordenada = sorted(lista_no_ordenada)

    # Obtener la hora actual del sistema
    hora_sistema = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Retornar la respuesta con la lista ordenada y la hora del sistema
    return {
        "hora_sistema": hora_sistema,
        "lista_ordenada": lista_ordenada
    }
    #
@app.get("/healthcheck")
async def healthcheck():
    return "OK"