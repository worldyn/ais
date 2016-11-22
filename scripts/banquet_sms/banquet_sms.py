# -*- coding: utf-8 -*-
'''
# *WARNING* Be sure that the encoding of this file is UTF-8.
# Lots of terminals run in latin-1 for example,
# so if you edit with vim and save, it will be latin-1 again.
'''
import sys
import csv
import urllib
import requests

def send_sms(phone_number, message):

    auth = (
	'ue222c7eb24ed71b2b889ed809cda74d3',
	'58434E29C22A17B1EE2513000FD45657'
	)

    fields = {
	'from': 'Armada',
	'to': phone_number,
	'message': message
	}

    response = requests.post(
	"https://api.46elks.com/a1/SMS",
	data=fields,
	auth=auth
	)

    return response

def make_message_for(attendee):
    name=attendee['first_name']
    message = "Welcome "+attendee['first_name']+", to the grand banquet of THS Armada! You Are seated at table "+attendee['table_name']+", seat "+attendee['seat_number']+". The doors will open 18:00 at Annexet, globen."
    return message

def main():
    attendees=[]
    error_file = open('errors.txt', 'w')
    number_of_errors = 0
    number_of_readins = 0


    with open(str(sys.argv[1]), 'rb') as csvfile:
        # Read the CSV as a python dict
        banquet_attendence = csv.DictReader(csvfile, delimiter=',')
        for attendee in banquet_attendence:
            # This simply strips out everything that is not a number (1234567890)
            phone_number="".join(_ for _ in attendee['phone_number'] if _ in "1234567890")

            if phone_number.startswith("07"):
                phone_number=phone_number[1:]

            if phone_number.startswith("46"):
                phone_number=phone_number[2:]

            phone_number="46"+phone_number
            send_to_this=1
            if len(phone_number)!=11:
                error_file.write("Phone number error: "+phone_number+"("+attendee['phone_number']+"), ")
                send_to_this=0

            if attendee['table_name']=="" or attendee['seat_number']=="":
                error_file.write("Placement error, ")
                send_to_this=0

            if send_to_this:
                #touple will be (phone_number, message)
                attendees.append( (phone_number, make_message_for(attendee)) )
                number_of_readins += 1
            else:
                error_file.write("Error with "+attendee['first_name']+" "+attendee['last_name']+"\n")
                number_of_errors += 1

    print("\nWe had %d errors, but %d attendees were read in correctly, see errors.txt for more information.\n"%(number_of_errors, number_of_readins))
    print("A total of %d text messages will be sent out. The price will be %.2f SEK" % (len(attendees), len(attendees)*0.35 ))
    print("Would you like to continue? (yes/no)") 
    error_file.close()
    choice = raw_input().lower()
    
    if choice=="yes":
        for attendee in attendees:
            try:
                number=attendee[0]
                message=attendee[1]
                print("To: %s\n%s\n" % (number, message) )
                send_sms(number, message)
            except Exception as inst:
                print(type(inst))
                print(inst)
    else:
        print("Operation canceled.\nNo texts have been sent, you may fix any errors and then try again.")

main()
