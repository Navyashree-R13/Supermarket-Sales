# Importing the Pandas library and assigning it the alias 'pd' for convenient reference
import pandas as pd

# Importing the pyplot module from the matplotlib library for data visualization
import matplotlib.pyplot as plt

# Reading a CSV file and creating a DataFrame using Pandas
df = pd.read_csv(r"Desktop\Retail_Sales.csv")

# Get the column names of the DataFrame
column_names = df.columns

# Print the column names
print(column_names)

# Get the number of rows in the DataFrame
num_rows = df.shape[0]

# Print the number of rows
print(num_rows)

# Display the first few rows of the DataFrame for a quick overview
print(df.head())

# Display a concise summary of the DataFrame, including data types and memory usage
df.info()

# Iterating through columns and their data types in the DataFrame and printing the results
for column, dtype in df.dtypes.items():
    print(f"{column}: {dtype}")

# Converting the 'Order Date' column to datetime format using pandas to_datetime function
df['Order Date'] = pd.to_datetime(df['Order Date'])

"""Iterating through columns and their data types in the DataFrame and printing the results to check
if the conversion of the 'Order Date' column to datetime format is successful"""
for column, dtype in df.dtypes.items():
    print(f"{column}: {dtype}")

# Checking if there are any missing values in the entire DataFrame
any_missing_values = df.isnull().any().any()

# Printing the number of missing values in each column of the DataFrame
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

# Understanding Sales Data

# Obtaining the unique values in the 'Region' column of the DataFrame
df['Region'].unique()

# Importing the NumPy library as np for numerical operations and array manipulations
import numpy as np

df['Year'] = df['Order Date'].dt.year  # Extract the year from 'Order Date'

# Group by year and calculate the sum of sales
yearly_sales = df.groupby('Year')['Sales'].sum()

# Plotting a pie chart
plt.figure(figsize=(6, 6))
plt.pie(yearly_sales, labels=yearly_sales.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Distribution of Sales by Year')
plt.show()

sales_by_region = df.groupby('Region')['Sales'].sum().to_dict()
# Print the sales in each region
print("Total Sales by Region:")
print(sales_by_region)

# Importing Plotly Express for easy and quick plotting
import plotly.express as px
# Importing Plotly IO for configuring plot settings
import plotly.io as pio

# Configuring the default template for a dark-themed plot
pio.templates.default = "plotly_dark"
# Creating a histogram using Plotly Express
# Plotting sales by region with unique colors for each region
fig = px.histogram(df, x = "Region", y = "Sales", color="Region", title = "Sales by the Regions", width=600, height=500)
# Displaying the plot
fig.show()

sales_by_category = df.groupby('Category')['Sales'].sum().reset_index()

# Sort the data by sales in descending order
sales_by_category = sales_by_category.sort_values(by='Sales', ascending=False)

# Create a bar chart
fig = px.bar(sales_by_category, x='Category', y='Sales', title='Sales by Category',
             labels={'Sales': 'Total Sales', 'Category': 'Product Category'},
             hover_data={'Sales': ':,.2f'}, #display data on hovering
             color='Category',  # Color bars by category
             color_discrete_sequence=px.colors.qualitative.Set2, width=600, height=500)  # Use Set2 color scale

# Styling
fig.update_layout(
    plot_bgcolor='black',  # Set the background color to Black
    paper_bgcolor='Black',  # Set the paper color to Black
)

# Show the figure
fig.show()

df['Original Price'] = df['Sales'] / (1 - (df['Discount'] / 100))

# Display the DataFrame with the new 'Original Price' column
print(df[['Sales', 'Discount', 'Original Price']])

# Add 'Original Price' to the list of columns
columns_list = ['Sales', 'Discount', 'Original Price']

columns_list = df.columns.tolist()

# Print the list of columns
print(columns_list)

# Grouping the data by 'Sub-Category' and summing the 'Sales' for each sub-category
sales_per_subcategory = df.groupby('Sub Category')['Sales'].sum().reset_index()

# Creating a bar chart for sales per sub-category
fig = px.bar(sales_per_subcategory, x='Sub Category', y='Sales',
             title='Sales per Sub Category',
             labels={'Sales': 'Total Sales', 'Sub Category': 'Sub-Category'},
             width=600, height=500, color='Sales')
fig.show()

#Box Plot for Numerical Data

import seaborn as sns

# Assuming df is your DataFrame with numerical data
# You may want to exclude non-numerical columns using df.select_dtypes('number')

# Melt the DataFrame to create a long-form dataset
df_long = pd.melt(df, value_vars=['Sales', 'Discount', 'Profit'], var_name='Variable', value_name='Value')

# Create a box plot for each variable
sns.boxplot(x='Variable', y='Value', data=df_long)

# Set plot labels
plt.xlabel('Variable')
plt.ylabel('Value')
plt.title('Box Plot for Numerical Data')

# Show the plot
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='Category', y='Profit', data=df)

# Set plot labels
plt.xlabel('Category')
plt.ylabel('Profit')
plt.title('Box Plot for Profit by Category')

# Show the plot
plt.show()

#Box Plot for Profit

# visualize Profit column
sns.boxplot(data=df,y='Profit')
plt.title('Box Plot for Profit')
plt.show()


#Removing Outliers in the Box Plot

#To remove the outliers
# 75th percentile
seventy_fifth=df['Profit'].quantile(0.75)
# 25th percentile
twenty_fifth=df['Profit'].quantile(0.25)
#Interquartile range
profit_IQR=seventy_fifth-twenty_fifth
print(profit_IQR)

# Upper threshold
upper = seventy_fifth + (1.5 * profit_IQR)
# Lower threshold
lower = twenty_fifth - (1.5 * profit_IQR)
print(upper, lower)

sup1=df[(df['Profit']>lower) & (df['Profit'] <upper)]

# boxplot for profit after removing outliers
sns.boxplot(data=sup1,y='Profit')
plt.title('Box Plot for Profit Without Outliers')
plt.figure(figsize=(4,4))
plt.show()

#Histogram for Profit

# Creating a histogram for the 'Profit' column using seaborn
sns.histplot(df['Profit'])

# Adding a title to the histogram
plt.title('Histogram for Profit')

# Show the plot
plt.show()

#Indentifying the Top 5 and Last 3 Customers
# Group the DataFrame by customer name and aggregate the sales and profit values
super_group=sup1.groupby('Customer Name').agg({'Sales':'sum','Profit':'sum'})
# Compute a performance metric based on sales and profit
super_group['Performance']=super_group['Sales']+super_group['Profit']
# Sort the customers by their performance metric in descending order
super_group = super_group.sort_values(by='Performance', ascending=False)

# Print the names of the top 5 customers
print("The top 5 customers are:")
print(super_group.index[:5].tolist())
# Print the names of the last 3 customers
print("The last 3 customers are:")
print(super_group.tail(3).index.tolist())

