"""
definition of pandas
pandas is a free python library that makes it super easy to work with data in tables (like excel or csv files).
in simple words:
pandas = "excel on steroids" for python programmers
it lets you:
read csv/excel/json files quickly
clean messy data
filter rows
add/remove columns
calculate averages/sums
group data
join/merge tables
handle missing values

most data analysts, scientists, and ml engineers use pandas daily.
"""

#import pandas
import pandas as pd

#create dataframe from dict
data = {
    "name": ["alex", "sara", "riya"],
    "age": [20, 22, 19],
    "city": ["delhi", "mumbai", "pune"]
}
df = pd.DataFrame(data)
print(df)

#read csv file
df = pd.read_csv("students.csv")
print(df.head())
print(df["name"])

#filer row
df = pd.DataFrame({
    "name": ["alex", "sara", "riya", "karan"],
    "marks": [85, 92, 78, 65]
})
high_marks = df[df["marks"] > 80]
print(high_marks)

# add column
df["grade"] = df["marks"].apply(lambda x: "a" if x >= 90 else "b" if x >= 70 else "c")
print(df)

#group by and count
df["city"] = ["delhi", "mumbai", "delhi", "pune"]
print(df.groupby("city").size())

#sortvalues
df_sorted = df.sort_values("marks", ascending=False)
print(df_sorted)

# drop column
df = df.drop("grade", axis=1)
print(df)

#fill missing values
df = pd.DataFrame({
    "name": ["alex", "sara", "riya"],
    "age": [20, None, 19]
})
df["age"] = df["age"].fillna(0)
print(df)

#merge two dataFrames
df1 = pd.DataFrame({"id": [1, 2], "name": ["alex", "sara"]})
df2 = pd.DataFrame({"id": [1, 2], "marks": [85, 92]})
merged = pd.merge(df1, df2, on="id")
print(merged)

# save to csv
df.to_csv("output.csv", index=False)
