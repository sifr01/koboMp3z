# koboMp3z
Zips mp3 files and renames the file extension to mp3z, allowing them to be sideloaded and played with a kobo as media files - ideal for audiobooks. See article [here](https://goodereader.com/blog/audiobooks/you-can-now-sideload-audiobooks-on-the-kobo-sage-libra-2-and-elipsa#disqus_thread) and [here](https://blog.the-ebook-reader.com/2021/11/10/how-to-sideload-audiobooks-and-mp3s-to-kobo-ereaders/) for more information.

# Usage:
    python3 koboMp3z.py /path/to/directory/

# Notes:
- The script only works on mp3 files
- If there are no mp3 files in the folder you specify, the script will exit
- If python doesnt have permissions to run in the folder you specify (eg. /tmp/ or /home/), python will not find any files in the folder and will also exit

After running the script, sideload the mp3z files onto your Kobo

Information on how to listen to audiobooks on your kobo can be found [here](https://help.kobo.com/hc/en-us/articles/4406292712471-Listen-to-audiobooks-on-your-Kobo-eReader).
