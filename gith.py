#script to give calculate the amount of contributions merged in Gerrit during a given period of time.
#uncopyrighted -Marv
#intended to be as minimal as possible .
import json
import requests
import time


Mergedcont=0;
user_name= str(input("Please enter the Gerrit username: "))
start_date=(input('Please enter the start date in the format YYYY-MM-DD: '))
end_date=(input('Please enter the end date in the format YYYY-MM-DD: '))

# Begin Gerrit API request
web = 'https://gerrit.wikimedia.org/r/changes/?q=owner:'
link = web + user_name +'+status:merged' + '+after:' + start_date +'+before:' + end_date
r = requests.get(link)
item_dict = r.text
#account for unnessecary header present in the json response. -TODO -file a bug report as soon as possible
item_dict = item_dict.replace(")]}'", '', 1)
database = json.loads(item_dict)

for i in database:
#search response for merged contribution.
    if (i['status']=="MERGED"):
        Mergedcont = Mergedcont+1

print(str(user_name) +  " Contributions Report")
print("MERGED Patches: " + str(Mergedcont))
#P.S some minutes was spent gaining inspiration from the original AWMD tool originally developed by -
# - D3rr1ck & AfricanHope
