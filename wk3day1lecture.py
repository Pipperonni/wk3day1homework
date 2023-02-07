import re

# re.compile()
# pattern = re.compile("abcd")

# # re.match() Only starting at the beginning
# match = pattern.match("abcd123")
# print(match)
# Accessing the span of the match
# print(match.span())

# example = "abcd123"

# "abcd123"[match.span()[0]: match.span()[1]]
# # OR
# span = match.span()
# "abcd123"[span[0]:span[1]]

# example[span[0]:span[1]]
# # re.findall()

# random_string = "123 123 234 abcd abc abcabc abc abcd"

# finders = pattern.findall(random_string)

# print(finders)
# re.search()

# found_searching = pattern.search(random_string)

# print(found_searching)

# print(isinstance(found_searching.span(), tuple))

# print(random_string[found_searching.span()[0]:found_searching.span()[-1]])

## SETS

## [a-z] or [A-Z] - any lowercase/uppercase letters from a to z
## [^2] - anything that's not 2


## Integer Ranges

# pattern_int = re.compile("[0-7][7-9][0-3]")

# random_number = pattern_int.match("67383") # checks just the beginning of string
# print(random_number)
# # OR
# random_number1 = pattern_int.search("67383") # checks the whole string till it finds the first instence of the match of pattern_int

# int_span = random_number[random_number.span()[0]]

# print(int_span)


## Character Ranges

# pattern_char = re.compile("[A-Z][a-z]")

# matrix_string = "Hello Mr. Anderson"
# found = pattern_char.findall(matrix_string)
# print(found)
## COUNTING OCCURENCES

## {x} - something that occurs {num_of_times}

# matrix_string2 = "Hello Mr. An33derson"

# pattern_occur = re.compile("[A-Z][a-z][0-3]{2}")

# print(pattern_occur.findall(matrix_string2))
# ## {x, x} - something that occurs between x and x times

# example = "This is an example of a regex trying to find one m, more than one mmm or five mmmmms"

# found_ms = find_ms = re.compile("m{1,5}")

# print(find_ms.findall(example))

# ## ? - something that occurs 0 or 1 time

# matrix_string3 = "Hello M There Mr.Anderson, Mid how is Mrs.Anderson, and Ms.Anderson MMMMsss?"

# pattern = re.compile("Mr?s?")

# # print(pattern.findall(matrix_string3))

# ## * - something that occurs at least 0 times

# pattern_zero = re.compile("M*s") # does not require the Ms pattern
# print(pattern_zero.findall(matrix_string3))

# ## + - something that occurs at least once

# pattern_m = re.compile("M+s") # require Ms pattern
# print(pattern_m.findall(matrix_string3))

# ## In-class exercise 1:

# my_string = "This string has 10909090 numbers, but it is only 1 string. I hope you solve this 2day."

# just_numbers = re.compile("[0-9]+")

# print(just_numbers.findall(my_string))

# Escaping Characters

# \w - look for any Unicode character
# \W - look for anything that isnt a Unicode character

# unicode_pattern = re.compile("[\w]+")
# # OR
# non_unicode_pattern = re.compile("[\W]+")

# string_with_punctuation = "This is a sentence. With an, exclamation mark at the end!"

# found_unicode = unicode_pattern.findall(string_with_punctuation)
# found_non_unicode_pattern = non_unicode_pattern.findall(string_with_punctuation)
# print(found_unicode)
# print(found_non_unicode_pattern)


# History on Unicode

# More on Unicode Characters


# \d - look for any digit 0-9
# \D - look for anything that isnt a digit

# string_with_dates = "Today is the 6th, in 20days it will be the 27th. 3rd,1st,30th"

# days_pattern = re.compile("\d{1,2}[d-t]{2}")

# found_days = days_pattern.findall(string_with_dates)

# print(found_days)
# \s - look for any white space
# \S - look for anything that isnt whitespace

# spooky = "Are you afraid       of the dark?"

# pattern = re.compile("\S+")
# pattern_space = re.compile("\s+")

# spaces = pattern_space.findall(spooky)
# print(spaces)

# not_spaces = pattern.findall(spooky)
# print(not_spaces)
# # \b - look for boundaries or edges of a word
# # \B - look for anything that isnt a boundary

# string = "TheCodingTemple"

# pattern_bound = re.compile(r"\bTheCodingTemple\b")

# found_bound = pattern_bound.findall(".TheCodingTemple.")
# print(found_bound)

# pattern_no_bound = re.compile(r"\BTheCodingTemple\B")
# found_no_bound = pattern.findall("TheCodingTemple")
# print(found_no_bound)



# # Grouping

# name_string = "Max Smith, aaron rodgers, Sam Darnold, LeBron James, Micheal Jordan, Kevin Durant, Patrick McCormick"

# group_pattern = re.compile("([A-Z][a-zA-z]+) ([A-Z][a-zA-Z]+)")

# found_names = group_pattern.findall(name_string)
# print(found_names)

# name = name_string.split(", ")
# # print(name)

# for n in name:
#     if group_pattern.match(n):
#         print(f"{n} is a name")
#     else:
#         print(f"{n} is not a name")

# # Opening a File

# # Python gives us a couple ways to import files, below are the two used most often.

# open()

f = open("./names.txt")

data = f.read()

print(data)

f.close()

# with open()

# re.match()

instructor = re.compile("Hawkins, Derek")

my_match = instructor.match(data)

print(my_match)

# re.search()

print(re.search(r"ripalp@codingtemple.com", data))
# OR
pattern = re.compile("ripalp@codingtemple.com")
pattern.search(data)

# Store the String to a Variable

answer = input("What would you like to search for?: ")

input_pattern = re.compile(answer)

found = input_pattern.search(data)

if found:
    print(found)
else:
    print("No match")