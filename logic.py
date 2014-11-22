__author__ = 'Owner'
import datetime

def getTime():
    date = str(datetime.datetime.now())[:-7]
    dateTime = date.split(" ")
    dateTimeOutput = {"date":dateTime[0],
                      "time":dateTime[1]}
    return dateTimeOutput

