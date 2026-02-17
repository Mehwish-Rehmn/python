"""what is numpy? (very easy)

numpy = “numerical python”  
it's a library that lets you work with big lists of numbers super fast and easy.

normal python list:
- slow for math on 1 million numbers
- no built-in math like matrix multiplication

numpy array:
- very fast (written in c language underneath)
- does math on whole list at once (no loops needed)
- has tons of ready-made functions for science, data, ml
"""
# you install it once:
# pip install numpy


#import:
import numpy as np  

### 2–3 simplest examples (copy-paste and run)

##example 1 – basic array + fast addition
import numpy as np

# normal python list (slow for big work)
a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]

# numpy array (fast)
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 30, 40, 50])

print(x + y)          
print(x * 2)          

## example 2 – create arrays easily (very useful)

import numpy as np

# zeros, ones, range, random
print(np.zeros(5))           # [0. 0. 0. 0. 0.]
print(np.ones((3, 2)))      # 3 rows, 2 columns full of 1
print(np.arange(0, 10, 2))  # [0 2 4 6 8] like range()
print(np.random.rand(4))    # 4 random numbers between 0 and 1

## example 3 – shape, reshape, mean, sum (data people use daily)**

import numpy as np

data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

print(data.shape)      # (9,)   ← 9 elements
print(data.mean())     # 50.0   ← average
print(data.sum())      # 450    ← total

# reshape into 3 rows × 3 columns
matrix = data.reshape(3, 3)
print(matrix)
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]

print(matrix[1, 2])    # 60   ← row 1, column 2

'''5 most important concepts (keep these in mind)
- array — main thing in numpy. like super-fast list but all elements same type (mostly numbers).
- vectorized operations — no need for loops
x + y, x * 5, x > 10 — works on whole array instantly
- shape & reshape — array has shape like (rows, columns)
reshape() changes shape without changing data
- slicing & indexing — same as list but more powerful
arr[2:5], arr[:, 1] (all rows, column 1)
- common functions
np.array() → make array
np.zeros(), np.ones(), np.arange(), np.linspace()
np.sum(), np.mean(), np.max(), np.min()
np.dot(), np.matmul() for matrix multiplication
'''