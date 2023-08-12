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
# int_to_float = float(35)
# float_to_int = int(44.2)
# int_to_complex = complex(35)
# print(int_to_float)
# print(float_to_int)
# print(int_to_complex)
# print(type(int_to_float))
# print(type(float_to_int))
# print(type(int_to_complex))

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

# *string.format()
# Prior to f-strings, string interpolation was accomplished with the .format() method. 
# If you're searching online, you will likely find code snippets using this method. To use it, 
# type out the full string, replacing any words that will get their values from variables with {}. 
# Then call the format method on the string, passing in arguments in the order in which they should 
# fill the {} placeholders. Here's an example:

# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# # output: My name is Zen Coder and I am 27 years old.
# print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# # output: My name is 27 Zen and I am Coder years old.

# *%-formatting
# There is an even older method of string interpolation that you may come across when troubleshooting 
# or researching, so you should know about it. Rather than curly braces, the % symbol is used to 
# indicate a placeholder, a %s for a string and %d for a number. After the string, a single % separates 
# the string to be interpolated from the values to be inserted into the string, like so:

# hw = "Hello %s" % "world" 	# with literal values
# py = "I love Python %d" % 3 
# print(hw, py)
# # output: Hello world I love Python 3
# name = "Zen"
# age = 27
# print("My name is %s and I'm %d" % (name, age))		# or with variables
# # output: My name is Zen and I'm 27

# *Built-In String Methods
# We've seen the format method, but there are several more methods that we can run on a string. 
# Here's how to use them:

# x = "hello world"
# print(x.title())
# # output:
# "Hello World"

# *The following is a list of commonly used string methods:
#.title(): returns a string with every word beginning with an upper case character. 
# string.upper(): returns a copy of the string with all the characters in uppercase.
# string.lower(): returns a copy of the string with all the characters in lowercase.
# string.count(substring): returns number of occurrences of substring in string.
# string.split(char): returns a list of values where string is split at the given character. Without a parameter the default split is at every space.
# string.find(substring): returns the index of the start of the first occurrence of substring within string.
# string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.
# string.join(list): returns a string that is all strings within our set (in this case a list) concatenated.
# string.endswith(substring): returns a boolean based upon whether the last characters of string match substring.

# It's important to know that we have only introduced you the basics of what we can do with strings. There 
# is a lot more you can do with string interpolation, and every data type has numerous built-in methods. 
# The Python documentation is the best place to look for more information. For example, under section 4.7.1 
# of https://docs.python.org/3/library/stdtypes.html, you will find the string methods. Have a general idea 
# of the tools we have available to us and try experimenting with them in the shell to see what they can do, 
# but don't spend time trying to memorize them, though. You can always look up whatever you need to use.

#Lists:
# A list, also known as an array in other programming languages, is a data type that allows you to hold 
# groups of values. Think of a list like a dresser with multiple drawers in which each drawer stores some 
# information. Lists are created with values inside of square brackets [], where each value is separated 
# by a comma. After a list is created, it can still be updated by adding values and/or by deleting values. 
# An empty list is simply [ ].

# In Python, the elements of a list do not have to be of the same data type. A list can be a mixture of any 
# Python data types, including, tuples, strings, numeric, and even a list itself (a list within a list). An 
# example:

# ninjas = ['Rozen', 'KB', 'Oliver']
# my_list = ['4', ['list', 'in', 'a', 'list'], 987]
# empty_list = []

# Another cool feature of lists in python is that you can combine them together and duplicate values fairly 
# easily, by using the + and * operators. If you 'add' lists together, it will create a new list that 
# contains all the values of both of the arrays! Likewise, if you 'multiply' a list by a whole number it 
# will copy all of the values that many times, and make a new list with all the copied values. Consider the 
# example below:

# fruits = ['apple', 'banana', 'orange', 'strawberry']
# vegetables = ['lettuce', 'cucumber', 'carrots']
# fruits_and_vegetables = fruits + vegetables
# print(fruits_and_vegetables)
# salad = 3 * vegetables
# print(salad)


# *Appending Values to a List
# Here's a useful example of a method that we will use to manipulate lists:

# some_list.append(some_value)

# Appends a new item onto the end of the given list. You can pass any data type into this function.

# nums = [1,2,3,4,5]
# nums.append(99)
# print(nums)
# #the output would be [1,2,3,4,5,99]

#*Slicing
# It's also useful to know that Python uses the following syntax: [:] to return a copy of some portion of the list, constrained by specified indices. This is called slicing and it can be useful if you want to:

# Use a copy of the list so you don't have to change the original
# Only use a portion of a list.
# The starting index and ending index should be separated by the : character. 

# words = ["start","going","till","the","end"]
# # Sub-ranges (portions) of the list
# print(words[1:]) # prints ['going', 'till', 'the', 'end']
# print(words[:4]) # prints ['start', 'going', 'till', 'the']
# print(words[2:4]) # prints ['till', 'the']
    
# # Making a copy of a list
# copy_of_words = words[:]
# copy_of_words.append("dojo") # only appends to the copy
# print(copy_of_words) # prints ['start', 'going', 'till', 'the', 'end', 'dojo']
# print(words) # prints ['start', 'going', 'till', 'the', 'end']

#*Built-in Python Functions for Sequences
# Below is an example of a built-in function that deals with lists. The following functions can also be applied to all sequence types, including dictionaries, strings and tuples. What do we mean when we say sequence? Think of a sequence as anything over which we can iterate. Here's one commonly used sequence function:

# len(sequence)

# my_list = [1, 'Zen', 'hi']
# print(len(my_list))
# # output
# 3

# Examples:
# len(sequence) returns the length (number of items) in a sequence.
# max(sequence) returns the highest value in a sequence.
# min(sequence) returns the lowest value in a sequence.
# sorted(sequence) returns a sorted sequence

# There are a many other useful built-in functions. You can find them below:
# https://docs.python.org/2/library/functions.html

# The  .append method you learned in the prior lesson is an example of a built-in list method. The built-in methods listed below are specific to lists versus other data types, much like the string methods shown in the previous tab. In order to use a built-in list method, you use dot-notation with an existing list, like so:

# some_list.pop()

# my_list = [1,5,2,8,4]
# my_list.pop()
# print(my_list)
# # output:
# # [1,5,2,8]

#*The following are some commonly used list methods:
# list.append(value) appends a value to the end of the list.
# list.pop(index) remove a value at given position. if no parameter is passed, it will remove the last value in the list.
# list.index(value) returns the index (position) of the given value if it exists in the list and raises an error if it does not exist.
# list.reverse() reverses the order of the elements, in place.*
# list.sort() sorts the items in order of least to greatest, or alphabetically for strings, in place.*

# "In place" means it changes that same array, instead of returning a new array.

# These are just some of the things you can do to manipulate or extract information from a list.
# To learn more about other built-in functions you can use with a list, visit this:
# https://docs.python.org/3/tutorial/datastructures.html

#*Tuple
# A Tuple is a container for a fixed sequence of data objects. The name comes from the Latin suffix 
# for multiples: double, triple, quadruple, quintuple. Tuples are sequences, just like lists. The only 
# difference is that tuples can't be changed -- that is, tuples are immutable. Also, while lists are 
# defined using square brackets, tuples use parentheses. Creating a tuple is as simple as declaring 
# different comma-separated values. Optionally you can put these values between parentheses.

# For example:

# tuple_data = ('physics', 'chemistry', 1997, 2000)
# tuple_num = (1, 2, 3, 4, 5 )
# tuple_letters = "a", "b", "c", "d"

# The Take Home: Watch Out for Tuples!
# As you evolve as a programmer, you will see that tuples can be extremely useful. 
# While you won't be creating and utilizing tuples a lot in this course, you will definitely encounter 
# them in Flask, used by the framework for immutable dictionaries among other things. You may also run 
# into some baffling logical errors that have to do with tuples. For example, if you accidentally type 
# a comma at the end of a line of code that assigns a variable to a value, your code will not error out, 
# but instead interpret the stored value as a tuple! 

# So far, you've probably built enough pattern-recognition in coding to intuitively know that parentheses, 
# (), almost always mean you're dealing with a function -- a function call, the beginning of a list of 
# arguments for a function, or the definition of a function. But watch out, occasionally you may be dealing 
# with a tuple! For more, read this: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences

# *Conditionals
# Conditional statements allow us to run certain lines of code depending on whether certain conditions are 
# met.  These statements control the flow of how our code is executed by the interpreter.  In Python, the 
# keywords for conditional statements are if, elif, and else. Here are some examples:

# x = 12
# if x > 50:
#     print("bigger than 50")
# else:
#     print("smaller than 50")
#     # because x is not greater than 50, the second print statement is the only one that will execute
    
#     x = 55
#     if x > 10:
# print("bigger than 10")
#     elif x > 50:
# print("bigger than 50")
#     else:
# print("smaller than 10")
#     # even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'
    
#     if x < 10:
# print("smaller than 10")
#     # nothing happens, because the statement is false   

#*For Loops with Range
# If we want to iterate through numbers, we can use Python's range function. It can have between 1 and 3 arguments:

# Note that if you need to specify an increment other than +1, all three arguments are required.

# for x in range(0, 10, 2):
#     print(x)
# # output: 0, 2, 4, 6, 8
# for x in range(5, 1, -3):
#     print(x)
# # output: 5, 2

#*For Loops through Strings
# Since a loop can be used on any sequence, you can access each value of a string individual with loop.

# for x in 'Hello':
#     print(x)
# output: 'H', 'e', 'l', 'l', 'o'

#*For Loops through Lists
# If we want to iterate through a list, we could use the range function and send in the length of the 
# list as the stopping value, but if we are not interested in the index values and want to just see the 
# values of each item in the list in order, we can actually loop to get the values of the list directly!

# my_list = ["abc", 123, "xyz"]
# for i in range(0, len(my_list)):
#     print(i, my_list[i])
# # output: 0 abc, 1 123, 2 xyz
    
# # OR 
    
# for v in my_list:
#     print(v)
# # output: abc, 123, xyz

#*While Loops:
# We can go from a 'for loop':
# for count in range(0,5):
#     print("looping =", count)

# To a 'while loop':
# count = 0
# while count <= 5:
#     print("looping - ", count)
#     count += 1

# Else
# There are certain conditions that we give for every loop that we have, but what if the condition was 
# not met and we still would like to do something if that happens? We can then use an else statement 
# with our while loop. Yes, that is right, else in a loop.

# y = 3
# while y > 0:
#     print(y)
#     y = y - 1
# else:
#     print("Final else statement")

# The output would look like this:
# 3
# 2
# 1
# Final else statement

# Note that this else code section is only executed if the while loop runs normally and its conditional 
# is false (whether we never entered the while loop, or we did but eventually the conditional changed 
# from true to false). If instead our while loop is exited prematurely because of a break or 
# return statement, then the else code section will never be executed.

#*Loop Control
# We were introduced to control flow in the previous tabs with if and else statements. Loops, breaks, 
# and continues are all a part of control flow as well. Control flow is the cornerstone of most programming 
# languages.

# When you want finer control over your loops, use the following statements to do so.

#*Break
# The break statement exits the current loop prematurely, resuming execution at the first post-loop 
# statement. The break statement can be used in both while and for loops.

# The most common use for the break is when some external condition is triggered, requiring a hasty exit 
# from a loop.

# When loops are nested, a break will only exit from the innermost loop.
# For example:
    
# for val in "string":
#     if val == "i":
#         break
#     print(val)
# # output: s, t, r

# *Continue
# The continue statement immediately returns control to the beginning of the loop. In other words, the 
# continue statement rejects, or skips, all the remaining statements in the current iteration of the loop, 
# and continues normal execution at the top of the loop.

# The continue statement is very useful when you want to skip specific iteration(s), but still keep looping 
# to the end. For example:

# for val in "string":
#     if val == "i":
#         continue
#     print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i

# A function is a named block of code that we can execute to perform a specific task. More simply, 
# a function is a list of instructions that we can run at any time and as many times as we would like. 
# If we find something that we seem to be using over and over again, it might be best to have a way to 
# streamline the process. A function:

# has a name
# takes in parameters (parenthesis required, parameters optional)
# perform a series of instructions
# return something afterwards (will return None if there is no explicit return statement)
# Think of the function as a recipe. If we were preparing a meal we would:

# Specify the ingredients (variables) needed for the meal
# Use the actual ingredients (pass arguments) when starting (invoke a function)
# We follow the instructions step by step (function) for the ingredients (parameters) and prepare them
# Once the food is ready we serve it up to those that are eating. (return)

# The recipe has all the instructions to prepare a meal and lays out the instructions. When you want to 
# start cooking, you call the recipe function and return your food so that can eat it.

# The advantages of using functions are:

# Reducing the duplication of code
# Breaking down complex problems into simpler pieces
# Improving clarity of code

# *Syntax
# The def keyword signifies the declaration of a function. This indicates that the following code is a 
# function and assigns a name to that function, so we can call it later. Parameters are inputs the function 
# is expecting and appear inside the parenthesis that follow the function name.

# Here's a basic example of a function:
# def add(a,b):	# function name: 'add', parameters: a and b
#     x = a + b	# process
#     return x	# return value: x

# We have declared a function with the def keyword, named it add, and specified that it takes two inputs 
# (parameters). If this is all we have in our file, nothing would actually appear to happen if we ran it. 
# To actually run the function, we must execute it by invoking or calling it. This is done outside of the 
# function using the function name followed by (). Inside the parenthesis are any values (arguments) the 
# function is expecting as input.

# new_val = add(3, 5)    # calling the add function, with arguments 3 and 5
# print(new_val)    # the result of the add function gets sent back to and saved into new_val, so we will see 8

# Once invoked, a function can give us an output. Some functions take an input and some functions don't give 
# us an output. Even if no output is produced, the code inside the function can alter the program - this is 
# called a side effect. Based upon what we learned above, a function that doesn't return anything would 
# produce no output!

# *Parameters and Arguments
# We define the input of functions using parameters. Functions can have as many parameters as we need, 
# including 0. Here we've defined the say_hi function with one parameter called name:

# def say_hi(name):
#     print("Hi, " + name)

# # invoking the function 3 times, passing in one argument each time
# say_hi('Michael')
# say_hi('Anna')
# say_hi('Eli')

# Wait, but what's the difference between a parameter and an argument? These two words get mixed up a lot 
# in programming. In this example 'name' is a parameter while "Michael", "Anna", and "Eli", are arguments. 
# We define parameters. We pass in arguments into functions.

# *Returning Values
# So far none of our functions had any value that we could hold onto. In many cases, we would want our function to return some sort of value that we can use later in our program. The following concept is critical in understanding how to use functions correctly in your code:

# It is very important to remember the following: a function call is equal to whatever that function returns. This might not make sense until we see it in action.

# Let's modify our original say_hi function and observe the differences:

# def say_hi(name):
#     return "Hi " + name
# greeting = say_hi("Michael") # the returned value from say_hi function gets assigned to the 'greeting' variable
# print(greeting) # this will output 'Hi Michael'

# Returning a value from a function allows us to store that value in a variable. In this example, we invoked 
# the say_hi function with "Michael" and set it to the greeting variable. When we print greeting we see that 
# it contains the returned value of the say_hi function - "Hi Michael".

# *Return Also Means Exit & Print Statements are for Debugging
# Many students at first have trouble understanding the difference between a print statement and a return 
# statement. There are two big differences:

# Saving values: When you print something with  print(), strictly speaking, it doesn't have any affect 
# on your program. No data is saved or changed or passed anywhere else in the program. Print statements 
# are primarily used for programmers to debug the code, to see what's happening in the program. On the 
# other hand, a return statement may pass a value back to the outer scope after it's done running for 
# the program to use!
# Exiting the function: Reaching a return statement always means "EXIT THIS FUNCTION NOW" whether or not 
# there is more code. Any remaining code will not be run.

#When running a function and you want to enter results on a new line, you can use \n.

# *Default Parameters
# With the functions we've written so far, we've had to provide the exact number of arguments specified 
# when calling the function. However, if we'd like to allow some of the parameters to be optional to the 
# caller of the function, we can set defaults. Take the following function as an example. The purpose of 
# the function is to take a name and a number and print "good morning {some_name}" to the terminal the 
# given number of times. If no name or number is given, the name is blank and the number is 2, respectively.

# set defaults when declaring the parameters
# def be_cheerful(name='', repeat=2):
# 	print(f"good morning {name}\n" * repeat)
# be_cheerful()    # output: good morning (repeated on 2 lines)
# be_cheerful("tim")    # output: good morning tim (repeated on 2 lines)
# be_cheerful(name="john")    # output: good morning john (repeated on 2 lines)
# be_cheerful(repeat=6)    # output: good morning (repeated on 6 lines)
# be_cheerful(name="michael", repeat=5)    # output: good morning michael (repeated on 5 lines)
# # NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
# be_cheerful(repeat=3, name="kb")    # output: good morning kb (repeated on 3 lines)

# Note all the different ways we are able to call on this one function! Even though our function defines 2 parameters, if:

# no arguments are provided -- the defaults are used
# one unnamed argument provided -- provided value is used as the value for the first parameter, and the second parameter's default value is used
# one named argument provided -- provided value is used as the value of the parameter of the same name, and the other parameter's default value is used
# both unnamed arguments provided -- values assigned to parameters in order (i.e. what we've been doing up to this point)
# both named arguments provided -- values are assigned to associated parameter (and then order doesn't matter!)



# When wanting to use random numbers, you can import the random module.
# Then you use the randint(starting_number, ending_number) function to set arguments. For example:
# import random 
# random_number = random.randint(0,5)
# An important note about using random is that the ending number is inclusive, unlike when doing a for loop, for example.

# Below is an example application of the above. It is using the random_num variable to randomly select the indices for
# the numbers variable. 

# import random
# random_num = random.randint(0,5)
# numbers = ["zero", "one", "two", "three", "four", "five"]
# print(numbers[random_num])

# *Changing or Updating Values
# Each key in a dictionary must be unique. If you make an assignment using an existing key as the index, the old value 
# associated with that key is overwritten by the new value. You can use this characteristic to an advantage in order to 
# modify an existing value for an existing key. 

# person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
# # Adds a new key value pair for email to person
# person["email"] = "alovelace@codingdojo.com"

# # Changes person's "last" value to "Bobada"
# person["last"] = "Bobada"
# print(person)

# *Testing for an Existing Key
# Sometimes you may want to test if a key already exists in the dictionary to know whether to add an initial value or 
# replace an existing value.

# if some_key in my_dictionary:
#     # update the value

# This also works with the not logical operator:

# if "email" not in person:
#     person["email"] = "newemail@email.com"
# else:
#     print("Would you like to replace your existing email?")

# *Accessing Values
# To access the values of a dictionary, you can use the familiar square brackets along with the key to obtain its value.

# print(person["first_name"])
# full_name = person["first_name"] + " " + person["last_name"]

# *Removing Values
# There are 2 ways to remove a key:value pair from a dictionary. 

# value_removed = capitals.pop('svk') # will remove the key 'svk' and return it's value
# del capitals['dnk'] # will delete the key, and not return anything

# *Multi-Line Syntax Too!
# You can write any dictionary's key-value pairs on multiple lines to make it easier to read, which is very useful for larger 
# dictionaries. For example the following dictionary.

# person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}

# ..can also be written like so:

# person = {
#     "first": "Ada", 
#     "last": "Lovelace", 
#     "age": 42, 
#     "is_organ_donor": True
# }

# *Common Built-in Functions and Methods
# Python includes the following standalone functions for dictionaries:

# len() - give the total length of the dictionary.
# str() - produces a string representation of a dictionary.
# type() - returns the type of the passed variable. If passed variable is a dictionary, it will then return a dict type.
# Here are some very useful Python dictionary methods:

# .clear() - removes all elements from the dictionary
# .get(key, default=None) - A safe way to get a value, if the key might not exist. Returns the value for the specified key or None (or a value you specify) if the key is not in the dictionary.
# .update(pairs_to_update) - Add and update multiple key-value pairs at once, by passing in another dictionary of the pairs to update and add.

# *Other Useful Methods!
# https://www.w3schools.com/python/python_ref_dictionary.asp

# *For Loops through Dictionaries
# Dictionaries are also iterable. When we iterate through a dictionary, the iterator is each of the keys of the dictionary.

# my_dict = { "name": "Noelle", "language": "Python" }
# for each_key in my_dict:
#     print(each_key)
# # output: name, language

# That means if we want the values of our dictionary, we might do something like this:

# my_dict = { "name": "Noelle", "language": "Python" }
# for each_key in my_dict:
#     print(my_dict[each_key])
# # output: Noelle, Python

# Dictionaries also have a few additional methods that allow us to iterate through them and have the keys and/or values as the iterator. 
# Test these out to get a better understanding:

# capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# # another way to iterate through the keys
# for key in capitals.keys():
#      print(key)
# # output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
# #to iterate through the values
# for val in capitals.values():
#      print(val)
# # output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
# #to iterate through both keys and values
# for key, val in capitals.items():
#      print(key, " = ", val)
# # output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

# *Nesting
# Nesting is also allowed in dictionaries. In other words, dictionaries may contain lists and tuples as well as other dictionaries. 
# Likewise, lists may contain dictionaries. All of these may be many levels deep! In this module you'll become more familiar 
# with how to manipulate nested lists and dictionaries.

# # List of dictionaries
# users = [
#     {"first": "Ada", "last": "Lovelace"}, # index 0
#     {"first": "Alan", "last": "Turing"}, # index 1
#     {"first": "Eric", "last": "Idle"} # index 2
# ]
# # Dictionary of lists
# resume_data = {
#     #        	     0           1           2
#     "skills": ["front-end", "back-end", "database"],
#     #                0           1
#     "languages": ["Python", "JavaScript"],
#     #                0              1
#     "hobbies":["rock climbing", "knitting"]
# }

# *Accessing Values in Nested Dictionaries
# To access a value in a nested data structure take a look at how you would access the first user's last name. 

# print(users[0]["last"]) # prints Lovelace

# First, users[0] is the whole user dictionary stored at index 0. Next, you find the value stored at the key "last" where 
# we finally get the raw value, "Lovelace". 