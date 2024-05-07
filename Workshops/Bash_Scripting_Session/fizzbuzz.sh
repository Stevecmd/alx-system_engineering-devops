#!/usr/bin/env bash

# print until a given number
# if the number is divisible by 3 print fizz
# if the number is divisible by 5 print buzz
# if the number is divisible by 3 and 5 print fizzbuzz
# otherwise print the number itself

# Check if the argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <number>"
    exit 1
fi

for ((i=1; i<= "$1"; i++))
do
    if ((i % 3 == 0)) && ((i % 5 == 0)); then
        echo "fizzbuzz"
    elif ((i % 3 == 0)); then
        echo "fizz"
    elif ((i % 5 == 0)); then
        echo "buzz"
    else
        echo "$i"
    fi
done
