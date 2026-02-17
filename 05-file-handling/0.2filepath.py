import os
print("Current working directory:", os.getcwd())

r''' FILE PATH
A file path is the "address" that tells Python exactly where your file is on your computer.

There are two main types:
1. Absolute path(full address from the root)  
- Windows example:`C:\Users\Mehwish\Documents\project\notes.txt`  
- macOS/Linux example:`/home/mehwish/projects/notes.txt` or `/Users/Mehwish/Desktop/notes.txt`

2. Relative path(relative to where your Python script is running)  
- `notes.txt`: same folder as your script  
- `data/notes.txt`: inside a folder called `data`  
- `../old/notes.txt`: one folder up, then inside `old`  
- `./logs/error.log`: current folder → logs folder

'''
## Common ways to work with paths in Python
# 1. Basic open() with relative path

# file is in the same folder as your script
with open("notes.txt", "r") as f:
    print(f.read())

# file is inside a folder called data
with open("data/scores.csv", "r") as f:
    print(f.read())

# file is one folder up
with open("../backup/old_data.txt", "w") as f:
    f.write("saved backup")

# 2. Use os.path to make paths safe & cross-platform
# note: Windows uses `\` and macOS/Linux use `/` — this causes problems when you share code.

# Solution: use `os.path.join()`
import os
# works on Windows, macOS, Linux
folder = "data"
filename = "users.txt"
full_path = os.path.join(folder, filename)
print(full_path)          
with open(full_path, "w") as f:
    f.write("user list")

# 3. Get current working directory (where your script is running)
import os
print(os.getcwd())          # shows full current folder path

# 4. Check if file or folder exists
import os
file_path = "notes.txt"
if os.path.exists(file_path):
    print("file exists!")
else:
    print("file not found")

if os.path.isfile(file_path):
    print("this is a file")

if os.path.isdir("data"):
    print("data is a folder")

# 5. Get filename, extension, folder name
import os
path = "reports/sales/2025/january_report.xlsx"
print(os.path.basename(path))       # january_report.xlsx
print(os.path.dirname(path))        # reports/sales/2025
print(os.path.splitext(path))       # ('reports/sales/2025/january_report', '.xlsx')

# 6. use pathlib
from pathlib import Path
# create path object
p = Path("data") / "users" / "profile.txt"
if not p.exists():
    print("File not found. Creating folder and file...\n")
    # create folder if missing
    p.parent.mkdir(parents=True, exist_ok=True)
    # create file with default content
    p.write_text("This is a new profile file.\nWelcome Mehwish!\n")

# Now read and print
print("Reading file content:\n")
print(p.read_text(), end="")

# create folders if needed
new_folder = Path("output/results")
new_folder.mkdir(parents=True, exist_ok=True)
# write file
(new_folder / "result.txt").write_text("done!")

r''' rules for beginners 

- Prefer **relative paths** when possible  
- Always use `os.path.join()` or `Path()/' instead of hardcoding `\` or `/`  
- Use `with open(...)` — never forget to close  
- Check `os.path.exists()` before reading if you're not sure  
- Use `pathlib` if you're on Python 3.6+ — it's cleaner and more modern
'''
