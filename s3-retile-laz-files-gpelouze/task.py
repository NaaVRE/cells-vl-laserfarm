import os
import json
from laserfarm import Retiler

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--split_laz_files', action='store', type=str, required=True, dest='split_laz_files')

arg_parser.add_argument('--param_max_x', action='store', type=str, required=True, dest='param_max_x')
arg_parser.add_argument('--param_max_y', action='store', type=str, required=True, dest='param_max_y')
arg_parser.add_argument('--param_min_x', action='store', type=str, required=True, dest='param_min_x')
arg_parser.add_argument('--param_min_y', action='store', type=str, required=True, dest='param_min_y')
arg_parser.add_argument('--param_n_tiles_side', action='store', type=str, required=True, dest='param_n_tiles_side')

args = arg_parser.parse_args()
print(args)

id = args.id

split_laz_files = json.loads(args.split_laz_files)

param_max_x = args.param_max_x.replace('"','')
param_max_y = args.param_max_y.replace('"','')
param_min_x = args.param_min_x.replace('"','')
param_min_y = args.param_min_y.replace('"','')
param_n_tiles_side = args.param_n_tiles_side.replace('"','')

conf_local_path_split = conf_local_path_split = os.path.join('/tmp/data', 'split')
conf_local_path_retiled = conf_local_path_retiled = os.path.join('/tmp/data', 'retiled')

grid_retile = {
    'min_x': float(param_min_x),
    'max_x': float(param_max_x),
    'min_y': float(param_min_y),
    'max_y': float(param_max_y),
    'n_tiles_side': int(param_n_tiles_side),
    }

retiling_input = {
    'setup_local_fs': {
        'input_folder': conf_local_path_split,
        'output_folder': conf_local_path_retiled,
        },
    'set_grid': grid_retile,
    'split_and_redistribute': {},
    'validate': {},
    }

os.makedirs(conf_local_path_retiled, exist_ok=True)
tiles = []

for file in split_laz_files:
    base_name = os.path.splitext(os.path.basename(file))[0]
    retile_record_filename = os.path.join(
        conf_local_path_retiled,
        f'{base_name}_retile_record.js',
        )
    if not os.path.isfile(retile_record_filename):
        print(f'Retiling {file}')
        retiler = Retiler(file, label=file).config(retiling_input)
        retiler.run()
    else:
        print(
            f'Skipping retiling of {file} because {retile_record_filename} already exists'
            )
    with open(retile_record_filename, 'r') as f:
        retile_record = json.load(f)
    tiles += retile_record['redistributed_to']

print(tiles)

file_tiles = open("/tmp/tiles_" + id + ".json", "w")
file_tiles.write(json.dumps(tiles))
file_tiles.close()
