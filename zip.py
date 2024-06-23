import geopandas as gpd
import fiona

rawfile = "NYS_2022_Tax_Parcels_Public.gdb"
layer = 'NYS_Tax_Parcels_Public'

layers = fiona.listlayers(rawfile)

assert layer in layers


print('reading input file...',flush=True)
raw = gpd.read_file(rawfile,layer=layer,engine='pyogrio')
print('done',flush=True)

print('records:',len(raw))

oneida = raw[ raw['COUNTY_NAME']=='Oneida' ]

oneida.rename(columns={'PRINT_KEY': 'PIN'}, inplace=True)


oneida.to_file('oneida.gpkg',layer='parcels')

