import re

# In-Class Exercise #3
# Print each persons name and twitter handle, using groups, should look like:

# ==============
# Full Name / Twitter
# ==============

# Derek Hawkins / @derekhawkins

# Erik Sven-Osterberg / @sverik

# Ryan Butz / @ryanbutz

# Example Exampleson / @example

# Ripal Pael / @ripalp

# Darth Vader / @darthvader

f = open("./names.txt")

data = f.readlines()

print(data)

f.close()

names = re.compile("([A-Z][a-z]+), ([\w-]*[A-Z][a-z]+).*\s(@[a-zA-Z0-9]+)$")

for people in data:
    match = names.search(people)

    if match:
        print("\n", f"{match.group(2)} {match.group(1)} / {match.group(3)}")


# Regex project
# Use python to read the file regex_test.txt and print the last name on each line using regular expressions and groups (return None for names with no first and last name, or names that aren't properly capitalized)

# Hint: use with open() and readlines()

f = open("./regex_test.txt")

data = f.readlines()

print(data)

f.close()

famous_person = re.compile("[A-Z][a-z]+\s[\S]*[\s]*[A-Z][a-z]+")

for person in data:
    match = famous_person.search(person)
    if match:
        print("\n",f"{match.group()}")
    else:
        print(None)