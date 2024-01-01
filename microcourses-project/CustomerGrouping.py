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