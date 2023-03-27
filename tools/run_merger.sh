#!/bin/bash

set -e

MERGER_FILES=$(find ./tools -name "Merger-*.py")

if [ -z "$MERGER_FILES" ]; then
    echo "Error: No Merger files found in ./tools directory"
    exit 1
fi

for file in $MERGER_FILES
do
    echo "Executing $file"
    python "$file"
done
