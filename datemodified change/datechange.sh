#!/bin/bash

# Specify the folder to process (default to current directory)
folder=${1:-.}

# Loop through all files in the specified folder
for file in "$folder"/*; do
    # Extract the date part from the filename
    if [[ "$file" =~ ([0-9]{4})([0-9]{2})([0-9]{2}) ]]; then
        year="${BASH_REMATCH[1]}"
        month="${BASH_REMATCH[2]}"
        day="${BASH_REMATCH[3]}"

        # Construct a date string in the format YYYY-MM-DD
        date_str="$year-$month-$day"

        # Use touch to set the modification and access time of the file
        touch -d "$date_str 12:00:00" "$file"
        echo "Updated $file to date $date_str"
    else
        echo "Filename $file does not contain a valid date."
    fi
done
