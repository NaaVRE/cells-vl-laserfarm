from laserfarm import GeotiffWriter
import os

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--feature_files', action='store', type=str, required=True, dest='feature_files')

arg_parser.add_argument('--param_feature_name', action='store', type=str, required=True, dest='param_feature_name')

args = arg_parser.parse_args()
print(args)

id = args.id

feature_files = json.loads(args.feature_files)

param_feature_name = args.param_feature_name.replace('"','')

conf_local_path_targets = conf_local_path_targets = os.path.join('/tmp/data', 'targets')
conf_local_path_geotiff = conf_local_path_geotiff = os.path.join('/tmp/data', 'geotiff')

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

geo_tiff = os.path.join(
    conf_local_path_geotiff,
    f'geotiff_TILE_000_BAND_{param_feature_name}.tif'
    )
print(geo_tiff)

file_geo_tiff = open("/tmp/geo_tiff_" + id + ".json", "w")
file_geo_tiff.write(json.dumps(geo_tiff))
file_geo_tiff.close()
