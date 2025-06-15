from minio import Minio
from laserfarm import GeotiffWriter
import os

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()

secret_minio_access_key = os.getenv('secret_minio_access_key')
secret_minio_secret_key = os.getenv('secret_minio_secret_key')

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--feature_files', action='store', type=str, required=True, dest='feature_files')

arg_parser.add_argument('--param_feature_name', action='store', type=str, required=True, dest='param_feature_name')
arg_parser.add_argument('--param_minio_endpoint', action='store', type=str, required=True, dest='param_minio_endpoint')
arg_parser.add_argument('--param_minio_public_dataset_prefix', action='store', type=str, required=True, dest='param_minio_public_dataset_prefix')
arg_parser.add_argument('--param_minio_user_bucket', action='store', type=str, required=True, dest='param_minio_user_bucket')
arg_parser.add_argument('--param_minio_user_prefix', action='store', type=str, required=True, dest='param_minio_user_prefix')

args = arg_parser.parse_args()
print(args)

id = args.id

feature_files = json.loads(args.feature_files)

param_feature_name = args.param_feature_name.replace('"','')
param_minio_endpoint = args.param_minio_endpoint.replace('"','')
param_minio_public_dataset_prefix = args.param_minio_public_dataset_prefix.replace('"','')
param_minio_user_bucket = args.param_minio_user_bucket.replace('"','')
param_minio_user_prefix = args.param_minio_user_prefix.replace('"','')

conf_local_path_targets = conf_local_path_targets = os.path.join('/tmp/data', 'targets')
conf_local_path_geotiff = conf_local_path_geotiff = os.path.join('/tmp/data', 'geotiff')
conf_local_tmp = conf_local_tmp = '/tmp/data'

print(feature_files)

geotiff_export_input = {
    'setup_local_fs': {
        'input_folder': conf_local_path_targets,
        'output_folder': conf_local_path_geotiff,
        },
    'parse_point_cloud': {},
    'data_split': {
        'xSub': 1,
        'ySub': 1,
        },
    'create_subregion_geotiffs': {
        'output_handle': 'geotiff'
        },
    }

writer = (
    GeotiffWriter(
        input_dir=param_feature_name,
        bands=param_feature_name,
        label=param_feature_name,
        )
    .config(geotiff_export_input)
    )
writer.run()

geotiff_file_local = os.path.join(
    conf_local_path_geotiff, f'geotiff_TILE_000_BAND_{param_feature_name}.tif',
    )
geotiff_file_remote = os.path.join(
    param_minio_user_prefix, param_minio_public_dataset_prefix,
    os.path.relpath(geotiff_file_local, conf_local_tmp),
    )
print(f'Uploading {geotiff_file_local} to {param_minio_user_bucket}/{geotiff_file_remote}')

mc = Minio(
    endpoint=param_minio_endpoint,
    access_key=secret_minio_access_key,
    secret_key=secret_minio_secret_key,
    )
mc.fput_object(
    bucket_name=param_minio_user_bucket,
    file_path=geotiff_file_local,
    object_name=geotiff_file_remote,
    )

