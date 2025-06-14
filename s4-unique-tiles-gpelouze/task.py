
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--tiles', action='store', type=str, required=True, dest='tiles')


args = arg_parser.parse_args()
print(args)

id = args.id

tiles = json.loads(args.tiles)



tiles = list(set(tiles))

print(tiles)

