__author__ = 'Owner'
import datetime

def getTime():
    date = str(datetime.datetime.now())[:-7]
    dateTime = date.split(" ")

    return dateTime

