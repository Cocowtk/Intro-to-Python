# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 04:36:43 2020

@author: Troy
"""
import numpy as np

# Concatenation of arrays

x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
np.concatenate([x, y])

# Two-dimensional arrays

z = [99, 99, 99]
print(np.concatenate([x, y, z]))

# Use np.vstack, np.hstack, or np.dstack for arrays of mixed dimensions

x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7],
                 [6, 5, 4]])

# vertically stack the arrays
np.vstack([x, grid])

# horizontally stack the arrays
y = np.array([[99],
              [99]])
np.hstack([grid, y])

# Splitting of arrays

x = [1, 2, 3, 99, 99, 3, 2, 1]
x1, x2, x3 = np.split(x, [3, 5])
print(x1, x2, x3)

grid = np.arange(16).reshape((4, 4))
grid

upper, lower = np.vsplit(grid, [2])
print(upper)
print(lower)

left, right = np.hsplit(grid, [2])
print(left)
print(right)

# Fancy Indexing

rand = np.random.RandomState(42)

x = rand.randint(100, size=10)
print(x)

[x[3], x[7], x[2]]

ind = [3, 7, 2]
x[ind]

# Fast sorting in NumPy

x = np.array([2, 1, 4, 3, 5])
np.sort(x)

# Can also sort in place
x.sort()
print(x)

# Can also use argsort to return indices:
    
x = np.array([2, 1, 4, 3, 5])
i = np.argsort(x)
print(i)
print(x)

# Partitioning arrays

x = np.array([7, 2, 3, 1, 6, 5, 4])
np.partition(x, 3)

# Example: k-Nearest Neighbors

rand = np.random.RandomState(42)
X = rand.rand(10, 2)
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn; seaborn.set() # Plot styling
plt.scatter(X[:, 0], X[:, 1], s=100);

dist_sq = np.sum((X[:, np.newaxis, :] - X[np.newaxis, :, :]) ** 2, axis=-1)

# for each pair of points, compute differences in their coordinates
differences = X[:, np.newaxis, :] - X[np.newaxis, :, :]
differences.shape

# square the coordinate differences
sq_differences = differences ** 2
sq_differences.shape

# sum the coordinate differences to get the squared distance
dist_sq = sq_differences.sum(-1)
dist_sq.shape

dist_sq.diagonal()

nearest = np.argsort(dist_sq, axis=1)
print(nearest)

K = 2
nearest_partition = np.argpartition(dist_sq, K + 1, axis=1)

plt.scatter(X[:, 0], X[:, 1], s=100)

# draw lines from each point to its two nearest neighbors
K = 2

for i in range(X.shape[0]):
    for j in nearest_partition[i, :K+1]:
        # plot a line from X[i] to X[j]
        # use some zip magic to make it happen:
        plt.plot(*zip(X[j], X[i]), color='black')

# Structured Arrays and Record Arrays

name = ['Alice', 'Bob', 'Cathy', 'Doug']
age = [25, 45, 37, 19]
weight = [55.0, 85.5, 68.0, 61.5]

# Use a compound data type for structured arrays
data = np.zeros(4, dtype={'names':('name', 'age', 'weight'),
                          'formats':('U10', 'i4', 'f8')})
print(data.dtype)

data['name'] = name
data['age'] = age
data['weight'] = weight
print(data)

# Get all names
data['name']

# Get first row of data
data[0]

# Get the name from the last row
data[-1]['name']

# Get names where age is under 30
data[data['age'] < 30]['name']
