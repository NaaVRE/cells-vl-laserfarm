
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--parameter_shapefiles_of_plot_locations', action='store', type=str, required=True, dest='parameter_shapefiles_of_plot_locations')


args = arg_parser.parse_args()
print(args)

id = args.id

parameter_shapefiles_of_plot_locations = json.loads(args.parameter_shapefiles_of_plot_locations)



"""
Determines which airborne laser scanning (ALS) tile is need for each plot location
"""
def Get_laz_file_mapping(shapefile_names):
    """
    A placeholder method which should return a ALS point cloud tile filenames that cover the geographical area of the plot locations 
    """
    dummy_set_of_las_files = ["AHN4_C_154000_465000.COPC.LAZ", "AHN4_C_175000_448000.COPC.LAZ"]
    shapefile_las_tile_mapping = []
    for index, shapefile_name in enumerate(shapefile_names):
        mapping = {
            "shapefile_name": shapefile_name, 
            "las_tile_name": dummy_set_of_las_files[index%len(dummy_set_of_las_files)]
        }
        shapefile_las_tile_mapping.append(mapping)
    return shapefile_las_tile_mapping
        
shapefile_laz_tile_mappings = Get_laz_file_mapping(parameter_shapefiles_of_plot_locations)
las_data_filenames = set([mapping["las_tile_name"] for mapping in shapefile_laz_tile_mappings])

file_shapefile_laz_tile_mappings = open("/tmp/shapefile_laz_tile_mappings_" + id + ".json", "w")
file_shapefile_laz_tile_mappings.write(json.dumps(shapefile_laz_tile_mappings))
file_shapefile_laz_tile_mappings.close()
