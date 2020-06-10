#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Dark Sky Assignment
# Marshall Bradley
# Orange Cohort
# MSA Fall 1


# Import important packages and set file location

import sys
import csv

sys.path.insert(1, '/Users/marshallbradley/Desktop/MSA Notes/Fall I/Python')

from forecastiopy import *
from statistics import mean    

# Start CSV File with header row

with open("mbradley_homework1.csv", mode= 'w' ) as hw1:

    writer = csv.writer(hw1, delimiter=',')
    writer.writerow(['City', 'Min 1', 'Max 1', 'Min 2', 'Max 2', 'Min 3', 'Max 3', 'Min 4', 'Max 4', 'Min 5', 'Max 5', 'Min Avg', 'Max Avg'])

    
    # Set up the city list

    loc = [          ["Anchorage, Alaska", 61.2181, -149.9003],          ["Buenos Aires, Argentina", -34.6037, -58.3816],          ["São José dos Campos, Brazil", -23.2237, -45.9009],          ["San José, Costa Rica", 9.9281, -84.0907],          ["Nanaimo, Canada", 49.1659, -123.9401],          ["Ningbo, China", 29.8683, 121.5440],           ["Giza, Egypt", 30.0131, 31.2089],           ["Mannheim, Germany", 49.4875, 8.4660],           ["Hyderabad, India", 17.3850, 78.4867],           ["Tehran, Iran", 35.6892, 51.3890],           ["Bishkek, Kyrgyzstan", 42.8746, 74.5698],           ["Riga, Latvia", 56.9496, 24.1052],           ["Quetta, Pakistan", 30.1798, 66.9750],           ["Warsaw, Poland", 52.2297, 21.0122],           ["Dhahran, Saudia Arabia", 26.2361, 50.0393],           ["Madrid, Spain", 40.4168, -3.7038],           ["Oldham, United Kingdom", 53.5409, -2.1114]          ]

    # Insert API Key for Dark Sky API
    
    api_key = 'f51acd215ae4bca2c95404b1c5f08861'

    # Create the FOR Loop that will retrieve the temperatures and create the temperature list
    
    for city in loc:
        weather = ForecastIO.ForecastIO( api_key, latitude=city[1], longitude=city[2], units = 'si')

        daily = FIODaily.FIODaily( weather )
        temperature = []
        minimum = []
        maximum = []
        
        temperature.append(city[0])
        
        # Create the FOR Loop that will append temperatures to the list and create the averages
        
        for day in range( 2, 7 ):
            val = daily.get( day )
            minimum.append( val[ 'temperatureMin' ] )
            temperature.append( val[ 'temperatureMin' ] )
            maximum.append( val[ 'temperatureMax' ] )
            temperature.append( val[ 'temperatureMax' ] )

        temperature.append( round(mean(minimum), 2) )
        temperature.append( round(mean(maximum), 2) )
        
        # Write the temperatures to the CSV File
        
        writer.writerow(temperature)
        


# In[ ]:




