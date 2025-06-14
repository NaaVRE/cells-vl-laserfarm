from minio import Minio
import os

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()

secret_minio_access_key = os.getenv('secret_minio_access_key')
secret_minio_secret_key = os.getenv('secret_minio_secret_key')

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--filename', action='store', type=str, required=True, dest='filename')

arg_parser.add_argument('--param_minio_endpoint', action='store', type=str, required=True, dest='param_minio_endpoint')
arg_parser.add_argument('--param_minio_user_bucket', action='store', type=str, required=True, dest='param_minio_user_bucket')
arg_parser.add_argument('--param_minio_user_prefix', action='store', type=str, required=True, dest='param_minio_user_prefix')

args = arg_parser.parse_args()
print(args)

id = args.id

filename = args.filename.replace('"','')

param_minio_endpoint = args.param_minio_endpoint.replace('"','')
param_minio_user_bucket = args.param_minio_user_bucket.replace('"','')
param_minio_user_prefix = args.param_minio_user_prefix.replace('"','')

conf_local_tmp = conf_local_tmp = '/tmp/data'

mc = Minio(
    endpoint=param_minio_endpoint,
    access_key=secret_minio_access_key,
    secret_key=secret_minio_secret_key,
    )

if filename.startswith(conf_local_tmp):
    object_name = os.path.relpath(filename, conf_local_tmp)
else:
    object_name = filename.lstrip('/')
object_name = f'{param_minio_user_prefix}/{object_name}'
print(f'Uploading {filename} to {param_minio_user_bucket}/{object_name}')

mc.fput_object(
    bucket_name=param_minio_user_bucket,
    file_path=filename,
    object_name=object_name,
    )

