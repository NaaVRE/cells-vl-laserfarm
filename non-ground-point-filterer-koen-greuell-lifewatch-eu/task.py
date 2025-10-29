
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--clipped_ALS_point_cloud_names', action='store', type=str, required=True, dest='clipped_ALS_point_cloud_names')


args = arg_parser.parse_args()
print(args)

id = args.id

clipped_ALS_point_cloud_names = json.loads(args.clipped_ALS_point_cloud_names)



def filter_non_ground_points(point_cloud_file_name):
    base_name, extension = point_cloud_file_name.split('.', 1)
    return base_name + "_non_ground_points." + extension

non_ground_ALS_point_cloud_filenames = []
for clipped_ALS_point_cloud_name in clipped_ALS_point_cloud_names:
    non_ground_ALS_point_cloud_filenames.append(filter_non_ground_points(clipped_ALS_point_cloud_name))

file_non_ground_ALS_point_cloud_filenames = open("/tmp/non_ground_ALS_point_cloud_filenames_" + id + ".json", "w")
file_non_ground_ALS_point_cloud_filenames.write(json.dumps(non_ground_ALS_point_cloud_filenames))
file_non_ground_ALS_point_cloud_filenames.close()
