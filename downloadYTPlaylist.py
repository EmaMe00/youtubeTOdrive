"""
Documentation:
https://pythonhosted.org/PyDrive/
https://pytube.io/en/latest/
"""

from pytube import YouTube
from pytube import Playlist
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

#Autentication on Google
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

#Playlist on youtube
p = Playlist('URL PLAYLIST')

#Folder path to save video
SAVE_PATH = "YOUR PATH" + p.title
os.mkdir(SAVE_PATH)

print(f'\nDownloading playlist: {p.title} ....\n')

#Downloading video youtube in your folder
for video in p.videos:
    print("Downloading video " + video.title + " ....")
    video.streams.filter(res="720p").first().download(SAVE_PATH)
    print("Downloaded video: " + video.title + "\n")

print("Playlist downloaded !\n")

# Get the list of all files and directories
dir_list = os.listdir(SAVE_PATH)

file_path = SAVE_PATH + "/"
folderID = "GOOGLE DRIVE FOLDER ID"

#Uploading file to local from drive folder
for filename in dir_list:
    print(f"Uploading {filename} ....")
    file1 = drive.CreateFile({'title': filename , 'parents': [{'id': folderID}]})
    file1.SetContentFile(file_path+filename)
    file1.Upload()
    print(f'Uploaded: {filename}\n')

#Removing file in local and directory
print("Removing file from pc ...\n")
for filename in dir_list:
    os.remove(file_path + filename)

os.rmdir(SAVE_PATH)

print("File removed!\n")
print("Finish !")

