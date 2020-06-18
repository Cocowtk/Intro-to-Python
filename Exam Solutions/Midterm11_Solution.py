# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 09:11:29 2020

@author: Troy Adair
"""
import random

# Define simple function for printing Die numbers
def print_head():
    print("Die numbers:")
    print("1 2 3 4 5")
    print("---------")

# Initialize lists for holding dice and lock choices
kept = [0,0,0,0,0]
keep = [0,0,0,0,0]
choice = 0

# Initial roll of dice and display
print_head()
for die in range(0,5):
    kept[die] = random.randrange(1,7)
    print(kept[die],end=" ")
print()

# Ask user to choose which dice to lock
print()
print("Lock Initial Rolls")
while choice != -99:
    choice = int(input("Which dice do you want to 'lock'? (-99 to continue)"))
    if choice == -99:
        break
    else:
        keep[choice-1]=1

# Re-roll any dice not locked by user and display results
print()
print("First Re-roll")
print_head()
for die in range(0,5):
    if keep[die] == 1:
        print(kept[die],end=" ")
        continue
    else:
        kept[die] = random.randrange(1,7)
        print(kept[die],end=" ")
print()

# Reset choice and list of dice to keep
choice = 0
keep = [0,0,0,0,0]

# Ask user to again choose which dice to lock
print()
print("Lock Second Rolls")
while choice != -99:
    choice = int(input("Which dice do you want to 'lock'? (-99 to continue)"))
    if choice == -99:
        break
    else:
        keep[choice-1]=1
        
# FInal re-roll of any dice not locked by user and display of results
print("Second Re-roll")
print_head()
for die in range(0,5):
    if keep[die] == 1:
        print(kept[die],end=" ")
        continue
    else:
        kept[die] = random.randrange(1,7)
        print(kept[die],end=" ")
print()