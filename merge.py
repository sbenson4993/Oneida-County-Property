import pandas as pd
import geopandas as gpd

# Load the DataFrame from the pickle file
buyout = pd.read_pickle("buyout.pkl")

# Load the GeoDataFrame from the GeoPackage
oneida = gpd.read_file("oneida.gpkg", layer="parcels")

# Ensure the 'PIN' column exists in both DataFrames
if 'PIN' not in buyout.columns:
    raise KeyError("'PIN' column not found in buyout DataFrame")
if 'PIN' not in oneida.columns:
    raise KeyError("'PIN' column not found in oneida GeoDataFrame")

# Clean 'PIN' columns to remove any leading/trailing spaces
buyout['PIN'] = buyout['PIN'].astype(str).str.strip()
oneida['PIN'] = oneida['PIN'].astype(str).str.strip()

# Perform the inner join
merged = oneida.merge(buyout, on='PIN', how='inner')

# Save the result to a new GeoPackage
output_path = 'merged.gpkg'
merged.to_file(output_path, driver='GPKG', layer='joined_layer')

# Display the first few rows of the merged GeoDataFrame
print("Merged GeoDataFrame:\n", merged.head())
