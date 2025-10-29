
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--non_ground_ALS_point_cloud_filenames', action='store', type=str, required=True, dest='non_ground_ALS_point_cloud_filenames')


args = arg_parser.parse_args()
print(args)

id = args.id

non_ground_ALS_point_cloud_filenames = json.loads(args.non_ground_ALS_point_cloud_filenames)



"""
What happens on the edge of the grid / plot? I am assuming there will be point clouds that contain partial trees?
"""
class Tree_point:
    def __init__(self, geolocation_point, tree_id):
        self.tree_id = tree_id
        self.geolocation_point = geolocation_point

def assign_points_to_trees(non_ground_ALS_point_cloud_filenames):
    for ALS_point_cloud_filename in non_ground_ALS_point_cloud_filenames:
        print(f"{ALS_point_cloud_filename=}")
    return 

assign_points_to_trees(non_ground_ALS_point_cloud_filenames)

