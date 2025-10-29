
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--shapefile_las_tile_mappings', action='store', type=str, required=True, dest='shapefile_las_tile_mappings')


args = arg_parser.parse_args()
print(args)

id = args.id

shapefile_las_tile_mappings = json.loads(args.shapefile_las_tile_mappings)



def clip(shapefile_las_tile_mappings):
    clipped_ALS_point_clouds = []
    for mapping in shapefile_las_tile_mappings:
        clipped_ALS_point_clouds.append(clip_point_cloud(mapping))
    return clipped_ALS_point_clouds

def clip_point_cloud(shapefile_las_tile_mapping):
    """
    Placeholder method that should clip point clouds
    """
    
    return shapefile_las_tile_mapping["las_tile_name"].replace(".shp", ".COPC.LAZ")

clipped_ALS_point_cloud_names = clip(shapefile_las_tile_mappings)

file_clipped_ALS_point_cloud_names = open("/tmp/clipped_ALS_point_cloud_names_" + id + ".json", "w")
file_clipped_ALS_point_cloud_names.write(json.dumps(clipped_ALS_point_cloud_names))
file_clipped_ALS_point_cloud_names.close()
