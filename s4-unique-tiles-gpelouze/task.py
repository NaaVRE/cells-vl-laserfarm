
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



unique_tiles = list(set(tiles))

print(unique_tiles)

file_unique_tiles = open("/tmp/unique_tiles_" + id + ".json", "w")
file_unique_tiles.write(json.dumps(unique_tiles))
file_unique_tiles.close()
