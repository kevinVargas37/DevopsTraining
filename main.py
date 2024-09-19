from fastapi import FastAPI, HTTPException, Query
from datetime import datetime
from typing import List
from pymongo import MongoClient
import os
import uuid

app = FastAPI()

# Configuración de MongoDB desde las variables de entorno
mongodb_host = os.getenv("MONGODB_HOST")
mongodb_port = int(os.getenv("MONGODB_PORT"))
try:
    client = MongoClient(mongodb_host, mongodb_port)
    db = client["python_app"]
    collection = db["listas_no_ordenadas"]
except Exception as e:
    print(f"Error conectando a MongoDB: {e}")
    raise HTTPException(status_code=500, detail="Error al conectar con MongoDB.")

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

@app.get("/guardar-lista-no-ordenada")
async def guardar_lista_no_ordenada(
        lista_no_ordenada: str = Query(
            ...,
            alias="lista-no-ordenada",
            description="Cadena de texto con números separados por comas",
        )
):
    """
    Guarda una lista desordenada junto con la hora del sistema y un identificador único en MongoDB.
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

    # Generar un identificador único
    id_unico = str(uuid.uuid4())

    # Obtener la hora actual del sistema
    hora_sistema = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Guardar en MongoDB
    collection.insert_one({
        "id": id_unico,
        "lista_no_ordenada": lista_no_ordenada,
        "hora_sistema": hora_sistema
    })

    # Responder con el mensaje de éxito
    return {"msg": f"La lista fue guardada con el id: {id_unico}"}

@app.get("/healthcheck")
async def healthcheck():
    """
    Endpoint para verificar el estado de la aplicación.

    Returns:
    - str: Devuelve "OK" si la aplicación está funcionando correctamente.
    """
    return "OK"
