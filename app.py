import openai
import base64
import requests
import boto3
from config import API_KEY

def get_image():
    openai.api_key=API_KEY
    response = openai.Image.create(
    prompt="a white siamese cat",
    n=1,
    size="256x256",
    response_format="b64_json"
    )
    data=response['data'][0]['b64_json'].encode()
    print(data)
    with open("imageToSave2.png", "wb") as fh:
        fh.write(base64.decodebytes(data))
    print("image saved")

def upload_image_s3():
    img_data=None
    try:
        with open("imageToSave2.png", "rb") as fh:
            img_data=fh.read()
        s3 = boto3.resource('s3')
        s3.Bucket('dalle-demo').put_object(Key='cat-image.jpg', Body=img_data)
        print("image saved to s3")
    except Exception as e:
        print(f"Error sending file: {e.args}")

upload_image_s3()