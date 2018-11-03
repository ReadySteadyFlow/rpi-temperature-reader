from google.cloud import storage
import colorsys
import time
import os
import fourletterphat as flp
import time
import csv

#set environment variable for Google API key

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/pi/temperatuur/apikey.json"

#set variables

bucket_name = "zwaanshals"
source_blob_name = "latest.csv"
destination_file_name = "/home/pi/temperatuur/latest.csv"

#download latest temperature from Google storage

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

    print('Blob {} downloaded to {}.'.format(
        source_blob_name,
        destination_file_name))
    
download_blob(bucket_name, source_blob_name, destination_file_name)

#convert csv values into variables

with open('/home/pi/temperatuur/latest.csv', mode='r') as latest:
  csv_reader = csv.DictReader(latest)
  for row in csv_reader:
    temperature = int(round(float(row["temperature"])))
    humidity = int(round(float(row["humidity"])))
    

#   for row in csv_reader:
#     print(row["temperature"])

#display temperature and humidity

display_value = str(temperature)+str(humidity)

flp.print_number_str(display_value)
flp.show()
time.sleep(870)
