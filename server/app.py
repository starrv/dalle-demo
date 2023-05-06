import openai
import base64
import requests
import boto3
from config import API_KEY
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api,Resource
from models import Image

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

api=Api(app)
db.init_app(app)


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

if __name__=="__main__":
    app.run(port=5555,debug=True)