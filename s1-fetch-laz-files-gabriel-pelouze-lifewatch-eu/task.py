from minio import Minio
import os

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_bucket_name', action='store', type=str, required=True, dest='param_bucket_name')
arg_parser.add_argument('--param_minio_server', action='store', type=str, required=True, dest='param_minio_server')
arg_parser.add_argument('--param_remote_path_root', action='store', type=str, required=True, dest='param_remote_path_root')

args = arg_parser.parse_args()
print(args)

id = args.id


param_bucket_name = args.param_bucket_name.replace('"','')
param_minio_server = args.param_minio_server.replace('"','')
param_remote_path_root = args.param_remote_path_root.replace('"','')

conf_local_path_raw = conf_local_path_raw = os.path.join('/tmp/data', 'raw')

os.makedirs(conf_local_path_raw, exist_ok=True)
raw_laz_files = []

minio_client = Minio(param_minio_server, secure=True)
objects = minio_client.list_objects(
    param_bucket_name, prefix=param_remote_path_root
    )
for obj in objects:
    if obj.object_name.lower().endswith('.laz'):
        laz_file = os.path.join(
            conf_local_path_raw, obj.object_name.split('/')[-1]
            )
        if not os.path.isfile(laz_file):
            print(
                f'Downloading {param_bucket_name}:{obj.object_name} to {laz_file}'
                )
            minio_client.fget_object(
                param_bucket_name, obj.object_name, laz_file
                )
        else:
            print(
                f'Skipping download of {param_bucket_name}:{obj.object_name} because {laz_file} already exists'
                )
        raw_laz_files.append(laz_file)

print(raw_laz_files)

file_raw_laz_files = open("/tmp/raw_laz_files_" + id + ".json", "w")
file_raw_laz_files.write(json.dumps(raw_laz_files))
file_raw_laz_files.close()
