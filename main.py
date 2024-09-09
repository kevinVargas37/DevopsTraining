from fastapi import FastAPI, HTTPException, Query
from datetime import datetime
from typing import List

app = FastAPI()


@app.get("/lista-ordenada")
async def lista_ordenada(
    lista_no_ordenada: str = Query(
        ...,
        alias="lista-no-ordenada",
        description="Cadena de texto con números separados por comas",
    )
):
    """
    Ordena una lista desordenada de números y devuelve la lista ordenada junto con la hora actual del sistema.

    Args:
    - lista_no_ordenada (str): Una cadena de texto que representa una lista de números separados por comas.
      Ejemplo: "[5,4,7,2,3,2]"

    Returns:
    - dict: Un diccionario que contiene la hora actual del sistema y la lista de números ordenada.

    Raises:
    - HTTPException: Si la cadena proporcionada no puede convertirse en una lista de enteros.
    """
    try:
        # Convertir la cadena de texto a una lista de enteros
        lista_no_ordenada = lista_no_ordenada.strip("[]").split(",")
        lista_no_ordenada = [int(x) for x in lista_no_ordenada]
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="La lista debe contener solo números enteros separados por comas.",
        )

    # Ordenar la lista
    lista_ordenada = sorted(lista_no_ordenada)

    # Obtener la hora actual del sistema
    hora_sistema = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Retornar la respuesta con la lista ordenada y la hora del sistema
    return {"hora_sistema": hora_sistema, "lista_ordenada": lista_ordenada}


@app.get("/healthcheck")
async def healthcheck():
    """
    Endpoint para verificar el estado de la aplicación.

    Returns:
    - str: Devuelve "OK" si la aplicación está funcionando correctamente.
    """
    return "OK"
