import speedtest
from datetime import datetime
import time
from steward.settings import Logger, INFLUXDB_CLIENT, INFLUXDB_DB, INTERVAL
import typer

app = typer.Typer()

TO_MEGABYTE = 1024 * 1024


@app.command()
def monitor(interval: int = INTERVAL):
    s = speedtest.Speedtest()

    while True:
        down_speed = round((round(s.download()) / TO_MEGABYTE), 2)
        up_speed = round((round(s.upload()) / TO_MEGABYTE), 2)
        best_server = s.get_best_server()
        latency = round(best_server['latency'], 2)
        # ping = round((round(s.upload()) / ), 2)
        Logger.info(f"Ping {latency} ms,  Download speed: {down_speed} Mb/s, upload speed: {up_speed} Mb/s")

        speed_event = [
            {
                "measurement": f"speed-test",
                "time": datetime.utcnow().replace(microsecond=0).isoformat(),
                "fields": {
                    "up": up_speed,
                    "down": down_speed,
                    "latency": latency

                },
            }
        ]

        INFLUXDB_CLIENT.write_points(speed_event, database=INFLUXDB_DB)
        time.sleep(interval)


if __name__ == "__main__":
    app()
