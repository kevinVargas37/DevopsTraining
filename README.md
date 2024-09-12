# Ejercicio DEVOPS-PYTHON-DOCKER

Proyecto de entrenamiento, contiene un API en python hecha en FastAPI dentro de un contenedor Docker.

## Endpoints del API

- **/lista-ordenada**: Ordena una lista desordenada de números.
- **/guardar-lista-no-ordenada**: Guarda una lista desordenada junto con la hora del sistema y un ID único en MongoDB.
- **/healthcheck**: Verifica el estado de la aplicación.

1. **Construir la imagen Docker**

   En la raíz del proyecto, ejecuta el siguiente comando para construir la imagen Docker:

   ```bash
   docker build -t python-api .
   ```

2. **Ejecutar el contenedor**

   Una vez que la imagen se haya construido correctamente, puedes ejecutar el contenedor con el
   siguiente comando:

   ```bash
   docker run -d -p 8000:8000 python-api
   ```

   Acá vamos a tener arriba: `http://localhost:8000`. en el puerto 8000.

### Ejemplos de Endpoints

Ordenar la lista:

 ```bash
  curl "http://localhost:8000/lista-ordenada?lista-no-ordenada=[5,4,3,2,1,]"
  ```

 Verificar el estado del API:

  ```bash
  curl http://localhost:8000/healthcheck
  ```

# MONGO DB

1. **Levantar servicios de Docker Compose**

   Ejecutar el siguiente comando para construir la imagen Docker y levantar el entorno con Docker Compose
   
   ```bash
   docker-compose up --build
   ```
   
### Ejemplos de Endpoints

Guardar la lista no ordenada:

```bash
  curl "http://localhost:8000/guardar-lista-no-ordenada?lista-no-ordenada=%5B4%2C3%2C2%2C1%5D"
  ```
