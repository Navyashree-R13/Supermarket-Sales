# Converting the 'Order Date' column to datetime format using pandas to_datetime function
df['Order Date'] = pd.to_datetime(df['Order Date'])

"""Iterating through columns and their data types in DataFrame and printing the results to check
if the conversion of the 'Order Date' column to datetime format is successful"""
for column, dtype in df.dtypes.items():
    print(f"{column}: {dtype}")