#!/usr/bin/env ruby

require 'yaml'
require 'rubygems'
# work-around for a bug in oauth 0.2.4
require 'oauth/helper'
require 'fireeagle'

# read the configuration
config = YAML.load(open("fireeagle.yml").read)

if config.has_key?("access_token") && config.has_key?("access_token_secret")
  puts "Application has already been authorized."
  exit
end

# initialize a Fire Eagle client
client = FireEagle::Client.new(config)

## Step 1 - Get a request token

client.get_request_token

## Step 2 - Ask the user to authorize the application, using that request token

puts "Please authorize this application:"
puts " #{client.authorization_url}"
print "<waiting>"
gets

## Step 3 - Convert the request token into an access token

client.convert_to_access_token

## (Step 4 - save the access token)

config.reject! do |k,v|
  k.to_s =~ /^request_token/
end

config["access_token"] = client.access_token.token
config["access_token_secret"] = client.access_token.secret

print "Saving the access token and secret..."
open("fireeagle.yml", "w") do |f|
  f << config.to_yaml
end
puts "done."