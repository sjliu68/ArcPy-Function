##====================================
##Project Raster
##Usage: ProjectRaster_management in_raster out_raster out_coor_system {NEAREST | BILINEAR 
##                                | CUBIC | MAJORITY} {cell_size} {geographic_transform;
##                                geographic_transform...} {Registration_Point} {in_coor_system}
    
import arcpy
import glob

arcpy.env.workspace = r"Q:\france\sar_project"

fps = glob.glob(r'Q:\france\sar\*.tif')

##Reproject a TIFF image with Datumn transfer
count = 0
for fp in fps:
    print(fp)
    count+=1
    arcpy.ProjectRaster_management(fp, "sar"+str(count)+'.tif', r"Q:\france\subset\s2a_TCI_0525.tif",\
                               "BILINEAR", "10")
