
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_1_tree_individualisation', action='store', type=str, required=True, dest='param_1_tree_individualisation')
arg_parser.add_argument('--param_2_tree_individualisation', action='store', type=str, required=True, dest='param_2_tree_individualisation')
arg_parser.add_argument('--param_3_tree_individualisation', action='store', type=str, required=True, dest='param_3_tree_individualisation')
arg_parser.add_argument('--param_4_tree_individualisation', action='store', type=str, required=True, dest='param_4_tree_individualisation')
arg_parser.add_argument('--param_5_tree_individualisation', action='store', type=str, required=True, dest='param_5_tree_individualisation')
arg_parser.add_argument('--param_shapefiles_of_plot_locations', action='store', type=str, required=True, dest='param_shapefiles_of_plot_locations')

args = arg_parser.parse_args()
print(args)

id = args.id


param_1_tree_individualisation = args.param_1_tree_individualisation.replace('"','')
param_2_tree_individualisation = args.param_2_tree_individualisation.replace('"','')
param_3_tree_individualisation = args.param_3_tree_individualisation.replace('"','')
param_4_tree_individualisation = args.param_4_tree_individualisation.replace('"','')
param_5_tree_individualisation = args.param_5_tree_individualisation.replace('"','')
print(args.param_shapefiles_of_plot_locations)
print(type(args.param_shapefiles_of_plot_locations))
try:
    param_shapefiles_of_plot_locations = json.loads(args.param_shapefiles_of_plot_locations)
except Exception as e:
    if e.__class__.__name__ == 'JSONDecodeError':
        import ast
        param_shapefiles_of_plot_locations = ast.literal_eval(args.param_shapefiles_of_plot_locations.replace('[','["').replace(',','","').replace('" ','"').replace(']','"]').replace("'",""))
    else:
        raise e


parameter_shapefiles_of_plot_locations = param_shapefiles_of_plot_locations
parameter_1_tree_individualisation = param_1_tree_individualisation
parameter_2_tree_individualisation = param_2_tree_individualisation
parameter_3_tree_individualisation = param_3_tree_individualisation
parameter_4_tree_individualisation = param_4_tree_individualisation
parameter_5_tree_individualisation = param_5_tree_individualisation

file_parameter_shapefiles_of_plot_locations = open("/tmp/parameter_shapefiles_of_plot_locations_" + id + ".json", "w")
file_parameter_shapefiles_of_plot_locations.write(json.dumps(parameter_shapefiles_of_plot_locations))
file_parameter_shapefiles_of_plot_locations.close()
