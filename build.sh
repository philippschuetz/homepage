#!/bin/bash

# clear contents of the output directory
rm -rf out/*

PLACEHOLDER_CONTENT="<!--content-->"
PLACEHOLDER_TEMPLATES_PREFIX="<!--templates-"
PLACEHOLDER_TEMPLATES_SUFFIX="-->"
HTML_TEMPLATE=$(cat "src/templates/index.html")
SOURCE_DIR="src/content"
DESTINATION_DIR="out"

# define replace values
REPLACE_KEYS=("testkey1" "testkey2")
REPLACE_VALUES=("testvalue1" "testvalue2")



# Iterate through each file in the source directory
find "$SOURCE_DIR" -type f | while read -r file; do

    # relative path of the file from the source directory
    relative_path="${file#$SOURCE_DIR/}"

    # create the destination directory if it doesn't exist
    mkdir -p "$DESTINATION_DIR/$(dirname "$relative_path")"

    # search & replace content, copy the content to the destination directory
    new_content=$(echo $HTML_TEMPLATE | sed "s|${PLACEHOLDER_CONTENT}|$(cat ${file})|g")
    echo $new_content > "$DESTINATION_DIR/$relative_path"
done
