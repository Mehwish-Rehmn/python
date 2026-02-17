"""
Exception
When your code runs into a problem it can't handle normally, Python "throws" an exception (error message) and stops.
Examples you see every day:
ZeroDivisionError: dividing by 0
FileNotFoundError: trying to open a file that doesn't exist
TypeError: "hello" + 5
IndexError: list[10] when list has only 5 items
KeyError: dictionary["age"] when key doesn't exist

Why do we need exception handling?
Without it: program crashes and stops completely
With it: program can:

catch the error
show nice message to user
continue running
log the problem
try something else
"""
### example 1- basic try/except (user input)
try:
    age = int(input("enter your age: "))
    print(f"you are {age} years old")
except ValueError:
    print("please enter a number, not letters or symbols")


### example 2- catch specific errors (division)
try:
    num = int(input("enter a number: "))
    result = 100 / num
    print("100 divided by your number is", result)
except ValueError:
    print("that's not a valid number")
except ZeroDivisionError:
    print("you can't divide by zero")


### example 3- catch anything + show the error message
try:
    a = 10
    b = "hello"
    print(a + b)           # this will crash
except Exception as e:
    print("something went wrong:", e)

### example 4- file reading with proper handling
try:
    with open("my_notes.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("file my_notes.txt not found in this folder")
except PermissionError:
    print("you don't have permission to read this file")

### example 5- else + finally (very common pattern)
try:
    number = int(input("enter a number to divide 50: "))
    answer = 50 / number
except ValueError:
    print("please type a number")
except ZeroDivisionError:
    print("can't divide by zero")
else:
    print("success! answer is", answer)
finally:
    print("this runs no matter what – cleanup done")


### example 6- raise your own error (validation)
def check_score(score):
    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")
    print("score is valid:", score)

try:
    check_score(150)
except ValueError as error:
    print("error:", error)

### example 7- real mini function (safe file append)
def log_message(message):
    try:
        with open("activity.log", "a") as log:
            log.write(message + "\n")
    except Exception as e:
        print("could not write to log:", e)

log_message("user started the program")
log_message("user clicked save")


### example 8- handling dictionary key errors
student = {"name": "alex", "age": 20}

try:
    print(student["grade"])
except KeyError:
    print("grade key not found – student has no grade yet")


### example 9- list index error
colors = ["red", "blue", "green"]

try:
    print(colors[5])
except IndexError:
    print("that index is out of range – list only has", len(colors), "items")


### example 10- multiple except PLUS general catch
try:
    num = int(input("enter number: "))
    result = 200 / num
    print(result)
    print(colors[10])         # will also crash
except ValueError:
    print("invalid input")
except ZeroDivisionError:
    print("zero division")
except Exception as ex:
    print("other error happened:", ex)

'''
Difference Between Specific Exception and Generic Exception

1. Specific Exception (e.g., ValueError, ZeroDivisionError)
Handles a particular type of error.
More precise and recommended in real projects.
Helps in better debugging.

2. Generic Exception (except Exception as e)
Catches all types of errors.
Used as a safety net.
Should be written after specific exception blocks.

'''