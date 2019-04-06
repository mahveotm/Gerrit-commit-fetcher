#script to give calculate the amount of contributions merged in Gerrit during a given period of time.
#uncopyrighted -Marv
#intended to be as minimal as possible .
import json
import requests
import time
import calendar
import datetime

def getusername():

    username= str(input("Please enter the Gerrit username: "))

    if not username:
        print('Error: Please enter the username')
        getusername()

    else:
        return username



    return username




def getstartmonth():

    start_date=(input('Please enter the start date in the format YYYY-MM-DD: '))

    return start_date
    #return start_date and end_date

def getendmonth():

    end_date=(input('Please enter the end date in the format YYYY-MM-DD: '))

    return end_date


def getcommit():
    username = getusername()
    start_date = getstartmonth()
    end_date = getendmonth()
    Mergedcont=0;
    web = 'https://gerrit.wikimedia.org/r/changes/?q=owner:'
    link = web + username +'+status:merged' + '+after:' + start_date +'+before:' + end_date
    r = requests.get(link)
    item_dict = r.text
    #account for error
    item_dict = item_dict.replace(")]}'", '', 1)
    database = json.loads(item_dict)

    for i in database:
    #search response for merged contribution.
        if (i['status']=="MERGED"):
            Mergedcont = Mergedcont+1

    print(str(username) +  " Contributions Report")
    print("MERGED Patches: " + str(Mergedcont))

while True:
    getcommit()

