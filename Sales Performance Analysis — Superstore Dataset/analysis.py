import pandas as pd

df = pd.read_csv("SalesPerformance_Cleaned.csv", encoding='ISO-8859-1')

df.head()
df.info()

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = df['Order ID'].nunique()
avg_profit_margin = round((df['Profit'].sum() / df['Sales'].sum()) * 100, 2)

print("📈 Total Sales:", round(total_sales, 2))
print("💰 Total Profit:", round(total_profit, 2))
print("🧾 Total Orders:", total_orders)
print("📊 Average Profit Margin (%):", avg_profit_margin)

region_summary = df.groupby('Region')[['Sales', 'Profit']].sum().sort_values(by='Sales', ascending=False)
region_summary['Profit Margin (%)'] = (region_summary['Profit'] / region_summary['Sales'] * 100).round(2)
region_summary

category_summary = df.groupby('Category')[['Sales', 'Profit']].sum().sort_values(by='Sales', ascending=False)
category_summary['Profit Margin (%)'] = (category_summary['Profit'] / category_summary['Sales'] * 100).round(2)
category_summary

subcategory_summary = df.groupby('Sub-Category')[['Sales', 'Profit']].sum().sort_values(by='Sales', ascending=False).head(10)
subcategory_summary

top_customers = df.groupby('Customer Name')[['Sales', 'Profit']].sum().sort_values(by='Sales', ascending=False).head(10)
top_customers

monthly_sales = df.groupby(['Order Year', 'Order Month'])['Sales'].sum().reset_index()
monthly_sales.sort_values(['Order Year'], inplace=True)
monthly_sales.head(12)

discount_impact = df.groupby('Discount')[['Sales', 'Profit']].mean().reset_index()
discount_impact.head(10)

region_summary.to_csv("Region_Summary.csv")
category_summary.to_csv("Category_Summary.csv")
monthly_sales.to_csv("Monthly_Sales.csv")
