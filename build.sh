rm -rf out/*

placeholder_content="<!--content-->"

# generate files in the out directory
content="test content"
sed "s/${placeholder_content}/${content}/" index.html
