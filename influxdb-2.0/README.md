# InfluxDB 2.x Reference

This folder contains sample codes which can be used as reference for sending and querying data to/from InfluxDB 2.x.

## Prerequisites
- InfluxDB 2.x up and running in your system.
- Python 3.6+
- InfluxDB python client

    ```py
    python3 -m pip install influxdb_client
    ```

## Instructions
- Edit config.json file and add your token, bucket name, organization and url.
- Send Data to InfluxDB - in Terminal 1

    ```py
        python3 data_gen.py
    ```
- Query Data from InfluxDB - in Terminal 2

    ```py
        python3 data_recv.py
    ```
- Visialize stored data on InfluxDB console
- 
## License

MIT