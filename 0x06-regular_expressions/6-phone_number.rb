#!/usr/bin/env ruby
# Ruby script that accepts one argument and
# passes it to a regular expression matching method

puts ARGV[0].scan(/^\d{10}$/).join
