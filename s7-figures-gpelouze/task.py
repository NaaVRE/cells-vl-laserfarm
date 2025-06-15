from minio import Minio
import rasterio
import os
import matplotlib.pyplot as plt
import rasterio.plot as rp

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()

secret_minio_access_key = os.getenv('secret_minio_access_key')
secret_minio_secret_key = os.getenv('secret_minio_secret_key')

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--geotiff_file_local', action='store', type=str, required=True, dest='geotiff_file_local')

arg_parser.add_argument('--param_feature_name', action='store', type=str, required=True, dest='param_feature_name')
arg_parser.add_argument('--param_minio_endpoint', action='store', type=str, required=True, dest='param_minio_endpoint')
arg_parser.add_argument('--param_minio_public_dataset_prefix', action='store', type=str, required=True, dest='param_minio_public_dataset_prefix')
arg_parser.add_argument('--param_minio_user_bucket', action='store', type=str, required=True, dest='param_minio_user_bucket')
arg_parser.add_argument('--param_minio_user_prefix', action='store', type=str, required=True, dest='param_minio_user_prefix')

args = arg_parser.parse_args()
print(args)

id = args.id

geotiff_file_local = args.geotiff_file_local.replace('"','')

param_feature_name = args.param_feature_name.replace('"','')
param_minio_endpoint = args.param_minio_endpoint.replace('"','')
param_minio_public_dataset_prefix = args.param_minio_public_dataset_prefix.replace('"','')
param_minio_user_bucket = args.param_minio_user_bucket.replace('"','')
param_minio_user_prefix = args.param_minio_user_prefix.replace('"','')

conf_local_path_figures = conf_local_path_figures = os.path.join('/tmp/data', 'figures')
conf_local_tmp = conf_local_tmp = '/tmp/data'

src = rasterio.open(geotiff_file_local)

os.makedirs(conf_local_path_figures, exist_ok=True)

ax = plt.gca()
rio_plot = rp.show((src, 1), interpolation='none', ax=ax)
img = rio_plot.get_images()[0]
cb = plt.colorbar(img, ax=ax)
cb.set_label(f'{param_feature_name}')
plt.xlabel('EPSG:28992 X [m]')
plt.ylabel('EPSG:28992 Y [m]')
plt.show()
map_file_local = os.path.join(
    conf_local_path_figures, f'{param_feature_name}_map.pdf',
    )
map_file_remote = os.path.join(
    param_minio_user_prefix, param_minio_public_dataset_prefix,
    os.path.relpath(map_file_local, conf_local_tmp),
    )
plt.savefig(map_file_local)

rp.show_hist(
    src,
    bins=50,
    lw=0.0,
    stacked=False,
    alpha=0.3,
    histtype='stepfilled',
    title="Histogram",
    )
plt.show()
histogram_file_local = os.path.join(
    conf_local_path_figures, f'{param_feature_name}_histogram.pdf',
    )
histogram_file_remote = os.path.join(
    param_minio_user_prefix, param_minio_public_dataset_prefix,
    os.path.relpath(histogram_file_local, conf_local_tmp),
    )
plt.savefig(histogram_file_local)

mc = Minio(
    endpoint=param_minio_endpoint,
    access_key=secret_minio_access_key,
    secret_key=secret_minio_secret_key,
    )
print(f'Uploading {map_file_local} to {param_minio_user_bucket}/{map_file_remote}')
mc.fput_object(file_path=map_file_local, bucket_name=param_minio_user_bucket, object_name=map_file_remote)
print(f'Uploading {histogram_file_local} to {param_minio_user_bucket}/{histogram_file_remote}')
mc.fput_object(file_path=histogram_file_local, bucket_name=param_minio_user_bucket, object_name=histogram_file_remote)

