#!/usr/local/bin/python
from pathlib import Path
import os
import boto3
import sys
from botocore.exceptions import ClientError
import mimetypes

ENV_S3_BUCKET_NAME = 'S3_BUCKET_NAME'
ENV_SITE_CONTENTS_PATH = 'SITE_CONTENTS_PATH'
site_contents_file_path = Path(os.environ.get(ENV_SITE_CONTENTS_PATH))


def get_mimetype(object_path):
    content_type, encoding = mimetypes.guess_type(object_path)
    if content_type is None:
       return 'binary/octet-stream'
    return content_type
    

class BucketManager:

    def __init__(self, bucket_name):
        self._s3_client = boto3.client('s3')
        self._bucket_name = bucket_name

    def upload_files(self, object_path):
        #https://stackoverflow.com/questions/34550816/aws-content-type-settings-in-s3-using-boto3
        # If the object is taken from the parent directory, then the key is the file name
        bucket_key = object_path.name
        # If the object originates from one of the subdirectories, its key would be the relative path
        # AWS S3 uses / to derive paths and create folders in the bucket itself
        if len(object_path.parts) > 3:
            bucket_key = "/".join(object_path.parts[2:])
        try:
            if object_path.is_file():
                sys.stdout.write(f'Uploading {bucket_key}\n')
                content_type = get_mimetype(object_path)
                response = self._s3_client.upload_file(str(object_path), self._bucket_name, bucket_key, 
                    ExtraArgs={'ContentType':content_type})
            if object_path.is_dir():
                for os_obj in object_path.iterdir():
                    self.upload_files(os_obj)
        except ClientError as e:
            sys.stderr.write(str(e))
            sys.stderr.flush()
            exit(1) #return exit code 1 to the container
            return False
        return True

def upload_site_contents():
    s3_bucket_name = os.environ.get(ENV_S3_BUCKET_NAME)
    s3_manager = BucketManager(s3_bucket_name)
    s3_manager.upload_files(site_contents_file_path)
    sys.stdout.flush()
    

upload_site_contents()
