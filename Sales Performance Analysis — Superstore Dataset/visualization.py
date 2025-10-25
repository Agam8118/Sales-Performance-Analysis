import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn as sns

df = pd.read_csv("SalesPerformance_Cleaned.csv")

plt.figure(figsize=(12,6))
df['State'].value_counts().head(10).plot(kind='bar', color='skyblue')
plt.title('Top 10 States with Most Sales')
plt.xlabel('State')
plt.ylabel('Number of Sales')
plt.show()

plt.figure(figsize=(10,6))
sns.barplot(x='Sub-Category', y='Sales', data=df, estimator=sum, order=df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False).index)
plt.xticks(rotation=45)
plt.title("Sales by Sub-Category")
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(x='Discount', y='Profit', data=df)
plt.title("Impact of Discount on Profit")
plt.show()


monthly_trend = df.groupby('Order Month')[['Sales','Profit']].sum().reindex(
    ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
)
monthly_trend.plot(kind='line', figsize=(10,5), title="Monthly Sales & Profit Trend")
plt.ylabel("Amount ($)")
plt.show()

yearly_trend = df.groupby('Order Year')[['Sales','Profit']].sum()
yearly_trend.plot(kind='bar', title="Yearly Sales & Profit Growth")
plt.show()

df['Delivery Days'] = (df['Ship Date'] - df['Order Date']).dt.days
print(df['Delivery Days'].describe())
sns.boxplot(x='Ship Mode', y='Delivery Days', data=df)
plt.title("Delivery Time by Shipping Mode")
plt.show()


top_products = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)
bottom_products = df.groupby('Product Name')['Profit'].sum().sort_values().head(10)

print("Top Profitable Products:\n", top_products)
print("\nLeast Profitable Products:\n", bottom_products)


