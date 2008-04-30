#!/usr/bin/env ruby

require 'yaml'
require 'rubygems'
# work-around for a bug in oauth 0.2.4
require 'oauth/helper'
require 'fireeagle'

config = YAML.load(open("fireeagle.yml").read)

unless config.has_key?("access_token") && config.has_key?("access_token_secret")
  puts "Application must be authorized: please run authorize.rb"
  exit
end

client = FireEagle::Client.new(config)

## Actual code to query

user = client.user

puts "Current location (best guess) is: #{user.best_guess.name}"
puts "Hierarchy looks like this:"
puts user.locations.map { |loc| loc.name }
