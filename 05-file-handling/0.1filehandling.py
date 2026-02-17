''' File Handling 

File handling in Python is the process of working with files on your computer- it means:
- Creating new files  
- Opening existing files  
- Reading data from files  
- Writing new data into files  
- Adding more text to files  
- Closing files safely  

Why need?

Real programs almost always need to:
- Save something (game score, shopping list, user settings, notes)  
- Read something back later (load previous data, show old messages, read config)  
- Log what happened (errors, user actions)  
- Work with data files (excel-like, csv reports, configuration files)

Without file handling, everything you do in Python stays only in memory and disappears when program ends.
'''

### Basic steps (the pattern you will use 90% of the time)
'''
1. Open the file
2. Do something (read or write)
3. Close the file
But modern way- we almost always use `with` statement  
- it automatically closes the file even if something crashes
'''

## 1. Writing to a file (creating or overwriting)
# create a new file (or overwrite if already exists)
with open("notes.txt", "w") as file:
    file.write("hello this is my first note\n")
    file.write("i am learning python\n")
    file.write("today is day 15\n")

'''
What happens:
- file named `notes.txt` is created in same folder
- `"w"` = write mode (erases old content if file already exists)
- `\n` = new line (very important!)
'''

### 2. Adding more text without deleting old content (append mode)
with open("notes.txt", "a") as file:
    file.write("new line added later\n")
    file.write("feeling good today\n")
#"a" = append mode- adds at the end

### 3. Reading the whole file at once
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
# "r"= read mode (default, so you can even write just `"notes.txt"`)

### 4. Reading line by line (very common & memory friendly)
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())     
# strip() removes \n from end

### 5. Read all lines into a list
with open("notes.txt", "r") as file:
    lines = file.readlines()
    print(lines)           


### 6. Quick one-liner examples people use a lot

# write one line
open("log.txt", "a").write("user logged in at 10:30\n")

# read whole file in one line
content = open("data.txt").read()


# (but better to use `with` in real code)

### 7. Real mini-project style example

# save user todo list
tasks = ["buy milk", "call mom", "finish python day 15"]
with open("todo.txt", "w") as f:
    for task in tasks:
        f.write(task + "\n")
print("todo list saved!")

# now read it back
print("\nmy todo list:")
with open("todo.txt") as f:
    for line in f:
        print("- " + line.strip())

''' 
8. Important modes summary (remember these 4)
mode | meaning                        | what happens if file doesn't exist  | overwrites? |
-----|--------------------------------|-------------------------------------|-------------|
"r"  | read                           | error                               | no          |
"w"  | write                          | creates new file                    | yes         |
"a"  | append (add at end)            | creates new file                    | no          |
"r+" | read + write (advanced)        | error                               | no          |
'''

### 9. Common mistakes beginners make (watch out)
# wrong: forgot to close → file may get corrupted
file = open("test.txt", "w")
file.write("hi")
# forgot file.close()

# better: always use with
with open("test.txt", "w") as f:
    f.write("hi")   
# auto closes

''' wrong: reading in write mode
with open("data.txt", "w") as f:
    print(f.read())   
#error!'''


### 10. One very useful pattern (save & load simple data)
# save
scores = {"math": 85, "science": 92}
with open("scores.txt", "w") as f:
    for subject, mark in scores.items():
        f.write(f"{subject}:{mark}\n")

# load back
scores = {}
with open("scores.txt") as f:
    for line in f:
        subject, mark = line.strip().split(":")
        scores[subject] = int(mark)
print(scores)   
