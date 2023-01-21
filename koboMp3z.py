import os
from os import listdir
from os.path import isfile, join

from zipfile import ZipFile

# List folder contents before zipping and renaming
print(f"\n Folder contents before zipping and renaming: \n {os.listdir()} \n ")

# Get path to current dir
cwd = os.getcwd()

# Get all files in dir
onlyfiles = [
    f for f in listdir(cwd) if isfile(join(cwd, f))
    ]
print(onlyfiles)

for file in onlyfiles:

    # Get the current format
    s = file.split(".")
    extn = s[-1]

    if extn != 'mp3':
        print(f'Not touching {file} as it is not an mp3 file. ')
        newExtn = extn
         
    elif extn == 'mp3':
        # zip the file with extension mp3
        print(f'Zipping {file}...')
        with ZipFile(file, 'w') as zip:
            zip.write(file)
        print(f'Zipped {file}...')

        # Change format and get new filename
        newExtn = 'mp3z'
        s[-1] = newExtn
        s = '.'.join(s)

        # Rename file
        os.rename(file, s)
        print(f"Renamed zip file extension to {s}")
        
    else:
        print(f'Oh dear, something weird will happen with {file} so I will stop the script now. ')

# List folder contents after zipping and renaming
print(f"\n Folder contents after zipping and renaming: \n {os.listdir()} \n")
