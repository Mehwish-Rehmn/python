"""
data manipulation and analysis in pandas
pandas lets you take messy, boring data (from csv, excel, database, api…) and do whatever you want with it quickly.

data manipulation = changing the data so it looks the way you need
data analysis = asking questions from the data and finding answers (averages, groups, patterns, top values…)

pandas is basically your swiss army knife for tables in python.
you don't write 50 lines of loops anymore — most things are one line.

core things you do every day with pandas
1.load data
read csv/excel/json/sql/etc.
2.look at data
see first few rows, column names, types, missing values
3.clean data
remove junk, fill missing, fix wrong types, drop duplicates
4.select / filter
pick columns, rows that match condition
5.add / change columns
create new columns from old ones
6.group & summarize
average per city, count per category, total sales per month
7.sort & rank
top 10, bottom 5, sorted by score
8.join / merge
combine two tables like vlookup in excel
9.save results
back to csv/excel/json
"""

import pandas as pd

# 1. load your data
df = pd.read_csv("sales.csv")

# 2. quick look
print(df.head())           
print(df.info())           
print(df.describe())       

# 3. clean a bit
df = df.drop_duplicates()
df["date"] = pd.to_datetime(df["date"])
df["amount"] = df["quantity"] * df["price"]
df = df.dropna(subset=["amount"])

# 4. filter
delhi_sales = df[df["city"] == "delhi"]

# 5. add column
df["tax"] = df["amount"] * 0.18

# 6. group & summarize
sales_by_city = df.groupby("city")["amount"].sum()
top_products = df.groupby("product")["amount"].sum().sort_values(ascending=False).head(5)

# 7. save cleaned data
df.to_csv("clean_sales.csv", index=False)