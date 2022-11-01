from flask import Flask, render_template
import datetime
import os

import boto3
from botocore.config import Config


app = Flask(__name__)


@app.route('/health')
def health_check():
    return "I'm okay :)"


@app.route("/")
@app.route('/<custom_text>')
def upload_to_s3(custom_text='Something special'):
    S3_HOST = os.environ.get('HOST_NAME')
    S3_BUCKET = os.environ.get('AWS_BUCKET_NAME')
    FILE_NAME = "test.txt"

    s3 = boto3.client(
        's3',
        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
        region_name=os.environ.get('REGION_NAME'),
        config=Config(s3={'addressing_style': 'auto'})
    )

    text_to_upload = 'Yay!  I\'m a file with the content...\n'
    text_to_upload += str(datetime.datetime.now()) + " : " + custom_text
    with open(FILE_NAME, 'w') as f:
        f.write(text_to_upload)

    with open(FILE_NAME, "rb") as f:
        s3.put_object(Body=f, Bucket=S3_BUCKET, Key=FILE_NAME) #, ContentMD5=md5)

    return render_template('index.html',
                           custom_text=text_to_upload,
                           s3_bucket=S3_HOST+'/'+S3_BUCKET+'/'+FILE_NAME)
