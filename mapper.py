#!/usr/bin/python
"""mapper.py"""
import sys
# input comes from STDIN (standard input)

crime_words=["crime","assault","bribe","burglar","abuse","drug","fraud","homicid","kidnap","piracy","rape","robb","smuggl","terror","theft"]
cities=["city.delhi","city.chennai","city.mumbai","city.kolkata"]
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    sent_split = line.split(",")
    year=sent_split[0][:4]
    category=sent_split[1]
    headline=" ".join(sent_split[2:])
    if(category in cities):
        for i in crime_words:
            if(i in headline):
                print(year+"\t"+category.split(".")[1])#+"\t"+headline)
