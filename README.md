Steward
=======

Steward is a small, easily deployed script for network speed evaluation purposes.
It is meant to easily monitor your network and send the measurements to an [InfluxDB](https://www.influxdata.com/products/influxdb-overview/).
Then using [Chronograf](https://www.influxdata.com/time-series-platform/chronograf/) we can easily visualize the measurements.

![Example](https://raw.githubusercontent.com/gph03n1x/Steward/main/images/Screenshot_2020-11-01%20Chronograf.png)

The whole project was inspired from [this article](http://www.pibits.net/learning/how-to-measure-internet-speed-in-python-using-speedtest.php)


Deployment
----------

### Deploying the TICK stack
The following is a quick way to get the entire TICK Stack spun up and working together.

First you need to clone the official sandbox repository from influxdata.
```bash
git clone https://github.com/influxdata/sandbox/
cd sandbox
```
Then we simply run the following command to start the stack.

```bash
./sandbox up
```
### Deploying Steward
You can build the steward agent image with the following command:
```bash
docker build -t steward:latest .
```

After the image is built you can deploy the agent like this:
```bash
docker run --name steward -d steward:latest
```

### Import Dashboard

Finally you need to import the steward dashboard in chronograf.
There is already an exported dashboard under the `dashboard/` directory.
You can find information on how to import a dashboard **[here](https://docs.influxdata.com/chronograf/v1.8/administration/import-export-dashboards/#import-a-dashboard)**.
