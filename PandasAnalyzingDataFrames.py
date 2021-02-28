# Pandas - Analyzing DataFrames
# Viewing the Data
import pandas as pd 
df = pd.read_csv('data.csv')

print(df.head(10)) # Get a quick overview by printing the first 10 rows of the DataFrame

# Print the first 5 rows of the DataFrame
import pandas as pd

df = pd.read_csv('data.csv')

print(df.head())

# Print the last 5 rows of the DataFrame
