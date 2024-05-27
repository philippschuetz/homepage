#!/bin/bash

# clear contents of the output directory
rm -rf out/*

PLACEHOLDER_CONTENT="<!--content-->"
PLACEHOLDER_TEMPLATES_PREFIX="<!--templates-"
PLACEHOLDER_TEMPLATES_SUFFIX="-->"
SOURCE_DIR="src/content"
DESTINATION_DIR="out"

# define replace values
REPLACE_KEYS=("testkey1" "testkey2")
REPLACE_VALUES=("testvalue1" "testvalue2")

# Iterate through each file in the source directory
find "$SOURCE_DIR" -type f | while read -r file; do

    # relative path of the file from the source directory
    relative_path="${FILE#$SOURCE_DIR/}"

    # create the destination directory if it doesn't exist
    mkdir -p "$DESTINATION_DIR/$(dirname "$relative_path")"

    # search & replace content, copy the content to the destination directory
    file=$(echo $file | sed -e "s/${PLACEHOLDER_CONTENT}/${content}/")
    cp "$file" "$DESTINATION_DIR/$relative_path"
done
