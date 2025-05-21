# 📸 fixphoto

[![PyPI version](https://img.shields.io/pypi/v/fixphoto.svg)](https://pypi.org/project/fixphoto/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build](https://github.com/daniellop1/fixphoto/actions/workflows/publish.yml/badge.svg)](https://github.com/daniellop1/fixphoto/actions)

**fixphoto** is a Python command-line tool that fixes incorrect file timestamps and EXIF metadata in photos exported via Google Takeout. It reads `.json` sidecar files (included in the export) to restore the original date taken and clean up the metadata.

---

## ✨ Features

- Reads real photo capture times from Takeout `.json` files.
- Updates file creation/modification timestamps.
- Sets proper EXIF `DateTimeOriginal` and `DateTimeDigitized` (for `.jpg`/`.jpeg`).
- Deletes the corresponding `.json` file after processing.
- Simple and fast CLI for batch processing.

---

## 📦 Installation

Install the latest version directly from [PyPI](https://pypi.org/project/fixphoto/):

```bash
pip install fixphoto
````

---

## 🚀 Usage

```bash
fixphoto /path/to/google-takeout-photos
```

### Example

```bash
fixphoto ~/Downloads/Takeout/Google\ Photos/Camera/
```

This will:

* Find all `.json` files in the specified folder.
* Read the timestamp from each JSON and apply it to the matching photo.
* Set EXIF metadata for JPEGs.
* Delete each processed `.json`.

---

## ⚠️ Notes

* Only `.jpg`/`.jpeg` files support EXIF metadata modification.
* `.png`, `.webp`, `.heic`, or `.mp4` files will have system timestamps adjusted but not EXIF (future versions may support these).
* This tool does not recurse into subdirectories yet — only the specified folder is processed.

---

## 🛠 Requirements

* Python 3.7 or higher
* [`piexif`](https://pypi.org/project/piexif/)
* [`click`](https://pypi.org/project/click/)

These are automatically installed when you use `pip install fixphoto`.

---

## 📄 License

MIT License — see [`LICENSE`](./LICENSE) for details.

---

## 🙋‍♂️ Contributing

Pull requests are welcome! If you want to suggest features like:

* Recursive folder support
* Support for more formats (e.g., `.heic`, `.mp4`)
* Dry-run or verbose options

Feel free to open an issue or PR.

---

## 🔗 Links

* 📦 PyPI: [https://pypi.org/project/fixphoto](https://pypi.org/project/fixphoto)
* 💻 GitHub: [https://github.com/daniellop1/fixphoto](https://github.com/daniellop1/fixphoto)
