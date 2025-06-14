import os
import laspy

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--raw_laz_files', action='store', type=str, required=True, dest='raw_laz_files')

arg_parser.add_argument('--param_laz_compression_factor', action='store', type=str, required=True, dest='param_laz_compression_factor')
arg_parser.add_argument('--param_max_filesize_mb', action='store', type=str, required=True, dest='param_max_filesize_mb')

args = arg_parser.parse_args()
print(args)

id = args.id

raw_laz_files = json.loads(args.raw_laz_files)

param_laz_compression_factor = args.param_laz_compression_factor.replace('"','')
param_max_filesize_mb = args.param_max_filesize_mb.replace('"','')

conf_local_path_split = conf_local_path_split = os.path.join('/tmp/data', 'split')

def save_chunk_to_laz_file(
        in_filename,
        out_filename,
        offset,
        n_points
        ):
    """ Read points from a LAS/LAZ file and write them to a new file. """
    with laspy.open(in_filename) as in_file:
        with laspy.open(
                out_filename,
                mode="w",
                header=in_file.header
                ) as out_file:
            in_file.seek(offset)
            points = in_file.read_points(n_points)
            out_file.write_points(points)
    return out_filename


def split_strategy(filename, max_filesize, dest_dir=None):
    """ Set up splitting strategy for a LAS/LAZ file. """
    with laspy.open(filename) as f:
        bytes_per_point = (
                f.header.point_format.num_standard_bytes +
                f.header.point_format.num_extra_bytes
        )
        n_points = f.header.point_count
    n_points_target = int(
        max_filesize * int(param_laz_compression_factor) / bytes_per_point
        )
    stem, ext = os.path.splitext(filename)
    if dest_dir is not None:
        stem = os.path.join(dest_dir, os.path.basename(stem))
    return [
        (filename, f"{stem}-{n}{ext}", offset, n_points_target)
        for n, offset in enumerate(range(0, n_points, n_points_target))
        ]


os.makedirs(conf_local_path_split, exist_ok=True)
split_laz_files = []

for raw_file in raw_laz_files:
    inps = split_strategy(
        raw_file,
        int(param_max_filesize_mb) * 2 ** 20,
        dest_dir=conf_local_path_split,
        )
    print(f'Splitting {raw_file} into {len(inps)} files:')
    for inp in inps:
        split_file = inp[1]
        if not os.path.isfile(split_file):
            print(f'  writing {split_file}')
            save_chunk_to_laz_file(*inp)
        else:
            print(f' skipping {split_file} because it already exists')
        split_laz_files.append(split_file)

print(split_laz_files)

file_split_laz_files = open("/tmp/split_laz_files_" + id + ".json", "w")
file_split_laz_files.write(json.dumps(split_laz_files))
file_split_laz_files.close()
