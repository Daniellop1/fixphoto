import click
from fixphoto.processor import process_directory

@click.command()
@click.argument('folder', type=click.Path(exists=True))
def cli(folder):
    """Fix timestamps and EXIF metadata in Google Takeout photo exports."""
    print(f"📁 Processing folder: {folder}")
    process_directory(folder)
