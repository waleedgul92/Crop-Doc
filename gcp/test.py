from google.cloud import storage
import tensorflow as tf
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model

model = None
interpreter = None
input_index = None
output_index = None

class_names = ["diseased cotton leaf","diseased cotton plant","fresh cotton leaf","fresh cotton plant"]

BUCKET_NAME = "crop-doc-bucket" # Here you need to put the name of your GCP bucket
              #crop-doc-bucket

def download_blob(bucket_name, source_blob_name, destination_file_name):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    print("here")
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

    print(f"Blob {source_blob_name} downloaded to {destination_file_name}.")
download_blob(
                BUCKET_NAME,
                "modesls/crops.h5",
                # /modesls/crops.h5
                "/tmp/crops.h5",
            )