from google.cloud import storage
import tensorflow as tf
from PIL import Image
import numpy as np
from tensorflow.keras.modes import load_model

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
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

    print(f"Blob {source_blob_name} downloaded to {destination_file_name}.")


def predict(request):
    global model
    if model is None:
        download_blob(
            BUCKET_NAME,
            "modesls/crops.h5",
            # /modesls/crops.h5
            "/crops.h5",
        )
        model = load_model("/crops.h5")

    image = request.files["file"]

    image = np.array(
        Image.open(image).convert("RGB").resize((256, 256)) # image resizing
    )

    image = image/255 # normalize the image in 0 to 1 range

    img_array = tf.expand_dims(image, 0)
    predictions = model.predict(img_array)

    print("Predictions:",predictions)

    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)

    return {"class": predicted_class, "confidence": confidence}

