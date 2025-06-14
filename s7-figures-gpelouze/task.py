import rasterio
import os
import matplotlib.pyplot as plt
import rasterio.plot as rp

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--geo_tiff', action='store', type=str, required=True, dest='geo_tiff')

arg_parser.add_argument('--param_feature_name', action='store', type=str, required=True, dest='param_feature_name')

args = arg_parser.parse_args()
print(args)

id = args.id

geo_tiff = args.geo_tiff.replace('"','')

param_feature_name = args.param_feature_name.replace('"','')

conf_local_path_figures = conf_local_path_figures = os.path.join('/tmp/data', 'figures')

src = rasterio.open(geo_tiff)

os.makedirs(conf_local_path_figures, exist_ok=True)

ax = plt.gca()
rio_plot = rp.show((src, 1), interpolation='none', ax=ax)
img = rio_plot.get_images()[0]
cb = plt.colorbar(img, ax=ax)
cb.set_label(f'{param_feature_name}')
plt.xlabel('EPSG:28992 X [m]')
plt.ylabel('EPSG:28992 Y [m]')
plt.show()
map_filename = os.path.join(conf_local_path_figures, f'{param_feature_name}_map.pdf')
plt.savefig(map_filename)

rp.show_hist(
    src,
    bins=50,
    lw=0.0,
    stacked=False,
    alpha=0.3,
    histtype='stepfilled',
    title="Histogram",
    )
plt.show()
histogram_filename = os.path.join(conf_local_path_figures, f'{param_feature_name}_histogram.pdf')
plt.savefig(histogram_filename)

file_histogram_filename = open("/tmp/histogram_filename_" + id + ".json", "w")
file_histogram_filename.write(json.dumps(histogram_filename))
file_histogram_filename.close()
file_map_filename = open("/tmp/map_filename_" + id + ".json", "w")
file_map_filename.write(json.dumps(map_filename))
file_map_filename.close()
