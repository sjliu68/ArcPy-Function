##Clip Raster Dataset by known extent - Left Bottom Right Top

import arcpy
import glob


arcpy.env.workspace = r"Q:\france\sar_subset"
fps = glob.glob(r'Q:\france\sar_project\*.tif')


count=0
ls = [1,10,11,12,2,3,4,5,6,7,8,9]
for fp in fps:
    print(fp)
    arcpy.Clip_management(
        fp,"399960 5339000 470060 5400000",
        "sarsub"+str(ls[count])+'.tif', "#", "#", "NONE")
    count+=1
