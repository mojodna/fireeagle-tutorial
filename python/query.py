#!/usr/bin/env python

from os import path
import pickle
from sys import argv
from fireeagle_api import FireEagle

import settings

# Die if we haven't authorized
if not path.exists( settings.AUTH_FILE ):
    print 'You need to authorize with Fire Eagleby running authorize.py.'
    exit()

fe = FireEagle( settings.CONSUMER_KEY, settings.CONSUMER_SECRET )

# Load the access token
token_file = open( settings.AUTH_FILE, 'r' )
try:
    access_token = pickle.load( token_file )
finally:
    token_file.close()

# Get the heirarchy
# NOTE: We're hacking past the user's token here to get straight to 
# the meat of location
user_heirarchy = fe.user( access_token )[0]['location']

# Do some list jiggering to format the locations into a pretty state
user_heirarchy_names = [
        location['level_name'] + ': ' + location['name']
        for location in user_heirarchy
    ]
print "\n".join( user_heirarchy_names )