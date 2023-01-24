# koboMp3z
_Zips mp3 files and renames the file extension to mp3z, allowing them to be sideloaded and played with a Kobo as media files - ideal for audiobooks. See article [here](https://goodereader.com/blog/audiobooks/you-can-now-sideload-audiobooks-on-the-kobo-sage-libra-2-and-elipsa#disqus_thread) and [here](https://blog.the-ebook-reader.com/2021/11/10/how-to-sideload-audiobooks-and-mp3s-to-kobo-ereaders/) for more information._

# Usage:
    python3 koboMp3z.py /path/to/directory/

# Notes:
- The script only works on mp3 files
- If there are no mp3 files in the folder you specify, the script will exit
- If python doesnt have permissions to run in the folder you specify (eg. /tmp/ or /home/), python will not find any files in the folder and will exit
- When you play the mp3 file on your PC, if it displays a picture (probably cover art) then this needs to be removed. Otherwise you wont be able to play the file using the kobo; it will crash and the kobo will restart. To fix this, BEFORE running the python script you must remove the picture (ID3 metadata). To do this in linux on the command line, install ID3v2:
`sudo apt install id3v2`
    - Then enter the folder using the command line and run:
        `id3v2 -D *.mp3`
    - Only then should you run the python script

After running the python script, sideload the mp3z files onto your Kobo

# Further information:

- Information on how to listen to audiobooks on your Kobo can be found [here](https://help.kobo.com/hc/en-us/articles/4406292712471-Listen-to-audiobooks-on-your-Kobo-eReader).

- Information on how to use your kobo without having to register your device can be found in my wiki [here](
https://github.com/sifr01/wiki/wiki/Kobo-ereader----use-device-without-online-registration).