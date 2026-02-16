
"""
what is an iterator?
iterator = something you can "loop over" one by one using next() or for loop
it remembers where it left off, gives you next item when you ask, and says "stop" when finished.
most things you already use in for loop are iterators:

list:  iterator
string:  iterator
range():  iterator
file when you do for line in file:  iterator

key idea:
iterator has two main jobs:
__iter__(): returns itself (or another iterator)
__next__(): gives next item, or raises StopIteration when done
"""
### super easy examples (copy-paste and feel it)

#### example 1 – list is already an iterator (you use it every day)

fruits = ["apple", "banana", "mango"]

it = iter(fruits)   # make iterator from list

print(next(it))     # apple
print(next(it))     # banana
print(next(it))     # mango
# print(next(it))   # StopIteration error – finished


#### example 2 – make your own tiny iterator (very simple class)

class Countdown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self   # i am my own iterator
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1   # return before decreasing

for num in Countdown(5):
    print(num)



#### example 3 – file lines are iterators (real useful)
with open("notes.txt") as f:
    it = iter(f)   # file becomes iterator
    
    print(next(it))   # first line
    print(next(it))   # second line
    # and so on...


# or normal way (python does iter + next for you):

for line in open("notes.txt"):
    print(line.strip())


"""why iterators feel magic
- you never run out of memory with big files/lists because it gives one item at a time
- `for` loop is just sugar for `iter()` + repeated `next()` + catch `StopIteration`
- many things (range, zip, map, filter, open files) are lazy iterators — they don't create full list in memory
"""
