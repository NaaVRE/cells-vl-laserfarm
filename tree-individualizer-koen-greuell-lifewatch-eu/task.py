
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--non_ground_ALS_point_cloud_filenames', action='store', type=str, required=True, dest='non_ground_ALS_point_cloud_filenames')

arg_parser.add_argument('--parameter_1_tree_individualisation', action='store', type=str, required=True, dest='parameter_1_tree_individualisation')

arg_parser.add_argument('--parameter_2_tree_individualisation', action='store', type=str, required=True, dest='parameter_2_tree_individualisation')

arg_parser.add_argument('--parameter_3_tree_individualisation', action='store', type=str, required=True, dest='parameter_3_tree_individualisation')

arg_parser.add_argument('--parameter_4_tree_individualisation', action='store', type=str, required=True, dest='parameter_4_tree_individualisation')

arg_parser.add_argument('--parameter_5_tree_individualisation', action='store', type=str, required=True, dest='parameter_5_tree_individualisation')


args = arg_parser.parse_args()
print(args)

id = args.id

non_ground_ALS_point_cloud_filenames = json.loads(args.non_ground_ALS_point_cloud_filenames)
parameter_1_tree_individualisation = args.parameter_1_tree_individualisation.replace('"','')
parameter_2_tree_individualisation = args.parameter_2_tree_individualisation.replace('"','')
parameter_3_tree_individualisation = args.parameter_3_tree_individualisation.replace('"','')
parameter_4_tree_individualisation = args.parameter_4_tree_individualisation.replace('"','')
parameter_5_tree_individualisation = args.parameter_5_tree_individualisation.replace('"','')



"""
What happens on the edge of the grid / plot? I am assuming there will be point clouds that contain partial trees?
"""
class Tree_point:
    def __init__(self, geolocation_point, tree_id):
        self.tree_id = tree_id
        self.geolocation_point = geolocation_point

def assign_points_to_trees(non_ground_ALS_point_cloud_filenames):
    print(f"{parameter_1_tree_individualisation=}")
    print(f"{parameter_2_tree_individualisation=}")
    print(f"{parameter_3_tree_individualisation=}")
    print(f"{parameter_4_tree_individualisation=}")
    print(f"{parameter_5_tree_individualisation=}")
    for ALS_point_cloud_filename in non_ground_ALS_point_cloud_filenames:
        print(f"{ALS_point_cloud_filename=}")
    return 

print(f"individualizing trees for the files: {non_ground_ALS_point_cloud_filenames}")
assign_points_to_trees(non_ground_ALS_point_cloud_filenames)

