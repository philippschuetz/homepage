import shutil
import datetime
from pathlib import Path

PLACEHOLDER_CONTENT = '<!--content-->'
PLACEHOLDER_TEMPLATES_PREFIX = '<!--components-'
PLACEHOLDER_TEMPLATES_SUFFIX = '-->'
HTML_TEMPLATE = open('src/base.html').read()
CONTENT_DIR = Path('src/content')
TEMPLATES_DIR = Path('src/components')
DESTINATION_DIR = Path('out')
REPLACE_DICT = {
    '<!--year-->': str(datetime.datetime.now().year)
}


def main():
    if DESTINATION_DIR.exists():
        shutil.rmtree(DESTINATION_DIR)
    DESTINATION_DIR.mkdir()

    # Iterate through each file in the source directory
    for file in Path(CONTENT_DIR).rglob('*'):
        if file.is_dir():
            continue
        relative_path = file.relative_to(CONTENT_DIR)
        Path(DESTINATION_DIR, relative_path.parent).mkdir(parents=True, exist_ok=True)
        # search & replace html content
        new_content = HTML_TEMPLATE.replace(PLACEHOLDER_CONTENT, open(file).read())

        # search and replace with REPLACE_KEYS and REPLACE_VALUES
        for key, value in REPLACE_DICT.items():
            new_content = new_content.replace(key, value)

        # add content from components files
        for tmp_file in TEMPLATES_DIR.rglob('*'):
            if file.is_file():
                old = f'{PLACEHOLDER_TEMPLATES_PREFIX}{tmp_file.stem}{PLACEHOLDER_TEMPLATES_SUFFIX}'
                new_content = new_content.replace(old, open(tmp_file).read())

        # write content to file
        with open(Path(DESTINATION_DIR, relative_path), 'w') as f:
            f.write(new_content)


if __name__ == '__main__':
    main()
