import boto3

from datetime import datetime, timedelta
from config.constants import Constants

s3_client = boto3.client('s3')
constants = Constants()

def upload_db_to_s3():
    s3_client.upload_file(Bucket=constants.BUCKET_NAME, Key=constants.DB_FILE_NAME, Filename=constants.LOCAL_DB_PATH)

def download_db_from_s3():
    print(str(constants.BUCKET_NAME), str(constants.DB_FILE_NAME), str(constants.LOCAL_DB_PATH))
    s3_client.download_file(Bucket=constants.BUCKET_NAME, Key=constants.DB_FILE_NAME, Filename=constants.LOCAL_DB_PATH)
