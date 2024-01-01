# Get the column names of the DataFrame
column_names = df.columns
# Print the column names
print(column_names)


# Get the number of rows in the DataFrame
num_rows = df.shape[0]
# Print the number of rows
print(num_rows)


# Display the first few rows of the DataFrame for quick overview
print(df.head())


# Display a concise summary of the DataFrame, including data types and memory usage
df.info()


# Iterating through columns and their data types in the DataFrame and printing the results
for column, dtype in df.dtypes.items():
    print(f"{column}: {dtype}")