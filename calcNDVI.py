import numpy as np, rasterio
import cv2
import matplotlib as plt
from rasterio.plot import show

outfile = r'/Users/Alex/Downloads/ndvi1.tif'
#url to the bands
b4 = '/Users/Alex/Downloads/T35MRU_20190915T080611_B04.jp2'
b8 = '/Users/Alex/Downloads/T35MRU_20190915T080611_B08.jp2'

#open the bands (I can't believe how easy is this with rasterio!)
with rasterio.open(b4) as red:
    RED = red.read()
with rasterio.open(b8) as nir:
    NIR = nir.read()

#compute the ndvi
ndvi = (NIR.astype(np.float64) - RED.astype(np.float64)) / (NIR+RED)
print(ndvi.min(), ndvi.max())

profile = red.meta
profile.update(photometric='CMYK')
profile.update(driver='GTiff')
profile.update(dtype=rasterio.float32)

with rasterio.open(outfile, 'w', **profile) as dst:
    dst.write(ndvi.astype(rasterio.float32))
    print(dst.crs)

#heatmap (needs matplotlib)
#img = cv2.imread("ndvi22.tif",-1)
#data = np.asarray(img)
#fig, ax = plt.subplots(figsize=(8,8))
#show(data, cmap='RdYlGn', ax=ax alpha=0.9)

