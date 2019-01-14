# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 09:18:27 2019

@author: winkl
"""

import sqlite3
import requests
#import phonebook2

###---connecting to database---###

###---creating a database and cursor---###
conn = sqlite3.connect('phonebook2.db')
c = conn.cursor()

###---looking up Postcodes from person table---###

postcode_list = []

endpoint_postcode = "https://api.postcodes.io/postcodes/"

def read_postcode_person_phonebook():
    c.execute('SELECT * FROM people_table ')
    for row in c.fetchall():
        postcode_list.append(row[5])
        print(postcode_list)
     
read_postcode_person_phonebook()        

print('----------------------------------------')

def looping_through_postcodes_longitude():
    for i in range(len(postcode_list)):
        postcode_response = requests.get(endpoint_postcode + postcode_list[i])
        data_postcode = postcode_response.json()
        if data_postcode['status'] == 200:
            longitude = data_postcode['result'] ['longitude']
            print(longitude)
        else:
            pass

looping_through_postcodes_longitude()


def looping_through_postcodes_latitude():
    for i in range(len(postcode_list)):
        postcode_response = requests.get(endpoint_postcode + postcode_list[i])
        data_postcode = postcode_response.json()
        if data_postcode['status'] == 200:
            latitude = data_postcode['result'] ['latitude']
            print(latitude)
        else:
            pass

looping_through_postcodes_latitude()



   