#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 7 15:09:04 2022

@author: toghrulnasirli
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

#Porosity Statistics(fraction)
porosity_mean = 0.163906
porosity_std = 0.021390084
porosity_dist = []
#Saturation Statistics(fraction)
saturation_mean = 0.39338
saturation_std = 0.235478469
min_sat = 0.1284
max_sat = 0.6256
sat_dist = []
#Area Statistics (acres)
area_mean = 715.29025
min_area = 205.339
max_area = 1890.78
area_dist = []
#Thickness Statistics (feets)
thickness_mean = 99.08016
min_thickness = 68.8968
max_thickness = 121.3896
thickness_dist = []
#Net-to-Gross Ratio and FVF
ng = 0.87
oil_fvf = 1.065

#Define the OOIP function

def OOIP(porosity,saturation,area,thickness,n_g,fvf):
    oil_in_place = 7758.3673*porosity*(1-saturation)*area*thickness*n_g*(1/fvf)
    return oil_in_place

oil_dist = []

for i in range(1000000):
    porosity = np.random.normal(porosity_mean,porosity_std)
    porosity_dist.append(porosity)
    water_sat = np.random.normal(saturation_mean,saturation_std)
    sat_dist.append(water_sat)
    area = np.random.triangular(min_area,area_mean,max_area)
    area_dist.append(area)
    thickness = np.random.triangular(min_thickness,thickness_mean,max_thickness)
    thickness_dist.append(thickness)
    oil_in_bbl = OOIP(porosity,water_sat,area,thickness,ng,oil_fvf)
    oil_dist.append(oil_in_bbl)
    
plt.hist(oil_dist, density=True, bins=5000)  # density=False would make counts
plt.ylim(0,16*10**-9)
plt.xlim(0,2.5*10**8 )
plt.ylabel('Probability Density')
plt.xlabel('OOIP(bbl)');
plt.title("Distribution of OOIP")
plt.show()

# create some randomly distributed data:


# sort the data:
data_sorted = np.sort(oil_dist)

# calculate the proportional values of samples
p = 1. * np.arange(len(oil_dist)) / (len(oil_dist) - 1)

# plot the sorted data:
fig = plt.figure()

ax1 = fig.add_subplot(122)
ax1.plot(data_sorted, p)
ax1.set_xlim(0, 4*10**8)
ax1.set_ylim(0, 1)
ax1.set_xlabel('$OOIP(bbl)$')
ax1.set_ylabel('$Probability$')
ax1.set_title("Cumulative Density Function")

plt.hist(porosity_dist, density = True, bins = 5000)
plt.ylabel("Probability Density")
plt.xlabel("Porosity (%)")
plt.title("Porosity Distribution")
plt.show()

plt.hist(sat_dist, density = True, bins = 5000)
plt.ylabel("Probability Density")
plt.xlabel("Water Saturation (%)")
plt.title("Water Saturation Distribution")
plt.show()

plt.hist(thickness_dist, density = True, bins = 5000)
plt.ylabel("Probability Density")
plt.xlabel("Thickness (ft)")
plt.title("Thickness Distribution")

plt.show()

percentiles = [i for i in range(100)]
percentiles_sorted = percentiles[:1:-1]
probability_list = []
for i in percentiles_sorted:
    p = np.percentile(oil_dist,i)
    probability_list.append(p)


print(percentiles_sorted)
print(probability_list)

plt.plot(probability_list,percentiles[1:-1:])
plt.xlabel("OOIP (BBL)")
plt.ylabel("Cumulative Percent Greater than or Equal To")


print(probability_list)
print(percentiles[1:-1:])
