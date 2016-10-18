# -*- coding: utf-8 -*-
"""
calculate_seasonal_temps.py

DESCRIBE WHAT CODE DOES HERE

@author: YOUR NAME - DATE
"""

# Import NumPy
import numpy as np

# Step 1: Load data file
#TODO: Fill in parameters to load data file
data = np.loadtxt()

# Step 2: Calculate mean and standard deviation
#TODO: Assign  mean and standard deviations of the temperatures to mean and std
mean = 
std = 

# Step 3: Clean up data file
# Part 1: Flag bad value lines
badvalues=[]
#TODO: Fill in array to loop through to find bad values
for i in range(len( )):
    #TODO: Add if statements to check if a given temperature is outside of
    #      mean plus or minus 4 * std
    if :
        #TODO: Append index value of temperature if outside mean +/- 4 * std
        badvalues.append( )

# Part 2: Remove bad values
#
#TODO: Reverse list of badvalues

# Loop over badvalues and delete them
#TODO: Fill in list to loop over to delete bad values
for i in range(len( )):
    # The line below works for removing "bad" values
    data = np.delete(data, badvalues[i], 0)

# Step 5: Loop over all years and calculate seasonal averages, append to lists
winterOut=[]
summerOut=[]

# Loop over all years 1927-2015
#TODO: Fill in years for range
for year in range( ):
    # Create year values that can be compared to numerical values for the dates
    lastYear = (year - 1) * 10000
    thisYear = year * 10000
    
    # Create Boolean (True/False) arrays for values in desired winter date ranges
    # XXX should be the dates array from the data file
    #TODO: Replace XXX
    winterMin = XXX >= lastYear + 1201
    winterMax = XXX <= thisYear + 229

    # Use the logical and (&) operator - Only values that are true in both arrays will be
    # True in winterVals
    winterVals = (winterMin & winterMax)

    # Create Boolean (True/False) arrays for values in desired summer date ranges
    # XXX should be the dates array from the data file
    #TODO: Replace XXX
    summerMin = XXX >= 
    summerMax = XXX <= 

    # Use the logical and (&) operator - Only values that are true in both arrays will be
    # True in summerVals
    summerVals = (summerMin & summerMax)

    # Extract values summer and winter values in the season ranges from full data array
    # XXX should be a Boolean array, YYY should contain temperature data
    #TODO: Replace XXX, YYY
    winterTemps = np.extract(XXX, YYY)
    summerTemps = np.extract(XXX, YYY)
    
    # Append year and seasonal average temperatures to summer and winter lists
    #TODO: Fill in values to be appended to list
    winterOut.append([ , ])
    summerOut.append([ , ])

# Step 6: Save data files
#
#TODO: Add output filenames and format information here
np.savetxt("", winterOut, fmt='', delimiter=',')
np.savetxt("", summerOut, fmt='', delimiter=',')
