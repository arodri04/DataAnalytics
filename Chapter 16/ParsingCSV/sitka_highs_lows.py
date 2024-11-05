############################################
# Software Req Doc: CSV Parsing
# Release Date: 11/15/24
# Sam Rodriguez
# Description: Python program to read CSV data
# and print out results to a graph. 
############################################

import csv
from matplotlib import pyplot as plt
from datetime import datetime

#variable where csv is stored
filename = 'data\\sitka_weather_2018_simple.csv'


with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    #Get dates and high tempurature
    highs, dates, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            
            high = int(row[5])
            low = int(row[6])


        except ValueError:
            print(current_date, "Missing data")

        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)

    #plotting data
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates, highs, c="red", alpha=0.5)
    plt.plot(dates, lows, c="blue", alpha=0.5)
    #Shading in between
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    #Format plot
    plt.title("Daily high and low tempuratures, 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()