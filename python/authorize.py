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
# Alternately, include a callback url when getting a request token
# request_token = fe.request_token( oauth_callback="http://example.com/cb")

## Step 2 - Ask the user to authorize the application, using that request token

auth_url      = fe.authorize( request_token )
print 'Please authorize this application:'
print auth_url
oauth_verifier = pause( 'Please enter the verification code:' )

## Step 3 - Convert the request token into an access token, using the verification code that was provided

access_token  = fe.access_token( token=request_token, oauth_verifier=oauth_verifier )

## (Step 4 - save the access token)

token_file = open( settings.AUTH_FILE, 'w' )
try:
    pickle.dump( access_token, token_file )
finally:
    token_file.close()