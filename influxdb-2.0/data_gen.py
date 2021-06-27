import json
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

class SendData():
    CONFIG_FILE = "./config.json"
    def __init__(self):
        self.readConfigFile()
        self.createInfluxClient()

    def readConfigFile(self):
        try:
            with open(self.CONFIG_FILE, 'r') as fp:
                config_data = json.load(fp)
                self.token = config_data["token"] 
                self.org = config_data["org"] 
                self.bucket = config_data["bucket"] 
                self.url = config_data["url"]
        except Exception as file_error:
            print(f'Error: {file_error}')
            exit(-1)

    def createInfluxClient(self):
        try:
            print("Creating client..")
            self.client = influxdb_client.InfluxDBClient(
                url=self.url, 
                token=self.token, 
                org=self.org
            )
            self.write_api = self.client.write_api(write_options=SYNCHRONOUS)
        except Exception as influx_error:
            print(f'Error: {influx_error}')
            exit(-1)

    def writeData(self, data_point):
        try:    
            self.write_api.write(bucket=self.bucket, org=self.org, record=data_point)
        except Exception as influx_error:
            print(f'Error: {influx_error}')
            exit(-1)


if __name__ == "__main__":
    s = SendData()
    print("Starting write operations...")
    p = influxdb_client.Point("my_measurement").tag("location", "Prague").field("temperature", 25.3)
    s.writeData(p)
    p = influxdb_client.Point("my_measurement2").field("temperature", 50.0)
    s.writeData(p)
    print("\nDone.")