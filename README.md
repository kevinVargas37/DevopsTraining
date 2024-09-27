# Ejercicio DEVOPS-PYTHON-DOCKER

Este proyecto configura un entorno Docker utilizando Docker Compose, que incluye dos servicios:
- `mongodb`: Un servicio de base de datos MongoDB.
- `python-api`: Un servicio API desarrollado en FastAPI que interactúa con MongoDB.

## Explicación de archivo Docker Compose.

El archivo docker-compose.yml define la configuración de dos servicios: mongodb y python-api.

Servicios
mongodb:

- image: Usa la imagen oficial de MongoDB mongo:5.0.3.
- container_name: Nombra al contenedor como mongodb.
- restart: La política de reinicio está configurada en always, lo que significa que  MongoDB siempre intentará reiniciarse en caso de fallos.
- volumes: Utiliza un volumen persistente mongodb_data para guardar los datos de MongoDB en /data/db. Este volumen asegura que los datos persistan aunque el contenedor se destruya o se reinicie.
- networks: Conecta a la red mongodb-net, la misma red que usa el servicio de la API.
- ports: Expone el puerto 27017 para que MongoDB pueda ser accesible desde fuera del contenedor.
- hostname: Asigna un nombre de host único (mongodb).
- profiles: Define un perfil llamado mongodb para ejecutar este servicio.

python-api:

- build: Indica que la API de Python se construirá desde el contexto actual (.).
- container_name: Nombra al contenedor como python-api.
- environment: Usa las variables de entorno definidas en el archivo .env para configurar la conexión con MongoDB.
- volumes: Monta el archivo de logs de la API en un bind mount, de manera que los logs se guarden en ./volumes/logs/info.log en tu sistema local y dentro del contenedor en /opt/python-api/logs/info.log.
- depends_on: Asegura que el servicio mongodb se inicie antes de python-api.
- ports: Expone el puerto 8000 para que puedas acceder a la API en http://localhost:8000.
- networks: Conecta a la red mongodb-net, lo que permite la comunicación con el contenedor de MongoDB.
- profiles: Define un perfil llamado python-api.
- restart: También configurado como always para reiniciar el contenedor en caso de fallos.

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
   touch ./volumes/logs/info.log
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

