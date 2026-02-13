"""
Importing in Python: Modules and Packages
MODULES:
module is just one python file (.py) that contains functions, classes, variables, or code you want to reuse.
"""
# 1. Import whole module
import math_utils

print("Whole module import:")
print(math_utils.add(5, 3))
print(math_utils.pi)

# 2. Import specific things
from math_utils import add, pi

print("\nSpecific import:")
print(add(10, 20))
print(pi)

# 3. Alias import
import math_utils as mu

print("\nAlias import:")
print(mu.multiply(4, 5))


"""
PACKAGE: 
package is a folder that contains multiple modules + one special file called __init__.py (can be empty).
"""

# 1. Import full module from package
import my_package.math_utils as mu

print("Full module import:")
print(mu.add(5, 3))
print(mu.multiply(4, 5))

# 2. Import specific function from package
from my_package.math_utils import add

print("\nSpecific import:")
print(add(10, 20))

# 3. Using __init__.py exposure
from my_package import shout

print("\nUsing __init__.py:")
print(shout("hello"))
