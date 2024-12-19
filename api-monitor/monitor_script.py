import os
import time
import requests
import logging

# Configuración de variables de entorno
host = os.getenv("TARGET_CONTAINER_HOST", "localhost")
port = os.getenv("TARGET_CONTAINER_PORT", "8000")
interval = int(os.getenv("CHECK_INTERVAL", "5"))

log_dir = "/opt/monitor/logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "api-monitor.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
)

healthcheck_url = f"http://{host}:{port}/healthcheck"

while True:
    try:
        response = requests.get(healthcheck_url, timeout=5)
        if response.status_code == 200 and response.text.strip() == "OK":
            logging.info(f"El contenedor {host}:{port} está funcionando correctamente.")
        else:
            logging.error(
                f"Respuesta inesperada del contenedor {host}:{port}: "
                f"Status: {response.status_code}, Body: {response.text.strip()}"
            )
    except Exception as e:
        logging.error(f"Error al contactar con {host}:{port}: {e}")
    time.sleep(interval)
