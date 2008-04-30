#!/usr/bin/env ruby

require 'yaml'
require 'rubygems'
# work-around for a bug in oauth 0.2.4
require 'oauth/helper'
require 'fireeagle'

if ARGV.empty?
  puts "Usage: update.rb <location>"
  exit
end

config = YAML.load(open("fireeagle.yml").read)

unless config.has_key?("access_token") && config.has_key?("access_token_secret")
  puts "Application must be authorised: please run authorize.rb"
  exit
end

client = FireEagle::Client.new(config)

## Actual code to update

client.update(:q => ARGV.shift)
puts "Location successfully updated."
