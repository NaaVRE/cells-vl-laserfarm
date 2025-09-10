import rasterio

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--geotiff_file_local', action='store', type=str, required=True, dest='geotiff_file_local')


args = arg_parser.parse_args()
print(args)

id = args.id

geotiff_file_local = args.geotiff_file_local.replace('"','')



src = rasterio.open(geotiff_file_local)
print(geotiff_file_local)

