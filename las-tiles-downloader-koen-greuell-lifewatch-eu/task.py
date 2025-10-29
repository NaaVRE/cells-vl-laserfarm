
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--las_data_filenames', action='store', type=str, required=True, dest='las_data_filenames')


args = arg_parser.parse_args()
print(args)

id = args.id

las_data_filenames = json.loads(args.las_data_filenames)



def download_las_tiles(las_filenames, source="ahn"):
    """
    function that downloads las files.
    No need to return anything, as the filenames are already known.
    """
    return 

download_las_tiles(las_data_filenames)
las_tiles_download_completed = 1

file_las_tiles_download_completed = open("/tmp/las_tiles_download_completed_" + id + ".json", "w")
file_las_tiles_download_completed.write(json.dumps(las_tiles_download_completed))
file_las_tiles_download_completed.close()
