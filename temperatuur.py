
from google.cloud import storage
from config import root, bucketName, sourceBlobName, destinationFileName
import colorsys
import time
import os
import fourletterphat as flp
import time
import csv

#set environment variable for Google API key

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/pi/temperatuur/apikey.json"

#download latest temperature from Google storage

def download_blob(bucketName, sourceBlobName, destinationFileName):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucketName)
    blob = bucket.blob(sourceBlobName)

    blob.download_to_filename(destinationFileName)

download_blob(bucketName, sourceBlobName, destinationFileName)

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
