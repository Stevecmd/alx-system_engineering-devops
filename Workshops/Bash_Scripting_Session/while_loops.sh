#!/usr/bin/env bash

# Print numbers from 1 to 15
counter=1
while [ $counter -le 15 ]
do
    echo "Number $counter"
    ((counter++))
done
echo "Done"
