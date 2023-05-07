import openai
import base64
import requests
import boto3
from config import app,api,API_KEY
from flask_restful import Resource
from models import Image

@app.before_request
def process_request():
    if(request.endpoint!="images"):
        return {"error":"forbidden resource"},401

class Images(Resource):

    def get(self):
        all=Image.query.all()
        images=[]
        for image in all:
            images.append(image.to_dict())
        return images,200

api.add_resource(Images,"/images",endpoint="images") 

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