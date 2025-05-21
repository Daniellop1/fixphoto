# Fixphoto

`fixphoto` is a command-line tool that corrects system file timestamps and EXIF metadata for photos exported via Google Takeout.

## Features

- Reads real creation dates from Google Takeout `.json` metadata files.
- Updates file modification and access times.
- Edits EXIF metadata (`DateTimeOriginal` and `DateTimeDigitized`) for `.jpg`/`.jpeg` files.
- Deletes the `.json` metadata files after processing.

## Installation

```bash
git clone https://github.com/daniellop1/fixphoto-cli.git
cd fixphoto-cli
pip install .
