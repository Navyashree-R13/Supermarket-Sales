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

# Show the plot.
plt.show()


plt.figure(figsize=(10, 6))
sns.boxplot(x='Category', y='Profit', data=df)

# Set plot labels
plt.xlabel('Category')
plt.ylabel('Profit')
plt.title('Box Plot for Profit by Category')

# Show the plot
plt.show()


# visualize Profit column
sns.boxplot(data=df,y='Profit')
plt.title('Box Plot for Profit')
plt.show()


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