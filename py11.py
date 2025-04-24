import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("Projectdata.csv")
'''
print("Basic Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())
'''
'''
category_sales = df.groupby('Category')['Sales'].sum()
category_sales.plot(kind='bar', color='skyblue', title='Total Sales by Category')
plt.ylabel('Sales')
plt.xlabel('Category')
plt.tight_layout()
plt.show()
'''
'''
corr = df[['Sales', 'Quantity', 'Profit']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()
'''
'''
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Month'] = df['Order Date'].dt.month
print(df[['Order Date', 'Month']].head())
'''
'''
top_products = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(5)
print("Top 5 Most Profitable Products:")
print(top_products)
'''


'''corr = df[['Sales', 'Quantity', 'Profit']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", ax=axs[0, 0])
axs[0, 0].set_title("Correlation Heatmap")
'''
'''category_sales = df.groupby('Category')['Sales'].sum()
axs[0, 1].pie(category_sales, labels=category_sales.index, autopct='%1.1f%%', startangle=140)
axs[0, 1].set_title("Sales Distribution by Category")'''

'''sns.countplot(data=df, y='Sub-Category', order=df['Sub-Category'].value_counts().index, ax=axs[1, 0], palette='viridis')
axs[1, 0].set_title("Count of Orders by Sub-Category")
'''
'''df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)

plt.figure(figsize=(8, 6))
corr = df[['Sales', 'Quantity', 'Profit']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()'''
'''
category_sales = df.groupby('Category')['Sales'].sum()

plt.figure(figsize=(6, 6))
plt.pie(category_sales, labels=category_sales.index, autopct='%1.1f%%', startangle=140)
plt.title("Sales Distribution by Category")
plt.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle.
plt.show()
'''
'''
category_sales = df.groupby('Category')['Sales'].sum()

plt.figure(figsize=(6, 6))
plt.pie(category_sales, labels=category_sales.index, autopct='%1.1f%%', startangle=140)
plt.title("Sales Distribution by Category")
plt.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle.
plt.show()
'''
plt.figure(figsize=(8, 6))
sns.violinplot(data=df, x='Category', y='Profit', palette='Set2')
plt.title("Profit Distribution by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.show()



