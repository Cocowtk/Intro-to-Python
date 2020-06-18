# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 10:12:43 2020

@author: Troy
"""
import statistics
# List=[]
def descriptive(myList):
    values=[0,0,0,0]
    titles=("Mean is:", "Median is:", "Sample SD is:", "Population SD is:")
    mean = statistics.mean(myList)
    median = statistics.median(myList)
    stdev = statistics.stdev(myList)
    pstdev = statistics.pstdev(myList)
    print(f'The mean is: {mean}')
    print(f'The median is: {median}')
    print(f'The sample standard deviation is: {stdev}')
    print(f'The population standard deviation is: {pstdev}')
    print()
    values[0]=statistics.mean(myList)
    values[1]=statistics.median(myList)
    values[2]=statistics.stdev(myList)
    values[3]=statistics.pstdev(myList)
    print("Descriptive Statistics")
    for i in range(0,4):
        print(titles[i],round(values[i],2))
    return (titles,values)

Sample=[1,2,3,4,5,6,7,8,9,10]
descriptive(Sample)
print(descriptive(Sample))
