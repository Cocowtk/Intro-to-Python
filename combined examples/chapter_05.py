# The following will allow for the use of .magic to clear console and variables
from IPython import get_ipython

# Section 5.2 snippets

# Creating a List
c = [-45, 6, 0, 72, 1543]

c

# Accessing Elements of a List
c[0]

c[4]

# Determining a List’s Length 
len(c)

# Accessing Elements from the End of the List with Negative Indices
c[-1]

c[-5]

# Indices Must Be Integers or Integer Expressions
a = 1

b = 2

c[a + b]

# Lists Are Mutable
c[4] = 17

c

# Some Sequences Are Immutable
s = 'hello'

s[0]

s[0] = 'H'

# Attempting to Access a Nonexistent Element
c[100]

# Using List Elements in Expressions
c[0] + c[1] + c[2]

# Appending to a List with +=
a_list = []

for number in range(1, 6):
    print("number is "+str(number))                         # Added by TAA
    print("putting it into a_list["+str(len(a_list))+"]")   # Added by TAA
    print()                                                 # Added by TAA
    a_list += [number]
    
    
a_list

a_list += (range(1,6))                          # Added by TAA

a_list                                          # Added by TAA

letters = []

letters += 'Python'

letters

letters = []                                    # Added by TAA

letters = letters + 'Python'                    # Added by TAA - Won't Work

letters                                         # Added by TAA

letters[len(letters):len(letters)] = ["Python"] # Added by TAA

letters                                         # Added by TAA

# Concatenating Lists with +
list1 = [10, 20, 30]

list2 = [40, 50]

concatenated_list = list1 + list2

concatenated_list

# Using for and range to Access List Indices and Values
for i in range(len(concatenated_list)):  
    print(f'{i}: {concatenated_list[i]}')

# Comparison Operators
a = [1, 2, 3]

b = [1, 2, 3]

c = [1, 2, 3, 4]

a == b

a == c

a < c

c >= b

# Cleaning up at end of snippet
get_ipython().magic('reset -f')
get_ipython().magic('clear')


##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 5.2 Self Check snippets

# Exercise 3

def cube_list(values):
    for i in range(len(values)):
        values[i] **= 3
        
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cube_list(numbers)

numbers


# Exercise 4
characters = []

characters += 'Birthday'

characters




##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 5.3 snippets

# Creating Tuples
student_tuple = ()

student_tuple

len(student_tuple)

student_tuple = 'John', 'Green', 3.3

student_tuple

len(student_tuple)

another_student_tuple = ('Mary', 'Red', 3.3)

another_student_tuple

a_singleton_tuple = ('red',)  # note the comma

a_singleton_tuple

# Accessing Tuple Elements
time_tuple = (9, 16, 1)

time_tuple

time_tuple[0] * 3600 + time_tuple[1] * 60 + time_tuple[2]

# Adding Items to a String or Tuple
tuple1 = (10, 20, 30)

tuple2 = tuple1

tuple2

hash(tuple1)                                # Added by TAA

hash(tuple2)                                # Added by TAA

tuple1 += (40, 50)

tuple1

tuple2

hash(tuple1)                                # Added by TAA

hash(tuple2)                                # Added by TAA

# Appending Tuples to Lists
numbers = [1, 2, 3, 4, 5]

numbers += (6, 7)

numbers

# Tuples May Contain Mutable Objects
student_tuple = ('Amanda', 'Blue', [98, 75, 87])

hash(student_tuple)                         # Added by TAA - Won't work

id(student_tuple)                           # Added by TAA

student_tuple[2][1] = 85

student_tuple

id(student_tuple)                           # Added by TAA

# Cleaning up at end of snippet
get_ipython().magic('reset -f')
get_ipython().magic('clear')

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 5.3 Self Check snippets

# Exercise 3
single = (123.45,)

single

# Exercise 4
[1, 2, 3] + (4, 5, 6)




##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 5.4 snippets
student_tuple = ('Amanda', [98, 85, 87])

first_name, grades = student_tuple

first_name

grades

first, second = 'hi'

print(f'{first}  {second}')

number1, number2, number3 = [2, 3, 5]

print(f'{number1}  {number2}  {number3}')

number1, number2, number3 = range(10, 40, 10)

print(f'{number1}  {number2}  {number3}')

# Swapping Values Via Packing and Unpacking
number1 = 99

number2 = 22

number1, number2 = (number2, number1)

print(f'number1 = {number1}; number2 = {number2}')

# Accessing Indices and Values Safely with Built-in Function enumerate
colors = ['red', 'orange', 'yellow']

list(enumerate(colors))

tuple(enumerate(colors))

for index, value in enumerate(colors):
    print(f'{index}: {value}')
    
# Cleaning up at end of snippet
get_ipython().magic('reset -f')
get_ipython().magic('clear')

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 5.4 Self Check snippets

# Exercise 3
high_low = ('Monday', 87, 65)

high_low 

print(f'{high_low[0]}: High={high_low[1]}, Low={high_low[2]}') 

day, high = high_low

# Exercise 4
names = ['Amanda', 'Sam', 'David']

for i, name in enumerate(names):
    print(f'{i}: {name}')
    


##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 5.5 snippets

# Specifying a Slice with Starting and Ending Indices
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

numbers[2:6]

# Specifying a Slice with Only an Ending Index
numbers[:6]

numbers[0:6]

# Specifying a Slice with Only a Starting Index
numbers[6:]

numbers[6:len(numbers)]

# Specifying a Slice with No Indices
numbers[:]

# Slicing with Steps
numbers[::2]

# Slicing with Negative Indices and Steps
numbers[::-1]

numbers[-1:-9:-1]

# Modifying Lists Via Slices
numbers[0:3] = ['two', 'three', 'five']

numbers

numbers[0:3] = []

numbers

numbers = [2, 3, 5, 7, 11, 13, 17, 19]

numbers[::2] = [100, 100, 100, 100]

numbers

id(numbers)

numbers[:] = []

numbers

id(numbers)

numbers = []

numbers

id(numbers)

# Cleaning up at end of snippet
get_ipython().magic('reset -f')
get_ipython().magic('clear')

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 5.5 Self Check snippets

# Exercise 3
numbers = list(range(1, 16))

numbers

numbers[1:len(numbers):2]

numbers[5:10] = [0] * len(numbers[5:10])

numbers

numbers[5:] = []

numbers


numbers[:] = []

numbers




##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 5.6 snippets

# Deleting the Element at a Specific List Index
numbers = list(range(0, 10))

numbers

del numbers[-1]

numbers

# Deleting a Slice from a List
del numbers[0:2]

numbers

del numbers[::2]

numbers

# Deleting a Slice Representing the Entire List
del numbers[:]

numbers

# Deleting a Variable from the Current Session
del numbers

numbers

# Cleaning up at end of snippet
get_ipython().magic('reset -f')
get_ipython().magic('clear')

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 5.6 Self Check snippets

# Exercise 2
numbers = list(range(1, 16))

numbers

del numbers[0:4]

numbers

del numbers[::2]

numbers




##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 5.7 snippets

# Passing an Entire List to a Function
def modify_elements(items):
    """"Multiplies all element values in items by 2."""
    for i in range(len(items)):
        items[i] *= 2

numbers = [10, 3, 7, 1, 9]

modify_elements(numbers)

numbers

# Passing a Tuple to a Function
numbers_tuple = (10, 20, 30)

numbers_tuple

modify_elements(numbers_tuple)

# Cleaning up at end of snippet
get_ipython().magic('reset -f')
get_ipython().magic('clear')


##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 5.8 snippets

# Sorting a List in Ascending Order
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

numbers.sort()

numbers

# Sorting a List in Descending Order
numbers.sort(reverse=True)

numbers

# Built-In Function sorted
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

ascending_numbers = sorted(numbers)

ascending_numbers

numbers

letters = 'fadgchjebi'

ascending_letters = sorted(letters)

ascending_letters

letters

colors = ('red', 'orange', 'yellow', 'green', 'blue')

ascending_colors = sorted(colors)

ascending_colors

colors

# Cleaning up at end of snippet
get_ipython().magic('reset -f')
get_ipython().magic('clear')

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 5.8 Self Check snippets

# Exercise 3
foods = ['Cookies', 'pizza', 'Grapes', 'apples', 'steak', 'Bacon']

foods.sort()

foods





##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 5.9 snippets
# 5.9 Searching Sequences

# List Method index
numbers = [3, 7, 1, 4, 2, 8, 5, 6]

numbers.index(5)

# Specifying the Starting Index of a Search
numbers *= 2

numbers

numbers.index(5, 7)

# Specifying the Starting and Ending Indices of a Search
numbers.index(7, 0, 4)

# Operators in and not in
1000 in numbers

5 in numbers

1000 not in numbers

5 not in numbers

# Using Operator in to Prevent a ValueError
key = 1000

if key in numbers:
    print(f'found {key} at index {numbers.index(search_key)}')
else:
    print(f'{key} not found')
    
# Cleaning up at end of snippet
get_ipython().magic('reset -f')
get_ipython().magic('clear')

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 5.9 Self Checksnippets

# Exercise 3
numbers = [67, 12, 46, 43, 13]

numbers.index(43)

if 44 in numbers:
    print(f'Found 44 at index: {numbers.index(44)}')
else:
    print('44 not found')
    


##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 5.10 snippets

color_names = ['orange', 'yellow', 'green']

# Inserting an Element at a Specific List Index
color_names.insert(0, 'red')

color_names

# Adding an Element to the End of a List
color_names.append('blue')

color_names

# Adding All the Elements of a Sequence to the End of a List
color_names.extend(['indigo', 'violet'])

color_names

sample_list = []

s = 'abc'

sample_list.extend(s)

sample_list

t = (1, 2, 3)

sample_list.extend(t)

sample_list

sample_list.extend((4, 5, 6))  # note the extra parentheses

sample_list

# Removing the First Occurrence of an Element in a List 
color_names.remove('green')

color_names


# Emptying a List
color_names.clear()

color_names

# Counting the Number of Occurrences of an Item
responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 
             1, 4, 3, 3, 3, 2, 3, 3, 2, 2]

for i in range(1, 6):
    print(f'{i} appears {responses.count(i)} times in responses')
    
# Reversing a List’s Elements
color_names = ['red', 'orange', 'yellow', 'green', 'blue']

color_names.reverse()

color_names

# Copying a List
copied_list = color_names.copy()

copied_list

# Cleaning up at end of snippet
get_ipython().magic('reset -f')
get_ipython().magic('clear')


##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 5.10 Self Check snippets

rainbow = ['green', 'orange', 'violet']

rainbow.insert(rainbow.index('violet'), 'red')

rainbow

rainbow.append('yellow')

rainbow

rainbow.reverse()

rainbow

rainbow.remove('orange')

rainbow


##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 5.11 snippets

# 5.11 Simulating Stacks with Lists 
stack = []

stack.append('red')

stack

stack.append('green')

stack

stack.pop()

stack

stack.pop()

stack

stack.pop()

# Cleaning up at end of snippet
get_ipython().magic('reset -f')
get_ipython().magic('clear')

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 5.12 snippets

list1 = []

for item in range(1, 6):
    list1.append(item)
    
list1

# Using a List Comprehension to Create a List of Integers
list2 = [item for item in range(1, 6)]

list2

# Mapping: Performing Operations in a List Comprehension’s Expression
list3 = [item ** 3 for item in range(1, 6)]

list3

# Filtering: List Comprehensions with if Clauses 
list4 = [item for item in range(1, 11) if item % 2 == 0]

list4


# List Comprehension That Processes Another List’s Elements 
colors = ['red', 'orange', 'yellow', 'green', 'blue']

colors2 = [item.upper() for item in colors]

colors2

colors

# Cleaning up at end of snippet
get_ipython().magic('reset -f')
get_ipython().magic('clear')

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 5.12 Self Check snippets

# Exercise 3
cubes = [(x, x ** 3) for x in range(1, 6)]

cubes

# Exercise 4
multiples = [x for x in range(3, 30, 3)]

multiples


##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 5.13 snippets
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

for value in (x ** 2 for x in numbers if x % 2 != 0):
    print(value, end='  ')

squares_of_odds = (x ** 2 for x in numbers if x % 2 != 0)

squares_of_odds 

# Cleaning up at end of snippet
get_ipython().magic('reset -f')
get_ipython().magic('clear')


##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 5.13 Self Check snippets

# Exercise 2
list(x ** 3 for x in [10, 3, 7, 1, 9, 4, 2] if x % 2 == 0)

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 5.14 snippets

# Filtering a Sequence’s Values with the Built-In filter Function
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

def is_odd(x):
    """Returns True only if x is odd."""
    return x % 2 != 0

list(filter(is_odd, numbers))

[item for item in numbers if is_odd(item)]

# Using a lambda Rather than a Function 
list(filter(lambda x: x % 2 != 0, numbers))

# Mapping a Sequence’s Values to New Values
numbers

list(map(lambda x: x ** 2, numbers))

[item ** 2 for item in numbers]

# Combining filter and map
list(map(lambda x: x ** 2, 
         filter(lambda x: x % 2 != 0, numbers)))

[x ** 2 for x in numbers if x % 2 != 0]

# Cleaning up at end of snippet
get_ipython().magic('reset -f')
get_ipython().magic('clear')

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 5.14 Self Check snippets

# Exercise 3
numbers = list(range(1, 16))

numbers

list(filter(lambda x: x % 2 == 0, numbers))

list(map(lambda x: x ** 2, numbers))

list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))

# Exercise 4
fahrenheit = [41, 32, 212]

list(map(lambda x: (x, (x - 32) * 5 / 9), fahrenheit)) 



##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 5.15 snippets

# Finding the Minimum and Maximum Values Using a Key Function
'Red' < 'orange'

ord('R')

ord('o')

colors = ['Red', 'orange', 'Yellow', 'green', 'Blue']

min(colors, key=lambda s: s.lower())

max(colors, key=lambda s: s.lower())

# Iterating Backwards Through a Sequence
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

reversed_numbers = [item ** 2 for item in reversed(numbers)]

reversed_numbers

# Combining Iterables into Tuples of Corresponding Elements
names = ['Bob', 'Sue', 'Amanda']

grade_point_averages = [3.5, 4.0, 3.75] 

for name, gpa in zip(names, grade_point_averages):
    print(f'Name={name}; GPA={gpa}')

# Cleaning up at end of snippet
get_ipython().magic('reset -f')
get_ipython().magic('clear')
##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 5.15 Self Check snippets

# Exercise 3
foods = ['Cookies', 'pizza', 'Grapes', 
         'apples', 'steak', 'Bacon']

min(foods)

min(foods, key=lambda s: s.lower())

# Exercise 4
[(a + b) for a, b in zip([10, 20, 30], [1, 2, 3])]



##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 5.16 snippets

# Creating a Two-Dimensional List
a = [[77, 68, 86, 73], [96, 87, 89, 81], [70, 90, 86, 81]]

# Illustrating a Two-Dimensional List

# Identifying the Elements in a Two-Dimensional List
for row in a:
    for item in row:
        print(item, end=' ')
    print()

# How the Nested Loops Execute
for i, row in enumerate(a):
    for j, item in enumerate(row):
        print(f'a[{i}][{j}]={item} ', end=' ')
    print()

# Cleaning up at end of snippet
get_ipython().magic('reset -f')
get_ipython().magic('clear')

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 5.16 Self Check snippets

# Exercise 4
t = [[10, 7, 3], [20, 4, 17]]

total = 0

items = 0

for row in t:
    for item in row:
        total += item
        items += 1     

total / items

total = 0

items = 0

for row in t:
    total += sum(row)
    items += len(row)

total / items



##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 5.17 snippets

# 5.17.1 Sample Graphs for 600, 60,000 and 6,000,000 Die Rolls

# 5.17.2 Visualizing Die-Roll Frequencies and Percentages

# Launching IPython for Interactive Matplotlib Development


# Importing the Libraries
import matplotlib.pyplot as plt

import numpy as np

import random

import seaborn as sns

# Rolling the Die and Calculating Die Frequencies
rolls = [random.randrange(1, 7) for i in range(600)]

values, frequencies = np.unique(rolls, return_counts=True)

# Creating the Initial Bar Plot
title = f'Rolling a Six-Sided Die {len(rolls):,} Times'

sns.set_style('whitegrid')

axes = sns.barplot(x=values, y=frequencies, palette='bright')

# Setting the Window Title and Labeling the x- and y-Axes
axes.set_title(title)

axes.set(xlabel='Die Value', ylabel='Frequency')  

# Finalizing the Bar Plot
axes.set_ylim(top=max(frequencies) * 1.10)

for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2.0  
    text_y = bar.get_height() 
    text = f'{frequency:,}\n{frequency / len(rolls):.3%}'
    axes.text(text_x, text_y, text, 
              fontsize=11, ha='center', va='bottom')
              
# Rolling Again and Updating the Bar Plot—Introducing IPython Magics
plt.cla()

%recall 5

rolls = [random.randrange(1, 7) for i in range(600)]

rolls = [random.randrange(1, 7) for i in range(60000)]

%recall 6-13

values, frequencies = np.unique(rolls, return_counts=True)
title = f'Rolling a Six-Sided Die {len(rolls):,} Times'
sns.set_style('whitegrid')
axes = sns.barplot(x=values, y=frequencies, palette='bright')
axes.set_title(title)
axes.set(xlabel='Die Value', ylabel='Frequency')  
axes.set_ylim(top=max(frequencies) * 1.10)
for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2.0  
    text_y = bar.get_height() 
    text = f'{frequency:,}\n{frequency / len(rolls):.3%}'
    axes.text(text_x, text_y, text, 
              fontsize=11, ha='center', va='bottom')
              
# Saving Snippets to a File with the %save Magic 
%save RollDie.py 1-13

# Cleaning up at end of snippet
get_ipython().magic('reset -f')
get_ipython().magic('clear')
 

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 5.17.2 Self Check snippets

# Exercise 5
plt.cla()

%recall 5

rolls = [random.randrange(1, 7) for i in range(6000000)]

%recall 6-13

values, frequencies = np.unique(rolls, return_counts=True)
title = f'Rolling a Six-Sided Die {len(rolls):,} Times'
sns.set_style('whitegrid')
axes = sns.barplot(values, frequencies, palette='bright')
axes.set_title(title)
axes.set(xlabel='Die Value', ylabel='Frequency')  
axes.set_ylim(top=max(frequencies) * 1.10)
for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2.0  
    text_y = bar.get_height() 
    text = f'{frequency:,}\n{frequency / len(rolls):.3%}'
    axes.text(text_x, text_y, text, 
              fontsize=11, ha='center', va='bottom')
              

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
