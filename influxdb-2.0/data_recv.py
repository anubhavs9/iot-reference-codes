import json
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

class QueryData():
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
            self.query_api = self.client.query_api()
        except Exception as influx_error:
            print(f'Error: {influx_error}')
            exit(-1)

    def queryData(self, query):
        print("Querying data")
        result = self.query_api.query(org=self.org, query=query)
        results = []
        for table in result:
            for record in table.records:
                results.append((record.get_field(), record.get_value()))
        print(results)

    def queryStream(self, query):   
        print("Querying data stream")
        records = self.query_api.query_stream(org=self.org, query=query)
        for record in records:
            print(record.get_field(), record.get_value())


if __name__ == "__main__":
    q = QueryData()
    query = f'from(bucket:"{q.bucket}")\
        |> range(start: -5m)\
        |> filter(fn:(r) => r._measurement == "my_measurement")\
        |> filter(fn: (r) => r.location == "Prague")\
        |> filter(fn:(r) => r._field == "temperature" )'
    q.queryData(query=query)
    # q.queryStream(query=query)
    print("\nDone.")