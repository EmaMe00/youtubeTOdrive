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

controlError = 0

#Autentication on Google
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

#Playlist on youtube
p = Playlist('PLAYLIST URL')

#Folder path to save video
SAVE_PATH = ("YOUR PATH" + p.title)
os.mkdir(SAVE_PATH)

with open(SAVE_PATH+"/ERROR_"+p.title, 'a') as f:
    f.write("Downloading Error: \n")
    f.close()

print(f'\nDownloading playlist: {p.title}. Total element: {len(p.videos)}\n')

counter = 0
for video in p.videos:
    try:
        counter = counter + 1
        print(f"Downloading video: {video.title}. Number {counter}/{len(p.videos)}")
        video.streams.filter(res="720p").first().download(SAVE_PATH)
        print("Downloaded video: " + video.title + "\n")
    except Exception as e: 
        try:
            video.streams.filter(res="480p").first().download(SAVE_PATH)
            print("Downloaded video: " + video.title + "\n")
        except:
            try:
                video.streams.filter(res="360p").first().download(SAVE_PATH)
                print("Downloaded video: " + video.title + "\n")
            except:
                controlError = 1
                print(e)
                print("Error to download " + video.title + "\n")
                with open(SAVE_PATH+"/ERROR_"+p.title(), 'a') as f:
                    f.write(video.title + '\n')
                    f.close()

print("Playlist downloaded !\n")

# Get the list of all files and directories
dir_list = os.listdir(SAVE_PATH)
#print("Files and directories in '", path, "' :")
# prints all files
#print(dir_list)


file_path = SAVE_PATH + "/"
folderID = "YOUR DRIVE FOLDER ID"

with open(SAVE_PATH+"/ERROR_"+p.title, 'a') as f:
    f.write("\nUploading Error: \n")
    f.close()

counter = 0
for filename in dir_list:
    try:
        if(filename != ("ERROR_"+p.title)):
            counter = counter + 1
            print(f"Uploading: {filename}. Number {counter}/{len(p.videos)}")
            file1 = drive.CreateFile({'title': filename , 'parents': [{'id': folderID}]})
            file1.SetContentFile(file_path+filename)
            file1.Upload()
            print(f'Uploaded: {filename}\n')
            os.remove(file_path + filename)

    except Exception as e:
        controlError = 1
        print(e)
        print("\nError to upload " + filename + "\n")
        with open(SAVE_PATH+"/ERROR_"+p.title, 'a') as f:
            f.write(filename + '\n')
            f.close()


dir_list = os.listdir(SAVE_PATH)
if (controlError == 0):
    print("Removing file from pc ...\n")
    for filename in dir_list:
        os.remove(file_path + filename)

    os.rmdir(SAVE_PATH)
    print("File removed!\n")

print("Finish !")

