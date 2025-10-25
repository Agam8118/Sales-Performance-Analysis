import pandas as pd

df = pd.read_csv('Sample - Superstore.csv',encoding='ISO-8859-1')
print(df.head())

df.info()
df.describe()
df.isnull().sum()

df = df.drop_duplicates()
df = df.dropna()

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

df['Order Month'] = df['Order Date'].dt.strftime('%b')
df['Order Year'] = df['Order Date'].dt.year
df['Profit Margin (%)'] = round((df['Profit'] / df['Sales']) * 100, 2)

df[df['Discount'] > 0.6]
df[df['Profit'] < 0]

df.to_csv("SalesPerformance_Cleaned.csv", index=False)
df.sample(5)
df.shape
