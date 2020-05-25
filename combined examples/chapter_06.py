# The following will allow for the use of .magic to clear console and variables
from IPython import get_ipython

# Section 6.2.1 snippets
country_codes = {'Finland': 'fi', 'South Africa': 'za', 
                  'Nepal': 'np'}
                 
country_codes

# Determining if a Dictionary Is Empty 
len(country_codes)

if country_codes:
    print('country_codes is not empty')
else:
    print('country_codes is empty')

country_codes.clear()

if country_codes:
    print('country_codes is not empty')
else:
    print('country_codes is empty')
    
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
# Section 6.2.1 Self Check snippets

# Exercise 3
states = {'VT': 'Vermont', 'NH': 'New Hampshire', 
          'MA': 'Massachusetts'}

states



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
# Section 6.2.2 snippets
days_per_month = {'January': 31, 'February': 28, 'March': 31}

days_per_month

for month, days in days_per_month.items():
    print(f'{month} has {days} days')

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
# Section 6.2.3 snippets

# 6.2.3 Basic Dictionary Operations
roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 100}

roman_numerals

# Accessing the Value Associated with a Key
roman_numerals['V']

# Updating the Value of an Existing Key–Value Pair
roman_numerals['X'] = 10

roman_numerals

# Adding a New Key–Value Pair
roman_numerals['L'] = 50

roman_numerals

# Removing a Key–Value Pair
del roman_numerals['III']

roman_numerals

roman_numerals.pop('X')

roman_numerals

# Attempting to Access a Nonexistent Key
roman_numerals['III']

roman_numerals.get('III')

roman_numerals.get('III', 'III not in dictionary')

roman_numerals.get('V')

# Testing Whether a Dictionary Contains a Specified Key
'V' in roman_numerals

'III' in roman_numerals

'III' not in roman_numerals

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
# Section 6.2.3 Self Check snippets

# Exercise 3
roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 100}

roman_numerals['x'] = 10

roman_numerals




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
# Section 6.2.4 snippets

months = {'January': 1, 'February': 2, 'March': 3}

for month_name in months.keys():
    print(month_name, end='  ')
    
for month_number in months.values():
    print(month_number, end='  ')
    
# Dictionary Views
months_view = months.keys()

for key in months_view:
    print(key, end='  ')

months['December'] = 12

months

for key in months_view:
    print(key, end='  ')

# Converting Dictionary Keys, Values and Key–Value Pairs to Lists
list(months.keys())

list(months.values())

list(months.items())

# Processing Keys in Sorted Order 

for month_name in sorted(months.keys()):
     print(month_name, end='  ')
     
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
# Section 6.2.4 Self Check snippets

# Exercise 3
roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5}

list(roman_numerals.keys())

list(roman_numerals.values())

list(roman_numerals.items())




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
# Section 6.2.5 snippets
country_capitals1 = {'Belgium': 'Brussels',
                     'Haiti': 'Port-au-Prince'}
                        
country_capitals2 = {'Nepal': 'Kathmandu',
                     'Uruguay': 'Montevideo'}
                        
country_capitals3 = {'Haiti': 'Port-au-Prince',
                     'Belgium': 'Brussels'}
                        
country_capitals1 == country_capitals2

country_capitals1 == country_capitals3

country_capitals1 != country_capitals2

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
# Section 6.2.6 snippets
# fig06_01.py
"""Using a dictionary to represent an instructor's grade book."""
grade_book = {            
    'Susan': [92, 85, 100], 
    'Eduardo': [83, 95, 79],
    'Azizi': [91, 89, 82],  
    'Pantipa': [97, 91, 92] 
}

all_grades_total = 0
all_grades_count = 0

for name, grades in grade_book.items():
    total = sum(grades)
    print(f'Average for {name} is {total/len(grades):.2f}')
    all_grades_total += total
    all_grades_count += len(grades)
    
print(f"Class's average is: {all_grades_total / all_grades_count:.2f}")

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
# Section 6.2.7 snippets
# fig06_02.py
"""Tokenizing a string and counting unique words."""

text = ('this is sample text with several words ' 
        'this is more sample text with some different words')

word_counts = {}

# count occurrences of each unique word
for word in text.split():
    if word in word_counts: 
        word_counts[word] += 1  # update existing key-value pair
    else:
        word_counts[word] = 1  # insert new key-value pair

print(f'{"WORD":<12}COUNT')

for word, count in sorted(word_counts.items()):
    print(f'{word:<12}{count}')

print('\nNumber of unique words:', len(word_counts))
# Python Standard Library Module ‘collections‘
from collections import Counter

text = ('this is sample text with several words '
        'this is more sample text with some different words')

counter = Counter(text.split())

for word, count in sorted(counter.items()):
    print(f'{word:<12}{count}')
    
print('Number of unique keys:', len(counter.keys()))

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
# Section 6.2.1 Self Check snippets

# Exercise 2
import random

numbers = [random.randrange(1, 6) for i in range(50)]

from collections import Counter

counter = Counter(numbers)

for value, count in sorted(counter.items()):
    print(f'{value:<4}{count}')
    



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
# Section 6.2.8 snippets
country_codes = {}

country_codes.update({'South Africa': 'za'})

country_codes

country_codes.update(Australia='ar')

country_codes

country_codes.update(Australia='au')

country_codes

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
# Section 6.2.9 snippets
months = {'January': 1, 'February': 2, 'March': 3}

months2 = {number: name for name, number in months.items()}

months2

grades = {'Sue': [98, 87, 94], 'Bob': [84, 95, 91]}

grades2 = {k: sum(v) / len(v) for k, v in grades.items()}

grades2

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
# Section 6.2.9 Self Check snippets

# Exercise 1
{number: number ** 3 for number in range(1, 6)}





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
# Section 6.3 snippets

# Creating a Set with Curly Braces
colors = {'red', 'orange', 'yellow', 'green', 'red', 'blue'}

colors

# Determining a Set’s Length
len(colors)

# Checking Whether a Value Is in a Set
'red' in colors

'purple' in colors

'purple' not in colors

# Iterating Through a Set
for color in colors:
    print(color.upper(), end=' ')

# Creating a Set with the Built-In set Function
numbers = list(range(10)) + list(range(5))

numbers

set(numbers)

set()

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
# Section 6.3 Self Check snippets

# Exercise 3
text = 'to be or not to be that is the question'

unique_words = set(text.split())

for word in sorted(unique_words):
    print(word, end='  ')
    




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
# Section 6.3.1 snippets
{1, 3, 5} == {3, 5, 1}

{1, 3, 5} != {3, 5, 1}

{1, 3, 5} < {3, 5, 1}

{1, 3, 5} < {7, 3, 5, 1}

{1, 3, 5} <= {3, 5, 1}

{1, 3} <= {3, 5, 1}

{1, 3, 5}.issubset({3, 5, 1})

{1, 2}.issubset({3, 5, 1})

{1, 3, 5} > {3, 5, 1}

{1, 3, 5, 7} > {3, 5, 1}

{1, 3, 5} >= {3, 5, 1}

{1, 3, 5} >= {3, 1}

{1, 3} >= {3, 1, 7}

{1, 3, 5}.issuperset({3, 5, 1})

{1, 3, 5}.issuperset({3, 2})

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
# Section 6.3.1 Self Check snippets

# Exercise 3
set('abc def ghi jkl mno').issuperset('hi mom')





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
# Section 6.3.2 snippets

# Union 
{1, 3, 5} | {2, 3, 4}

{1, 3, 5}.union([20, 20, 3, 40, 40])

# Intersection 
{1, 3, 5} & {2, 3, 4}

{1, 3, 5}.intersection([1, 2, 2, 3, 3, 4, 4])

# Difference 
{1, 3, 5} - {2, 3, 4}

{1, 3, 5, 7}.difference([2, 2, 3, 3, 4, 4])

# Symmetric Difference 
{1, 3, 5} ^ {2, 3, 4}

{1, 3, 5, 7}.symmetric_difference([2, 2, 3, 3, 4, 4])

# Disjoint
{1, 3, 5}.isdisjoint({2, 4, 6})

{1, 3, 5}.isdisjoint({4, 6, 1})

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
# Section 6.3.2 Self Check snippets

# Exercise 2
{10, 20, 30} - {5, 10, 15, 20}

{10, 20, 30} ^ {5, 10, 15, 20}

{10, 20, 30} | {5, 10, 15, 20}

{10, 20, 30} & {5, 10, 15, 20}





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
# Section 6.3.3 snippets

# Mutable Mathematical Set Operations
numbers = {1, 3, 5}

numbers |= {2, 3, 4}

numbers

numbers.update(range(10))

numbers

# Methods for Adding and Removing Elements
numbers.add(17)

numbers.add(3)

numbers

numbers.remove(3)

numbers

numbers.pop()

numbers

numbers.clear()

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
# Section 6.3.4 snippets
numbers = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 10]

evens = {item for item in numbers if item % 2 == 0}

evens

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
