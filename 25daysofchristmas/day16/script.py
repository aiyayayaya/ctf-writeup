import os
import zipfile
import exiftool

with zipfile.ZipFile('final-final-compressed.zip', 'r') as zip_ref:
    zip_ref.extractall('extracted')
zips = os.listdir('extracted')
for zipped in zips:
    with zipfile.ZipFile('extracted/' + zipped, 'r') as zip_ref:
        zip_ref.extractall('extracted/' + zipped[:-4])
directories = [x for x in os.listdir('extracted') if os.path.isdir('extracted/' + x)]
file_count = 0
version_count = 0
for directory in directories:
    files = ['extracted/' + directory + '/' + i for i in os.listdir('extracted/' + directory)]
    file_count += len(files)
    with exiftool.ExifTool() as et:
        metadata = et.get_metadata_batch(files)
    for data in metadata:
        for key, value in data.items():
            if "1.1" in str(value):
                version_count += 1
    for tempfile in files:
        with open(tempfile, 'r', errors='ignore') as reader:
            f = reader.readlines()
        for line in f:
            if "password" in line:
                print(tempfile)

    