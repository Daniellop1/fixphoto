import os
import json
from datetime import datetime
from pathlib import Path
import piexif

def timestamp_to_exif_format(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime("%Y:%m:%d %H:%M:%S")

def process_directory(directory):
    for file in Path(directory).iterdir():
        if file.suffix != '.json':
            continue
        try:
            with open(file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            image_name = data.get('title')
            timestamp = int(data.get('photoTakenTime', {}).get('timestamp', 0))
            image_path = file.parent / image_name

            if not image_path.exists():
                print(f"⚠️ Image not found: {image_name}")
                continue

            # Update system file timestamps
            file_time = datetime.utcfromtimestamp(timestamp).timestamp()
            os.utime(image_path, (file_time, file_time))
            print(f"✅ File timestamp updated: {image_path.name}")

            # Update EXIF data if it's a JPEG
            if image_path.suffix.lower() in ['.jpg', '.jpeg']:
                exif_dict = piexif.load(str(image_path))
                exif_date = timestamp_to_exif_format(timestamp).encode('utf-8')
                exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = exif_date
                exif_dict["Exif"][piexif.ExifIFD.DateTimeDigitized] = exif_date
                piexif.insert(piexif.dump(exif_dict), str(image_path))
                print(f"📝 EXIF data updated: {image_path.name}")

            # Delete JSON file
            file.unlink()
            print(f"🗑️ JSON file deleted: {file.name}")

        except Exception as e:
            print(f"❌ Error processing {file.name}: {e}")
