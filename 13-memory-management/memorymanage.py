''' 
Concepts in Python Memory Management

Python handles memory automatically— you almost never say free this memory like in C/C++.  
But under the hood it uses two main systems working together:

- Reference counting— quick, main system  
- Garbage collector (GC)— cleans up when reference counting is not enough

Everything in Python is an object(even numbers, strings, functions).  
Every object has:
- data
- type
- reference count(how many variables point to it)
'''
### 2. Memory Allocation and Deallocation
# When you write:
a = [1, 2, 3]

'''Python:
1. Allocates memory for the list object
2. Allocates memory for each integer object (1, 2, 3)
3. Sets reference count = 1 for the list
4. Sets reference count = 2 for each number (because list points to them + the variable a)
'''

# When you do:
a = None

'''
- reference count of list drops to 0- memory freed immediately
- reference count of 1,2,3 drops to 1- still alive (small integers are cached anyway)
Deallocation happens automatically when reference count reaches 0 (for most objects).
'''
### 3. Reference Counting (the main hero)
# Python counts how many names/variables point to an object.
x = "hello"
y = x           # ref count of "hello" becomes 2
z = x           # now 3

del x           # ref count → 2
del y           # ref count → 1
del z           # ref count → 0 → string is deleted


# You can see it live:
import sys
a = []
print(sys.getrefcount(a))   # usually 2 (function call adds 1 temporarily)
b = a
print(sys.getrefcount(a))   # 3
## Important: small integers (-5 to 256) and some strings are **interned** — they never die, refcount can look weird.

### 4. Garbage Collection (the backup cleaner)
# Reference counting fails in **circular references**:
a = []
b = []
a.append(b)
b.append(a)

# now a points to b, b points to a → refcount never reaches 0
del a
del b
# objects are still alive → memory leak!


# Garbage collector finds and cleans these cycles.
# It runs automatically in background, or you can force it:

import gc
gc.collect()   # run garbage collection now


### 5. The gc module (what you can control)
import gc

print(gc.isenabled())       # True by default

gc.disable()                # turn off automatic GC (rarely do this)
gc.enable()

print(gc.get_count())       # how many objects in each generation

gc.collect()                # force clean now


'''Generations:
- Gen 0: short-lived objects (fast)
- Gen 1: medium
- Gen 2: long-lived (slow)'''

### 6. Memory Management Best Practices (real tips)
'''
- Use 'del' when you know a big object is not needed anymore
'''

big_list = [i for i in range(1000000)]
# ... use it ...
del big_list   # free memory now

'''
- Avoid global variables holding big data
- Use generators instead of huge lists when looping

'''
# bad – eats memory
for x in [i**2 for i in range(1000000)]:
    pass

# good – memory friendly
for x in (i**2 for i in range(1000000)):
    pass
'''
- Watch out for circular references in custom classes
- Use 'weakref' module if you really need weak references
- For very large data- use numpy/pandas (they manage memory better)
- Profile memory: use 'memory_profiler or objgraph'
'''
### Quick test you can run now
import sys
import gc

a = []
b = []
a.append(b)
b.append(a)

print("before del:", sys.getrefcount(a))  # 2
del a
del b
gc.collect()
print("after gc.collect()- should be gone")
