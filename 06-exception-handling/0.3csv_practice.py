''' CSV file
csv = comma-separated values  
it's just a plain text file where data is stored like a table, but separated by commas (or sometimes other characters like ; or tab).
'''
# example of a simple 
filename= "students.csv"
students = [
["name","age","grade","city"],
["alex","20","A","delhi"],
["sara","22","B","mumbai"],
["riya","19","A","delhi"],
["karan","21","C","bangalore"]
]

'''
very common because:
- excel / google sheets save as csv
- many websites / apis give data in csv
- easy to read/write with code
'''
### two main ways to work with csv in python

#using built-in csv module** (simple, good for beginners)  
#using pandas** (very powerful, most people use this in real work)

## 1. using built-in csv module
# first import:
import csv
# write students list to CSV first
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)
# read a csv file (row by row)
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    
    # first row is header
    header = next(reader)
    print("columns:", header)
    
    # now read data rows
    for row in reader:
        print(row)               # ['alex', '20', 'A', 'delhi']

# or better — read as dictionary (very useful)
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        print(row["name"], "is", row["age"], "years old")
        # alex is 20 years old


## write to a csv file
data = [
    ["name", "age", "grade", "city"],
    ["neha", 23, "B", "chennai"],
    ["mohan", 19, "A", "kolkata"]
]
with open("new_students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# or using DictWriter (better when you have dicts)
students = [
    {"name": "priya", "age": 21, "grade": "A", "city": "hyderabad"},
    {"name": "rahul", "age": 20, "grade": "B", "city": "pune"}
]
with open("output.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age", "grade", "city"])
    writer.writeheader()               # writes the header row
    writer.writerows(students)


## 2. using pandas (the modern way- most recommended)
import pandas as pd
# read csv
df = pd.read_csv("students.csv")
print(df)

# easy things you can do
print(df["name"])                    # all names
print(df[df["age"] > 20])            # students older than 20
print(df["grade"].value_counts())    # count of each grade

# save back to csv
df.to_csv("updated_students.csv", index=False)

"""
pandas makes life 10x easier for:
filtering
sorting
calculating averages
handling missing values
merging files
huge files
"""
