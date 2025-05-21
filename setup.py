from setuptools import setup, find_packages

setup(
    name="fixphoto",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["click", "piexif"],
    entry_points={
        "console_scripts": [
            "fixphoto=fixphoto.cli:cli",
        ],
    },
    author="Daniel López Pérez",
    description="CLI tool to fix file timestamps and EXIF metadata for Google Takeout photos",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.7',
)
