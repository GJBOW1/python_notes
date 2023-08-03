# Python Notes from Coding Dojo 2023 - Gregg Bowen 

# *Pass
# If we start a code block, there must be at least one line of indented code immediately following. 
# If we try to run a file with a hanging code block, we'll get a syntax error. Luckily, Python has 
# provided us with the pass statement for situations where we know we need the block statement, but 
# we aren't sure what to put in it yet.

# For Example: 
# class EmptyClass:
#     pass

# for val in my_string:
#     pass

# The pass statement is a null operation; nothing happens when it executes. The pass is almost never 
# seen in final production, but can be useful in places where your code has not been completed yet.

# In addition to the traditional data types we are used to (ie: numbers, strings, boolean), we also have
# composite types, which include:

# *1) Tuples - A type of data that is immutable (can't be modified after its creation) and can hold a group of values. 
# Tuples can contain mixed data types.

# Example: dog = ('Bruce', 'cocker spaniel', 19, False)
# print(dog[0])		# output: Bruce
# dog[1] = 'dachshund'	# ERROR: cannot be modified ('tuple' object does not support item assignment)

# *2) Lists - A type of data that is mutable and can hold a group of values. Usually meant to store a 
# collection of related data.

# Example: 

# empty_list = []
# ninjas = ['Rozen', 'KB', 'Oliver']
# print(ninjas[2]) 	# output: Oliver
# ninjas[0] = 'Francis'
# ninjas.append('Michael')
# print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
# ninjas.pop()
# print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
# ninjas.pop(1)
# print(ninjas)	# output: ['Francis', 'Oliver']

# *Dictionaries - A group of key-value pairs. Dictionary elements are indexed by unique keys which are used 
# to access values. 

# Example: 

# empty_dict = {}
# new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
# new_person['name'] = 'Jack'	# updates if the key exists, adds a key-value pair if it doesn't
# new_person['hobbies'] = ['climbing', 'coding']
# print(new_person)	
# # output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
# w = new_person.pop('weight')	# removes the specified key and returns the value
# print(w)		# output: 160.2
# print(new_person)	
# # output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}        


# *If we're ever unsure of a value or variable's data type, we can use the type function to find out. 
# For example:

# print(type(2.63))		# output: <class 'float'>
# print(type(new_person))		# output: <class 'dict'>

# *For data types that have a length attribute (eg. lists, dictionaries, tuples, strings), we can 
# use the len function to get the length:

# print(len(new_person))		# output: 4 (the number of key-value pairs)
# print(len('Coding Dojo'))	# output: 11 

# *Javascript	                                                                Python
# int	var num = 35;	                                                            num = 25
# float	var dec = 4.2;	                                                        dec = 4.2
# log	console.log(num);	                                                        print(num)
# type check	console.log(typeof(dec));	                                        print(type(dec))
# conversion	N/A.  All numbers are floating point in Javascript	                num_to_dec = float(num)
# random number between 2-5	var rand_num = Math.floor(Math.random() * 4) + 2	import random rand_num = random.randint(2,5)


# *Numbers
# There are 3 basics types of numbers in Python.

# int - whole numbers, positive or negative.  ex. 35
# float - decimal numbers, positive or negative.  ex. 4.2
# complex - are a part of the real number system and are often referenced with the letter j.  ex. 1 + 3j.  
# **Note** If you're not sure if you need to use them, it's safe to say you can ignore this data type.

# *Conversion
# All Python objects have data type methods we can use to convert number types from one to another.
int_to_float = float(35)
float_to_int = int(44.2)
int_to_complex = complex(35)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))

# *Random Number
# Python does not have a built in random number generator, use the random module instead.
# example: 
# import random
# print(random.randint(2,5)) # provides a random number between 2 and 5

# *Concatenating Strings and Variables with the print function
# There are multiple ways that we can print a string containing data from variables.

# *The first is by adding a comma after the string, followed by the variable. Note that the comma 
# is outside the closing quotation mark of the string. The print() function inserts a space between 
# elements separated by a comma.

# name = "Zen"
# print("My name is", name)

# *The second is by concatenating the contents into a new string, with the help of +.

# name = "Zen"
# print("My name is " + name)

# *Type Casting or Explicit Type Conversion
# We may find ourselves wanting to change a value's data type from one type to another. Python 
# doesn't know how to add a string and a number, but it can add two strings together, so if we can 
# cast the number as a string, then we will be able to "add" the two values together, like so:

# print("Hello " + 42)			# output: TypeError
# print("Hello " + str(42))		# output: Hello 42

# Another example may be receiving a string input from a user that we want to treat as a number:

# total = 35
# user_val = "26"
# total = total + user_val		# output: TypeError
# total = total + int(user_val)		# total will be 61

# *String Interpolation
# We can also inject variables into our strings, which is known as string interpolation. There are 
# a few different ways this can be done.

# *F-Strings (Literal String Interpolation)
# Python 3.6 introduced f-strings for string interpolation. To construct a f-string, place an f right 
# before the opening quotation. Then within the string, place any variables within curly brackets.

# Example:
# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print(f"My name is {first_name} {last_name} and I am {age} years old.")







