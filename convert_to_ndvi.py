import numpy as np
import rasterio
import argparse


def convert_to_ndvi(b4, b8, out):
    b4 = rasterio.open(b4)
    b8 = rasterio.open(b8)
    red = b4.read()
    nir = b8.read()
    ndvi = (nir.astype(np.float32) - red.astype(np.float32)) / (nir + red)
    profile = b4.meta
    profile.update(driver='GTiff')
    profile.update(dtype=rasterio.float32)
    rasterio.open(out, 'w', **profile).write(ndvi.astype(rasterio.float32))
    print("Converted to " + out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-b4", required=True, help="Path to b4 band")
    ap.add_argument("-b8", required=True, help="Path to b8 band")
    ap.add_argument("-out", required=True, help="Path to output file to be created")
    args = ap.parse_args()
    convert_to_ndvi(args.b4, args.b8, args.out)
