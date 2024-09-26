# Ejercicio DEVOPS-PYTHON-DOCKER

Este proyecto configura un entorno Docker utilizando Docker Compose, que incluye dos servicios:
- `mongodb`: Un servicio de base de datos MongoDB.
- `python-api`: Un servicio API desarrollado en FastAPI que interactúa con MongoDB.


## Ejecutar el proyecto

1. **Archivo .env**

   Crea un archivo .env en la raíz del proyecto con las siguientes variables de entorno:

   ```bash
   MONGODB_HOST=mongodb
   MONGODB_PORT=27017
   TZ=XX/XX
   ```

2. **Crear los directorios necesarios**

   Crea los directorios necesarios para los volúmenes de datos y logs:

   ```bash
   mkdir -p volumes/logs
   ```

3. **Ejecutar los contenedores**
Esto iniciará ambos contenedores y los conectará utilizando una red de Docker llamada mongodb-net.

```bash
docker-compose --profile mongodb --profile python-api up --build
   ```

   4. **Ejecutar un servicio en especifico**

   Si se prefiere ejecutar solo uno de los servicios, se puede hacerlo utilizando el comando --profile para seleccionar el perfil deseado. Por ejemplo, para ejecutar solo MongoDB:

   ```bash
   docker-compose --profile mongodb up --build

   ```
   O solo ejecutar el api de python:

```bash
docker-compose --profile python-api up --build
   ```
   5. **Detener los servicios**

   Para detener los servicios en ejecución, utiliza el comando:

   ```bash
docker-compose down

   ```

   ## Endpoints del API

- **/lista-ordenada**: Ordena una lista desordenada de números.
- **/guardar-lista-no-ordenada**: Guarda una lista desordenada junto con la hora del sistema y un ID único en MongoDB.
- **/healthcheck**: Verifica el estado de la aplicación.
### Ejemplos de Endpoints

Ordenar la lista:

 ```bash
curl "http://localhost:8000/lista-ordenada?lista-no-ordenada=[5,4,3,2,1,]"
  ```

 Verificar el estado del API:

  ```bash
curl http://localhost:8000/healthcheck
  ```

## MONGO DB

Guardar la lista no ordenada:

```bash
curl "http://localhost:8000/guardar-lista-no-ordenada?lista-no-ordenada=%5B4%2C3%2C2%2C1%5D"
  ```

