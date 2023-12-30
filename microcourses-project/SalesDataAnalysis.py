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


