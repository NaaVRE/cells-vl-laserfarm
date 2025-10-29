
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

args = arg_parser.parse_args()
print(args)

id = args.id


param_1_tree_individualisation = args.param_1_tree_individualisation.replace('"','')
param_2_tree_individualisation = args.param_2_tree_individualisation.replace('"','')
param_3_tree_individualisation = args.param_3_tree_individualisation.replace('"','')
param_4_tree_individualisation = args.param_4_tree_individualisation.replace('"','')
param_5_tree_individualisation = args.param_5_tree_individualisation.replace('"','')


parameter_1_tree_individualisation = param_1_tree_individualisation
parameter_2_tree_individualisation = param_2_tree_individualisation
parameter_3_tree_individualisation = param_3_tree_individualisation
parameter_4_tree_individualisation = param_4_tree_individualisation
parameter_5_tree_individualisation = param_5_tree_individualisation

file_parameter_1_tree_individualisation = open("/tmp/parameter_1_tree_individualisation_" + id + ".json", "w")
file_parameter_1_tree_individualisation.write(json.dumps(parameter_1_tree_individualisation))
file_parameter_1_tree_individualisation.close()
file_parameter_2_tree_individualisation = open("/tmp/parameter_2_tree_individualisation_" + id + ".json", "w")
file_parameter_2_tree_individualisation.write(json.dumps(parameter_2_tree_individualisation))
file_parameter_2_tree_individualisation.close()
file_parameter_3_tree_individualisation = open("/tmp/parameter_3_tree_individualisation_" + id + ".json", "w")
file_parameter_3_tree_individualisation.write(json.dumps(parameter_3_tree_individualisation))
file_parameter_3_tree_individualisation.close()
file_parameter_4_tree_individualisation = open("/tmp/parameter_4_tree_individualisation_" + id + ".json", "w")
file_parameter_4_tree_individualisation.write(json.dumps(parameter_4_tree_individualisation))
file_parameter_4_tree_individualisation.close()
file_parameter_5_tree_individualisation = open("/tmp/parameter_5_tree_individualisation_" + id + ".json", "w")
file_parameter_5_tree_individualisation.write(json.dumps(parameter_5_tree_individualisation))
file_parameter_5_tree_individualisation.close()
