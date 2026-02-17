'''JSON 

json = javascript object notation  
it’s basically a very popular way to store and send data that looks almost like a python dictionary.
'''
# example of json 
{
  "name": "alex",
  "age": 22,
  "is_student": True,
  "subjects": ["math", "science", "python"],
  "address": {
    "city": "delhi",
    "pin": 110001
  }
}

'''
why do we care in python?
because almost every real project talks to:
- websites/apis (they send/receive json)
- config files (settings.json)
- save/load data (user profiles, game scores…)
- databases (many return json)

the two main jobs in python
1. convert python data: json text (called dumping / serializing)  
2. convert json text: python data (called loading / deserializing)
'''
## step-by-step with easy examples
# first import the module (built-in, no install needed):
import json

## 1. python dict: json string (json.dumps)
person = {
    "name": "sara",
    "age": 25,
    "city": "mumbai",
    "hobbies": ["reading", "coding", "music"]
}

# convert to json string
json_text = json.dumps(person)

print(json_text)  # {"name": "sara", "age": 25, "city": "mumbai", "hobbies": ["reading", "coding", "music"]}

# want it pretty (readable with indentation)?
print(json.dumps(person, indent=4))

# output looks nice:
json
{
    "name": "sara",
    "age": 25,
    "city": "mumbai",
    "hobbies": [
        "reading",
        "coding",
        "music"
    ]
}


## 2. save python data to json file (json.dump)
with open("person.json", "w") as file:
    json.dump(person, file, indent=4)

print("saved to person.json")
# now you have a real file called `person.json` on your computer.

## 3. read json file → python dict (json.load)
with open("person.json", "r") as file:
    loaded_data = json.load(file)
print(loaded_data["name"])     # sara
print(loaded_data["hobbies"])  # ['reading', 'coding', 'music']

## 4. json string → python data (json.loads)
# if you get json as text (from api, copy-paste, etc.)
json_string = '''
{
    "product": "laptop",
    "price": 65000,
    "in_stock": true
}
'''
data = json.loads(json_string)
print(data["price"])   # 65000


# common real life patterns
## pattern 1: save settings
settings = {"theme": "dark", "font_size": 16, "auto_save": True}

with open("settings.json", "w") as f:
    json.dump(settings, f, indent=2)

## pattern 2: load and use
try:
    with open("settings.json") as f:
        settings = json.load(f)
    print("theme is", settings["theme"])
except FileNotFoundError:
    print("settings not found – using defaults")
    settings = {"theme": "light"}

## pattern 3: simple api-like response
students = [
    {"id": 1, "name": "riya", "marks": 92},
    {"id": 2, "name": "karan", "marks": 78}
]

print(json.dumps(students, indent=2))


''' important things to remember
json uses double quotes only (" not ')
true/false in json- True/False in python
null in json- None in python
numbers stay numbers, lists stay lists, dicts stay dicts
json can’t store python functions/classes— only basic types (str, int, float, bool, None, list, dict)
'''
