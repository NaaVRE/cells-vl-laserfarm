import os
from laserfarm import DataProcessing

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--tiles', action='store', type=str, required=True, dest='tiles')

arg_parser.add_argument('--param_apply_filter_value', action='store', type=str, required=True, dest='param_apply_filter_value')
arg_parser.add_argument('--param_attribute', action='store', type=str, required=True, dest='param_attribute')
arg_parser.add_argument('--param_feature_name', action='store', type=str, required=True, dest='param_feature_name')
arg_parser.add_argument('--param_filter_type', action='store', type=str, required=True, dest='param_filter_type')
arg_parser.add_argument('--param_max_x', action='store', type=str, required=True, dest='param_max_x')
arg_parser.add_argument('--param_max_y', action='store', type=str, required=True, dest='param_max_y')
arg_parser.add_argument('--param_min_x', action='store', type=str, required=True, dest='param_min_x')
arg_parser.add_argument('--param_min_y', action='store', type=str, required=True, dest='param_min_y')
arg_parser.add_argument('--param_n_tiles_side', action='store', type=str, required=True, dest='param_n_tiles_side')
arg_parser.add_argument('--param_tile_mesh_size', action='store', type=str, required=True, dest='param_tile_mesh_size')
arg_parser.add_argument('--param_validate_precision', action='store', type=str, required=True, dest='param_validate_precision')

args = arg_parser.parse_args()
print(args)

id = args.id

tiles = json.loads(args.tiles)

param_apply_filter_value = args.param_apply_filter_value.replace('"','')
param_attribute = args.param_attribute.replace('"','')
param_feature_name = args.param_feature_name.replace('"','')
param_filter_type = args.param_filter_type.replace('"','')
param_max_x = args.param_max_x.replace('"','')
param_max_y = args.param_max_y.replace('"','')
param_min_x = args.param_min_x.replace('"','')
param_min_y = args.param_min_y.replace('"','')
param_n_tiles_side = args.param_n_tiles_side.replace('"','')
param_tile_mesh_size = args.param_tile_mesh_size.replace('"','')
param_validate_precision = args.param_validate_precision.replace('"','')

conf_local_path_retiled = conf_local_path_retiled = os.path.join('/tmp/data', 'retiled')
conf_local_path_targets = conf_local_path_targets = os.path.join('/tmp/data', 'targets')

feature_files = []

for i, tile in enumerate(tiles):
    grid_feature = {
        'min_x': float(param_min_x),
        'max_x': float(param_max_x),
        'min_y': float(param_min_y),
        'max_y': float(param_max_y),
        'n_tiles_side': int(param_n_tiles_side),
        }

    feature_extraction_input = {
        'setup_local_fs': {
            'input_folder': conf_local_path_retiled,
            'output_folder': conf_local_path_targets,
            },
        'load': {'attributes': [param_attribute]},
        'normalize': 1,
        'apply_filter': {
            'filter_type': param_filter_type,
            'attribute': param_attribute,
            'value': [int(param_apply_filter_value)],
            },
        'generate_targets': {
            'tile_mesh_size': float(param_tile_mesh_size),
            'validate': True,
            'validate_precision': float(param_validate_precision),
            **grid_feature
            },
        'extract_features': {
            'feature_names': [param_feature_name],
            'volume_type': 'cell',
            'volume_size': float(param_tile_mesh_size),
            },
        'export_targets': {
            'attributes': [param_feature_name],
            'multi_band_files': False,
            },
        }
    idx = (tile.split('_')[1:])

    target_file = os.path.join(
        conf_local_path_targets, param_feature_name, tile + '.ply'
        )
    print(target_file)

    if not os.path.isfile(target_file):
        print(f'Extracting features from {tile} ({i + 1} of {len(tiles)})')
        processing = DataProcessing(tile, tile_index=idx, label=tile).config(
            feature_extraction_input
            )
        processing.run()
    else:
        print(
            f'Skipping features extraction for {tile} ({i + 1} of {len(tiles)}) because {target_file} already exists'
            )

    feature_files.append(target_file)

print(feature_files)

file_feature_files = open("/tmp/feature_files_" + id + ".json", "w")
file_feature_files.write(json.dumps(feature_files))
file_feature_files.close()
