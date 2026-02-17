### filters()
# filter() keeps only the items that return **True** from the function you give it.
# Syntax:  
# filter(function, iterable)`
# Always convert result to list: `list(filter(...))`

## examples
# 1. Keep only even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)        

# 2. Keep numbers greater than 10
nums = [5, 12, 3, 18, 7, 15, 9]
big = list(filter(lambda x: x > 10, nums))
print(big)            

# 3. Keep only strings longer than 3 characters
words = ["cat", "dog", "elephant", "rat", "lion"]
long_words = list(filter(lambda w: len(w) > 3, words))
print(long_words)    

# 4. Remove empty strings
items = ["hello", "", "world", " ", None, "python"]
clean = list(filter(None, items))          # None as function keeps truthy values
print(clean)         

# 5. Keep only vowels from a string
text = "beautiful"
vowels = list(filter(lambda c: c in 'aeiou', text))
print(vowels)         

# 6. Using normal function 
def is_positive(n):
    return n > 0
values = [-5, 0, 3, -2, 7, 1]
positive = list(filter(is_positive, values))
print(positive)       

# 7. one-liner pattern
ages = [12, 17, 19, 15, 21, 16]
adults = list(filter(lambda age: age >= 18, ages))
print(adults)     


# example 1
nums = [3, 8, 2, 10, 1, 7]
big = list(filter(lambda x: x > 5, nums))
print(big)            

