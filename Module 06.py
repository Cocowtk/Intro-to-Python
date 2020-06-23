# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 14:22:57 2020

@author: Troy
"""
import pandas as pd
import numpy as np
import pickle

import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.available[:20]
plt.style.use('fivethirtyeight')

# Plotting like Matlab: pyplot tutorial

# Think of pyplot as creating layers
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

# Specifiying both y and x variables
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.ylabel('y Axis')
plt.xlabel('x Axis')
plt.show()

# Plotting multiple lines in same figure
x = np.linspace(0,10,10_000)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.ylabel('f(x)')
plt.xlabel('x')
plt.show()

# Generating legend
x = np.linspace(0,10,10_000)
plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.cos(x), label='cos(x)')
plt.ylabel('f(x)')
plt.xlabel('x')
plt.legend(loc='upper right', shadow=True, fontsize='x-large')
plt.show()

# Specifying colors
plt.plot(x, np.sin(x), label='sin(x)',color = 'purple')
plt.plot(x, np.cos(x), label='cos(x)',color='red')
plt.ylabel('f(x)')
plt.xlabel('x')
plt.legend(loc='upper right', shadow=True, fontsize='x-large')
plt.show()

# Specifying line styles
plt.plot(x, np.sin(x), label='sin(x)',color = 'purple',
         linestyle='dashed')
plt.plot(x, np.cos(x), label='cos(x)',color='red',
         linestyle='dashdot')
plt.ylabel('f(x)')
plt.xlabel('x')
plt.legend(loc='upper right', shadow=True, fontsize='x-large')
plt.show()

# Quick formatting the style of your plot
plt.plot(x, np.sin(x), 'm-.', 
         label='sin(x)')
plt.plot(x, np.cos(x), 'g--',
         label='cos(x)')
plt.ylabel('f(x)')
plt.xlabel('x')
plt.legend(loc='upper right', shadow=True, fontsize='x-large')
plt.show()

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

# See format strings at https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot

# Specifying axis limits
plt.plot(x, np.sin(x), 'm-.', 
         label='sin(x)')
plt.plot(x, np.cos(x), 'g--',
         label='cos(x)')
plt.ylabel('f(x)')
plt.xlabel('x')
plt.axis([0,6,-.5,.5])
plt.legend(loc='upper right', shadow=True, fontsize='x-large')
plt.show()

# Using our Yellow Taxicab data

# To disable "SettingWithCopyWarning..."
pd.options.mode.chained_assignment = None  # default='warn'

# Reading the data
file = open('test', 'rb')

YT = pickle.load(file)
# close the file
file.close()

# Verifying that pickle kept the data types unchanged
YT

YT.dtypes

# First attempt at a plot
plt.plot(YT['total_amount'],YT['trip_distance'])
plt.ylabel('total_amount')
plt.xlabel('trip_distance')
plt.show()


# What if we use fare_amount instead of total_amount?
plt.plot(YT['fare_amount'],YT['trip_distance'])
plt.ylabel('fare_amount')
plt.xlabel('trip_distance')
plt.show()

# Let's try a scatterplot instead
plt.plot(YT['fare_amount'],YT['trip_distance'],'bx')
plt.ylabel('fare_amount')
plt.xlabel('trip_distance')
plt.show()

# 538 style seems to be hiding our chart, so let's switch to classic
plt.style.use('classic')

plt.plot(YT['fare_amount'],YT['trip_distance'],'bx')
plt.ylabel('fare_amount')
plt.xlabel('trip_distance')
plt.show()

# Using plt.scatter
plt.scatter(YT['fare_amount'],YT['trip_distance'],color='red',
            marker='^')
plt.ylabel('fare_amount')
plt.xlabel('trip_distance')
plt.show()

# Using plt.scatter and adjusting axes
plt.scatter(YT['fare_amount'],YT['trip_distance'],color='red',
            marker='^')
plt.ylabel('fare_amount')
plt.xlabel('trip_distance')
plt.axis([-5,300,-1,60])
plt.show()

# Using plt.scatter with groups
YT1 = YT[YT.passenger_count == 1]
plt.scatter(YT1['fare_amount'],YT1['trip_distance'],
            color='red',marker='^',label='1')
YT2 = YT[YT.passenger_count == 2]
plt.scatter(YT2['fare_amount'],YT2['trip_distance'],
            color='blue',marker='o',label='2')
plt.ylabel('fare_amount')
plt.xlabel('trip_distance')
plt.title('Fare vs Distance by Passenger Count')
plt.legend(loc='upper right', shadow=True)
plt.axis([-5,300,-1,60])
plt.show()

# Using plt.scatter with subplots
figs,subs = plt.subplots(2,sharex=True, sharey=True)
YT1 = YT[YT.passenger_count == 1]
subs[0].scatter(YT1['fare_amount'],YT1['trip_distance'],
            color='red',marker='^',label='1')
YT2 = YT[YT.passenger_count == 2]
subs[1].scatter(YT2['fare_amount'],YT2['trip_distance'],
            color='blue',marker='^',label='2')
plt.ylabel('fare_amount')
plt.xlabel('trip_distance')
plt.axis([-5,300,-1,60])
plt.title('Fare vs Distance by Passenger Count')
plt.figlegend(
    labels=('1 Passenger', '2 Passengers'),
    loc='upper right')
plt.show()

# Showing more detail with seaborn
import seaborn as sns
g =sns.scatterplot(x='trip_distance', y='fare_amount',
                   hue='passenger_count',data=YT,
                   palette=['green','orange','brown','dodgerblue',
                            'red','magenta'], legend='full')
g.set(xscale="linear")


# Plotting histograms
plt.hist(YT['passenger_count'])
plt.show()

# Try to make it look better

plt.hist(YT['passenger_count'], bins=6, align ='mid')
plt.show()

# Let's build a histogram from scratch using numpy functions and bar chart
hist,bin_edges = np.histogram(YT['passenger_count'])
hist
bin_edges

plt.bar(bin_edges[:-1], hist, width = 0.5, color='#0504aa',alpha=0.7)
plt.xlim(min(bin_edges)-.5, max(bin_edges)+.5)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Value',fontsize=15)
plt.ylabel('Frequency',fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel('Frequency',fontsize=15)
plt.title('Passenger Counts',fontsize=15)
plt.show()

# Let's round the bin_edges to an integer.
bin_edges = np.round(bin_edges,0)
bin_edges

plt.bar(bin_edges[:-1], hist, width = 0.5, color='#0504aa',alpha=0.7)
plt.xlim(min(bin_edges)-.5, max(bin_edges)+.5)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Value',fontsize=15)
plt.ylabel('Frequency',fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel('Frequency',fontsize=15)
plt.title('Passenger Counts',fontsize=15)
plt.show()

# Creating groups for time of day

YT['starthour'] = YT['pickup'].dt.hour

YT.dtypes
YT[['pickup','starthour']].head()

def group_time_of_day(value):
    if 0 <= value <= 6:
        return '01 - Early Morning'
    elif 7 <= value <= 12:
        return '02 - Morning'
    elif 13 <= value <= 18:
        return '03 - Afternoon'
    else:
        return '04 - Evening'

YT['timegroup'] = YT['starthour'].apply(group_time_of_day)

YT[['pickup','timegroup']].head()

# Using plt.hist with subplots

figs,subs = plt.subplots(4,sharex=True, sharey=True)
YT1 = YT[YT.timegroup == '01 - Early Morning']
subs[0].hist(YT1['tip_amount'],density=True,
             color='lightcyan')
YT2 = YT[YT.timegroup == '02 - Morning']
subs[1].hist(YT2['tip_amount'],density=True,
             color='cyan')
YT3 = YT[YT.timegroup == '03 - Afternoon']
subs[2].hist(YT3['tip_amount'],density=True,
             color='deepskyblue')
YT4 = YT[YT.timegroup == '04 - Evening']
subs[3].hist(YT4['tip_amount'],density=True,
             color='dodgerblue')
plt.xlabel('Tip')
plt.figlegend(
    labels=('1-Early Morning', '2-Morning',
            '3-Afternoon', '4-Evening'),
    loc='upper right')
plt.show()

# Adding more bins and "zooming in" on typical tips

figs,subs = plt.subplots(4,sharex=True, sharey=True)
YT1 = YT[YT.timegroup == '01 - Early Morning']
subs[0].hist(YT1['tip_amount'],density=True, bins=100,
             color='lightcyan')
YT2 = YT[YT.timegroup == '02 - Morning']
subs[1].hist(YT2['tip_amount'],density=True, bins=1000,
             color='cyan')
YT3 = YT[YT.timegroup == '03 - Afternoon']
subs[2].hist(YT3['tip_amount'],density=True, bins=100,
             color='deepskyblue')
YT4 = YT[YT.timegroup == '04 - Evening']
subs[3].hist(YT4['tip_amount'],density=True, bins=100,
             color='dodgerblue')
plt.xlim(0,10)
plt.xlabel('Tip')
plt.figlegend(
    labels=('1-Early Morning', '2-Morning',
            '3-Afternoon', '4-Evening'),
    loc='upper right')
plt.show()

# Is Morning's tips' disadvantage born out by stats?
YT.groupby('timegroup')['tip_amount'].describe()
