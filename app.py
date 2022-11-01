from flask import Flask, render_template
import datetime
import os

app = Flask(__name__)

@app.route("/")
@app.route('/<custom_text>')
def upload_to_s3(custom_text='Something special'):
    S3_REGION = os.environ.get('REGION_NAME')
    S3_HOST = os.environ.get('HOST_NAME')
    S3_BUCKET = os.environ.get('AWS_BUCKET_NAME')
    FILE_NAME = "test.txt"

    text_to_upload = str(datetime.datetime.now()) + " : " + custom_text

    return render_template('index.html',
                           custom_text=text_to_upload,
                           s3_bucket=S3_HOST+'/'+S3_BUCKET+'/'+FILE_NAME)
