import os
from os import listdir
from os.path import isfile, join

from zipfile import ZipFile

# List folder contents before zipping and renaming
print(f"\n Folder contents before zipping and renaming: \n {os.listdir()} \n ")

# Get path to current dir
cwd = os.getcwd()

# Get all files in dir
onlyFiles = [
    f for f in listdir(cwd) if isfile(join(cwd, f))
    ]
print(onlyFiles)

for file in onlyFiles:

    # Get the file extension
    s = file.split(".")
    extn = s[-1]

    # Dont touch any files which arent mp3 files
    if extn != 'mp3':
        print(f'Not touching {file} as it is not an mp3 file. ')
        newExtn = extn

    #Do work on files which are mp3 files
    elif extn == 'mp3':
        # zip the file with extension mp3
        print(f'Zipping {file}...')
        # rename the file suffix to mp3z
        newName = s[0]+".mp3z"
        with ZipFile(newName, 'w') as zip:
            zip.write(file)
        print(f'Zipped {file}...')
        
    else:
        print(f'Oh dear, something weird will happen with {file} so I will stop the script now. ')

# List folder contents after zipping and renaming
print(f"\n Folder contents after zipping and renaming: \n {os.listdir()} \n")