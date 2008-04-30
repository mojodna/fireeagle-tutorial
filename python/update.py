#!/usr/bin/env python

from os import path
import pickle
from sys import argv
from fireeagle_api import FireEagle

import settings

# Die if we haven't authorized
if not path.exists( settings.AUTH_FILE ):
    print 'You need to authorize with Fire Eagle by running authorize.py.'
    exit()

def pause( prompt='hit to continue' ):
    return raw_input( '\n' + prompt + '\n' )

fe = FireEagle( settings.CONSUMER_KEY, settings.CONSUMER_SECRET )

# Load the access token
token_file = open( settings.AUTH_FILE, 'r' )
try:
    access_token = pickle.load( token_file )
finally:
    token_file.close()

# Disambiguate the input to a place_id that Fire Eagle can understand
lookup_results = fe.lookup( access_token, q=argv[1] )

# If we have multiple locations, get the user to confirm. Otherwise, go ahead.
if 1 < len(lookup_results):
    for i, location in enumerate( lookup_results ):
        print '%(#)d: %(name)s' % { '#': i, 'name': location['name'] }
    
    chosen_location = pause( "Pick the correct location:" )
    update_location = lookup_results[int( chosen_location )]
elif 1 == len(lookup_results):
    update_location = lookup_results[0]
else:
    print "Fire Eagle couldn't find anywhere matching that string, sorry."
    exit()

# Perform the update
fe.update( access_token, woeid=update_location['woeid'] )