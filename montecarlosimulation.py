#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 7 15:09:04 2022

@author: toghrulnasirli
"""

# Importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Porosity Statistics (fraction)
porosity_mean = 0.163906  # Mean porosity
porosity_std = 0.021390084  # Standard deviation of porosity
porosity_dist = []  # List to store porosity distribution

# Saturation Statistics (fraction)
saturation_mean = 0.39338  # Mean water saturation
saturation_std = 0.235478469  # Standard deviation of water saturation
min_sat = 0.1284  # Minimum water saturation
max_sat = 0.6256  # Maximum water saturation
sat_dist = []  # List to store water saturation distribution

# Area Statistics (acres)
area_mean = 715.29025  # Mean area
min_area = 205.339  # Minimum area
max_area = 1890.78  # Maximum area
area_dist = []  # List to store area distribution

# Thickness Statistics (feet)
thickness_mean = 99.08016  # Mean thickness
min_thickness = 68.8968  # Minimum thickness
max_thickness = 121.3896  # Maximum thickness
thickness_dist = []  # List to store thickness distribution

# Net-to-Gross Ratio and Oil Formation Volume Factor
ng = 0.87  # Net-to-Gross Ratio
oil_fvf = 1.065  # Oil Formation Volume Factor

# Define the function to calculate Original Oil in Place (OOIP)
def OOIP(porosity, saturation, area, thickness, n_g, fvf):
    oil_in_place = 7758.3673 * porosity * (1 - saturation) * area * thickness * n_g * (1 / fvf)
    return oil_in_place

oil_dist = []  # List to store OOIP distribution

# Generating random data for porosity, water saturation, area, and thickness
for i in range(1000000):
    porosity = np.random.normal(porosity_mean, porosity_std)
    porosity_dist.append(porosity)
    water_sat = np.random.normal(saturation_mean, saturation_std)
    sat_dist.append(water_sat)
    area = np.random.triangular(min_area, area_mean, max_area)
    area_dist.append(area)
    thickness = np.random.triangular(min_thickness, thickness_mean, max_thickness)
    thickness_dist.append(thickness)
    oil_in_bbl = OOIP(porosity, water_sat, area, thickness, ng, oil_fvf)
    oil_dist.append(oil_in_bbl)

# Plotting histogram of OOIP distribution
plt.hist(oil_dist, density=True, bins=5000)  # density=False would make counts
plt.ylim(0, 16 * 10 ** -9)
plt.xlim(0, 2.5 * 10 ** 8)
plt.ylabel('Probability Density')
plt.xlabel('OOIP (bbl)')
plt.title("Distribution of OOIP")
plt.show()

# Sorting the OOIP data
data_sorted = np.sort(oil_dist)

# Calculating the cumulative density function
p = 1. * np.arange(len(oil_dist)) / (len(oil_dist) - 1)

# Plotting the cumulative density function
fig = plt.figure(figsize=(8, 6))  # Adjust the figure size as needed
ax1 = fig.add_subplot(122)
ax1.plot(data_sorted, p)
ax1.set_xlim(0, 4 * 10 ** 8)
ax1.set_ylim(0, 1)
ax1.set_xlabel('OOIP (bbl)')
ax1.set_ylabel('Probability')
ax1.set_title("Cumulative Density Function")
plt.tight_layout()  # Adjust subplot parameters to give specified padding
plt.show()

# Plotting histograms for porosity, water saturation, and thickness distributions
plt.hist(porosity_dist, density=True, bins=5000)
plt.ylabel("Probability Density")
plt.xlabel("Porosity (%)")
plt.title("Porosity Distribution")
plt.show()

plt.hist(sat_dist, density=True, bins=5000)
plt.ylabel("Probability Density")
plt.xlabel("Water Saturation (%)")
plt.title("Water Saturation Distribution")
plt.show()

plt.hist(thickness_dist, density=True, bins=5000)
plt.ylabel("Probability Density")
plt.xlabel("Thickness (ft)")
plt.title("Thickness Distribution")
plt.show()

# Calculating percentiles and plotting them against cumulative percent greater than or equal to
percentiles = [i for i in range(100)]
percentiles_sorted = percentiles[:1:-1]
probability_list = []
for i in percentiles_sorted:
    p = np.percentile(oil_dist, i)
    probability_list.append(p)

print("Sorted Percentiles: ", percentiles_sorted)
print("Listed Probabilities: ", probability_list)

plt.plot(probability_list, percentiles[1:-1:])
plt.xlabel("OOIP (BBL)")
plt.ylabel("Cumulative Percent Greater than or Equal To")
plt.show()

print("Percentiles: ", percentiles[1:-1:])
