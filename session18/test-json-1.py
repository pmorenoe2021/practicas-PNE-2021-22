import json
import termcolor
from pathlib import Path


jsonstring = Path("people1.json").read_text()  # -- Read the json file
person = json.loads(jsonstring)  # Create a dictionary from the json string

# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'
firstname = person['Firstname']  # -- Read the Firtname
lastname = person['Lastname']
age = person['age']

print()  # Print the information on the console, in colors
termcolor.cprint("Name: ", 'green', end="")
print(firstname, lastname)
termcolor.cprint("Age: ", 'green', end="")
print(age)