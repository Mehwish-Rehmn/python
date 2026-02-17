#!/usr/bin/env python
# coding: utf-8

# ## loops
# 

# A loop lets you repeat a block of code multiple times — automatically — instead of writing the same code again and again.
# - Python has two main loops beginners use:
# 
# for loop
# - Best when you know how many times to repeat (or when going through a list, range, string, etc.)
# 
# while loop
# - Best when you repeat until a condition becomes false (you don't always know the number of times)
# ## one-line memory
# - break    = break out(stop loop)
# - continue = continue to next round
# - pass     = pass/do nothing right now

# In[5]:


range(6)


# In[ ]:


# for loop
for i in range(5):
    print(i)


# In[7]:


for i in range(1,8):
    print(i)


# In[8]:


for i in range(1,6,2):
    print(i)


# In[9]:


for i in range(10,1,-2):
    print(i)


# In[ ]:


# strings
str="wish cobe"
for i in str:
    print(i)


# In[ ]:


# Repeat 5 times using range
for i in range(5):
    print("Hello world!")  
    


# In[ ]:


# Numbers 1 to 10
for num in range(1, 11):
    print(num)  


# In[ ]:


# Keep asking until correct password
password = ""

while password != "1234":
    password = input("Enter password: ")
    if password != "1234":
        print("Wrong! Try again.")

print("Correct! Welcome.")


# In[ ]:


# Count down
count = 5

while count > 0:
    print(count)
    count = count - 1   # or count -= 1

print("Blast off!")


# In[ ]:


# break- stops the nearest loop completely

for i in range(1, 5):          # outer loop
    print(i)
    for j in range(1, 6):      # inner loop
        print(j)
        if j == 3:
            break                  
    print("finished")


# In[ ]:


# continue– skips to next iteration of nearest loop
for i in range(3):
    for j in range(5):
        if j == 2:
            continue
        print(f"i{i} j{j}", end=" ")
    print()


# In[14]:


# pass- does nothing (placeholder)
for i in range(3):
    for j in range(5):
        if j == 2:
            pass          # ← nothing happens
        print(j, end=" ")
    print()


# In[15]:


# Nested loops a loop inside a loop

for i in range(3):
    for j in range(2):
        print(f"i:{i} and j:{j}")


# In[16]:


# Prime numbers between 1 and 100

for num in range(1,50):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)

