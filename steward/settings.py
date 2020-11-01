import logging
from decouple import config
from influxdb import InfluxDBClient
from rich.logging import RichHandler

Logger = logging.getLogger(__name__)
Logger.setLevel(logging.INFO)
Logger.addHandler(RichHandler(rich_tracebacks=True))

INFLUXDB_HOST = config("INFLUXDB_HOST", default="127.0.0.1")
INFLUXDB_PORT = config("INFLUXDB_PORT", cast=int, default=8086)
INFLUXDB_DB = config("INFLUXDB_DB", default="Steward")
INFLUXDB_CLIENT = InfluxDBClient(host=INFLUXDB_HOST, port=INFLUXDB_PORT)
INFLUXDB_CLIENT.create_database(INFLUXDB_DB)

INTERVAL = config("INTERVAL", cast=int, default=30)

