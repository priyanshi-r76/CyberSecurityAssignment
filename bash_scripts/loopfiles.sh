#!/bin/bash

# Script to create 10 files with current date

for i in {1..10}
do
    filename="file$i.txt"

    echo "Current Date:" > $filename
    date >> $filename

done

echo "10 files created successfully"
