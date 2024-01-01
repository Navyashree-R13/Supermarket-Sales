# Checking if there are any missing values in the entire DataFrame
any_missing_values = df.isnull().any().any()

# Printing the number of missing values in each column of the DataFrame.
print("Missing values in the entire DataFrame:")
print(any_missing_values)

# Check for duplicate rows in the entire DataFrame
duplicate_rows = df.duplicated()

# Check for duplicate rows based on specific columns, e.g., ['Year', 'Region', 'Sales']
duplicate_subset = df.duplicated(subset=['Order Date', 'Region', 'Sales'])

# Print the results
print("Duplicate rows in the entire DataFrame:")
print(duplicate_rows)

print("\nDuplicate rows based on ['Order Date', 'Region', 'Sales']:")
print(duplicate_subset)