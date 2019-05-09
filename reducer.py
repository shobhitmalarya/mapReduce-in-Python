#!/usr/bin/python
"""reducer.py"""

from operator import itemgetter
import sys
import matplotlib.pyplot as plt

# current_time = None
# current_count = 0
# headline = None


current_city=None
current_year=0

city_count={"delhi":0,"chennai":0,"mumbai":0,"kolkata":0}

year = []

count_delhi = []

count_chennai = []

count_mumbai = []

count_kolkata = []


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    time,crime_city = line.split('\t')

    # convert count (currently a string) to int
    try:
        time = int(time)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    if(current_year==time):
        city_count[crime_city]+=1    
    elif(current_year!=time):
        if(current_year):
            print(current_year)
            print(city_count)
            year.append(current_year)
            count_delhi.append(city_count["delhi"])
            count_chennai.append(city_count["chennai"])
            count_mumbai.append(city_count["mumbai"])
            count_kolkata.append(city_count["kolkata"])
        current_year=time
        city_count["delhi"]=0
        city_count["chennai"]=0
        city_count["mumbai"]=0
        city_count["kolkata"]=0
        
if(current_year==time):
    city_count

plt.plot(year, count_delhi, label = "delhi", color='green', linestyle='solid', marker='o', markerfacecolor='black', markersize=6)
plt.plot(year, count_chennai, label = "chennai", color='orange', linestyle='dotted', marker='^', markerfacecolor='black', markersize=6)
plt.plot(year, count_mumbai, label = "mumbai", color='red', linestyle='dashed', marker='*', markerfacecolor='black', markersize=6)
plt.plot(year, count_kolkata, label = "kolkata", color='blue', linestyle='dashdot', marker='X', markerfacecolor='black', markersize=6)

# naming the x axis 
plt.xlabel('Year') 
# naming the y axis 
plt.ylabel('Count')

plt.title('Articles on criminal activities')

plt.legend()

plt.show()
