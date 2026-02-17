#!/usr/bin/env python
# coding: utf-8

# ## CONDITIONAL STATEMENTS
# 

# Conditional statements let your program make decisions and run different code depending on whether something is True or False.
# - In simple words:
# - "If this is true → do this.
# - Otherwise → do that."

# if
# → Run code only if condition is True

# In[1]:


age = 20
if age >= 18:
    print("You can vote")    


# if + else
# → Do one thing if True, something else if False

# In[2]:


temperature = 15
if temperature > 25:
    print("It's hot!")
else:
    print("It's cool")       


# if + elif + else
# → Check multiple conditions in orderPython

# In[3]:


marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")         # Checks only if previous was False
elif marks >= 70:
    print("Grade C")
else:
    print("Grade D or Fail")


# One-liner if (short & simple)

# In[4]:


age = 17
status = "Adult" if age >= 18 else "Minor"
print(status)          # Minor


# Nested if (if inside if)

# In[7]:


## Nested Condiitonal Statements
# You can place one or more if, elif, or else statements inside another if, elif, or else statement to create nested conditional statements.
## number even ,odd,negative

num=int(input("Enter the number"))

if num>0:
    print("The number is positive")
    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")

else:
    print("The number is zero or negative")


# In[8]:


## Examples
## Determine if a year is a leap year using nested condition statement

year=int(input("Enter the year"))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
    else:
        print(year,"is a leap year")

else:
    print(year,"is not a leap year")


# In[5]:


age = 20
has_license = True

if age >= 18:
    if has_license:
        print("Can drive")
    else:
        print("Adult but no license")
else:
    print("Too young to drive")


# In[10]:


username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "password123":
        print("Login successful!")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")

