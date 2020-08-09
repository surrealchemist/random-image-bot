import boto3
import botocore
import os
import random
import tempfile
from twython import Twython, TwythonError

import json

BUCKET_NAME = os.environ['BUCKET_NAME']
APP_KEY = os.environ['APP_KEY']
APP_SECRET = os.environ['APP_SECRET']
OAUTH_TOKEN = os.environ['OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = os.environ['OAUTH_TOKEN_SECRET']

s3 = boto3.resource('s3')
bucket = s3.Bucket(BUCKET_NAME)

def lambda_handler(event, context):
    KEY = random.choice(list(bucket.objects.all())).key
    print(KEY)
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    tmp_dir = tempfile.gettempdir()
    path = os.path.join(tmp_dir, KEY)
    print("created directory at " + path)
    try:
        s3.Bucket(BUCKET_NAME).download_file(KEY, path)
        print('file moved to temp directory')
        with open(path, 'rb') as img:
            try:
                twit_resp = twitter.upload_media(media=img)
                twitter.update_status(status=KEY , media_ids=twit_resp['media_id'])
                print("image tweeted")
            except TwythonError as e:
                print(e)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object " + KEY + " does not exist.")
        else:
            raise
