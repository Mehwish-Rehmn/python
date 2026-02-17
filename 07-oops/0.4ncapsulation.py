'''
Encapsulation:
in oops is one of the four main pillars of object-oriented programming.
Simple words:  
encapsulation means keeping the data and the methods that work on that data together inside one box (class), and hiding the internal details from the outside world.

think of it like a medicine capsule:
- outside you see only the smooth shell (public interface)
- inside there is medicine + exact ingredients + how it works — you don't touch or see that directly
- you just swallow it (use the public method) and it does its job safely

### why do we need encapsulation?

without it:
- anyone can directly change important data- bugs, wrong values
- code becomes messy— everyone is touching internal parts
- hard to change later— because everyone knows the internal structure

with encapsulation:
- data is safe (protected or private)
- you control how data is changed (through methods)
- easy to change internal logic later without breaking other code
- code is cleaner and safer

How encapsulation works in python (STEP WISE)
python uses naming conventions to show what is private/public:
- public: normal name- self.name
- protected: single underscore- self._balance(convention: please don't touch directly)
- private: double underscore- self.__secret(name mangling — python hides it strongly)
'''
### very easy real example – bank account
class BankAccount:
    def __init__(self, name, balance):
        self.name = name               
        self.__balance = balance        

    # public methods – the only safe way to interact
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"deposited ₹{amount}. new balance: {self.__balance}")
        else:
            print("amount must be positive")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"withdrew ₹{amount}. remaining: {self.__balance}")
        else:
            print("not enough money or invalid amount")

    def get_balance(self):
        return self.__balance         

# use it
acc = BankAccount("robert", 10000)

acc.deposit(5000)          
acc.withdraw(2000)          
print(acc.get_balance())    

# these will not work directly
# print(acc.__balance)      # AttributeError – hidden!
# acc.__balance = -10000    # doesn't affect real balance (new variable created)


''' key points about encapsulation in python

1. private attributes(__name) are name-mangled
   python changes the name inside the class to '_ClassName__name' 
   so 'self.__balance' becomes '_BankAccount__balance'  
   → very hard to access from outside by accident

2. protected attributes(_name)  
   just a convention- "please don't touch me directly"  
   programmers respect it, but python won't stop you
'''
## 3. getter & setter methods- best practice
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):              # getter
        return self.__age

    @age.setter
    def age(self, new_age):     # setter
        if new_age >= 0 and new_age <= 120:
            self.__age = new_age
        else:
            print("invalid age")

p = Person("alex", 25)
print(p.age)          
p.age = 30            
p.age = -5           
