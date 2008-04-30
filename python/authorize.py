#!/usr/bin/env python

from os import path
import pickle
from fireeagle_api import FireEagle

import settings

# Die if we've already authorized
if path.exists( settings.AUTH_FILE ):
    print "It looks like you already authorized Fire Eagle. Bye!"
    exit()

def pause( prompt='hit to continue' ):
    return raw_input( '\n' + prompt + '\n' )

fe = FireEagle( settings.CONSUMER_KEY, settings.CONSUMER_SECRET )

## Step 1 - Get a request token

request_token = fe.request_token()

## Step 2 - Ask the user to authorize the application, using that request token

auth_url      = fe.authorize( request_token )
print auth_url
pause( 'Please authorize the app at that URL' )

## Step 3 - Convert the request token into an access token

access_token  = fe.access_token( request_token )

## (Step 4 - save the access token)

token_file = open( settings.AUTH_FILE, 'w' )
try:
    pickle.dump( access_token, token_file )
finally:
    token_file.close()