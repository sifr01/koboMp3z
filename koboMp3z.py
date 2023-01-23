import os
from os import listdir
from os.path import isfile, join
import sys
from zipfile import ZipFile

# Get path to the target directroy
if len(sys.argv) < 2:
	print("USAGE: python3 koboMp3z.py /path/to/directory/")	
	import os
	os._exit(1)
targetDir = sys.argv[1]

# List folder contents before zipping and renaming
print(f"\n Folder contents before zipping and renaming: \n {os.listdir(targetDir)} \n ")

# Get all files in target directory
onlyFiles = [f for f in listdir(targetDir) if isfile(join(targetDir, f))]

# Exit if there are no mp3 files found in the target directory
count = 0
for file in onlyFiles:
    # Get the file extension
    s = file.split(".")
    # If file extension is mp3, add to the counter
    if s[-1] == "mp3":
        count += 1
        break
if count == 0:
        print(" ! No mp3 files found in this directory.\n ! Does python have the correct permissions to work in this directory?")
        exit()

# # Would you now like to delete the mp3 files?
while True:
    yes_or_no = input("After creating the mp3z files, would you like to delete the mp3 files? Yes or No? ").lower()
    if yes_or_no == "yes":
        print("mp3 files will be deleted")
        break
    elif yes_or_no == "no":
        print("mp3 files will be left")
        break

# loop through files in the folder
for file in onlyFiles:
    # Get the file extension
    s = file.split(".")
    extn = s[-1]
    print(extn)
    # Dont touch any files which arent mp3 files
    if extn != 'mp3':
        print(f'Not touching {file} as it is not an mp3 file. ')
        newExtn = extn
    #Do work on files which are mp3 files
    elif extn == 'mp3':
        # zip the file with extension mp3
        print(f'Zipping {file}...')
        # rename the file suffix to mp3z
        outputName = targetDir + s[0] + ".mp3z"
        with ZipFile(outputName, 'w') as zip:
            zip.write(targetDir + file)
        print(f'Zipped {file}...')
        if yes_or_no == "yes":
            os.remove(targetDir+file)

# # List folder contents after zipping and renaming
# print(f"\n Folder contents after zipping and renaming: \n {os.listdir(targetDir)} \n")