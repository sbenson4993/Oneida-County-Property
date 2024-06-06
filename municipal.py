import pandas as pd

# Read the CSV file into a DataFrame
buyout = pd.read_csv("whitesboro_flood_buyout.csv")
buyout.rename(columns={' full_market_value ': 'market_value'}, inplace=True)

# Ensure 'market_value' column is in numeric format by removing special characters and converting to float
buyout['market_value'] = buyout['market_value'].replace('[\$,]', '', regex=True).astype(float)

# Organize the values in the 'market_value' column into 5 bins
num_bins = 5
buyout['value_bins'] = pd.cut(buyout['market_value'], bins=num_bins, labels=[f' {i+1}' for i in range(num_bins)])
buyout['value_bins'] = buyout['value_bins'].astype(str)
# Display the updated DataFrame with the new 'value_bins' column
print("DataFrame with 'market_value' organized into 5 bins:\n")
print(buyout.head())

buyout.drop(columns=['OWNER_FULL', 'OWNER_LAST_NAME', 'PROP_CLASS'], inplace=True)

buyout.to_pickle("buyout.pkl")


