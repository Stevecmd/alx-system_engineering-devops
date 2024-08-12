#!/usr/bin/env bash
i=1
until [ 15 -lt $i ]
do
    echo "using until $i"
    ((i++))
done
