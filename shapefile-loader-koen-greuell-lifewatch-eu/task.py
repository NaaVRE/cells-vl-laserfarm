
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_shapefiles_plot_locations', action='store', type=str, required=True, dest='param_shapefiles_plot_locations')

args = arg_parser.parse_args()
print(args)

id = args.id


print(args.param_shapefiles_plot_locations)
print(type(args.param_shapefiles_plot_locations))
try:
    param_shapefiles_plot_locations = json.loads(args.param_shapefiles_plot_locations)
except Exception as e:
    if e.__class__.__name__ == 'JSONDecodeError':
        import ast
        param_shapefiles_plot_locations = ast.literal_eval(args.param_shapefiles_plot_locations.replace('[','["').replace(',','","').replace('" ','"').replace(']','"]').replace("'",""))
    else:
        raise e


shapefiles_of_plot_locations = param_shapefiles_plot_locations

file_shapefiles_of_plot_locations = open("/tmp/shapefiles_of_plot_locations_" + id + ".json", "w")
file_shapefiles_of_plot_locations.write(json.dumps(shapefiles_of_plot_locations))
file_shapefiles_of_plot_locations.close()
