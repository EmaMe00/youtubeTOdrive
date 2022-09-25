'''
Befor starting this program you need to run: 
pip3 install httplib2==0.15.0 pip install google-api-python-client==1.6
pip3 install pytube
pip3 install pydrive
brew install python-tk
'''

from cgi import test
from concurrent.futures import thread
from multiprocessing.resource_sharer import stop
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from pytube import YouTube
from pytube import Playlist
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import threading

def startThread():
    thread.start()
    

def downloadYTPlaylist():

    controlError = 0

    #Autentication on Google
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

    #Playlist on youtube
    p = Playlist(linkfield.get())

    #Folder path to save video
    SAVE_PATH = ("/Users/emanuelemele/Desktop/Altro/downloadYTPlaylistPY/" + p.title)
    os.mkdir(SAVE_PATH)

    with open(SAVE_PATH+"/ERROR_"+p.title, 'a') as f:
        f.write("Downloading Error: \n")
        f.close()

    textbox.insert(INSERT,f'\nDownloading playlist: {p.title}. Total element: {len(p.videos)}\n')
    #print(f'\nDownloading playlist: {p.title}. Total element: {len(p.videos)}\n')

    counter = 0
    for video in p.videos:
        try:
            counter = counter + 1
            textbox.insert(INSERT,f"Downloading video: {video.title}. Number {counter}/{len(p.videos)}")
            #print(f"Downloading video: {video.title}. Number {counter}/{len(p.videos)}")
            video.streams.filter(res="720p").first().download(SAVE_PATH)
            textbox.insert(INSERT,"Downloaded video: " + video.title + "\n")
            #print("Downloaded video: " + video.title + "\n")
        except Exception as e: 
            try:
                video.streams.filter(res="480p").first().download(SAVE_PATH)
                textbox.insert(INSERT,"Downloaded video: " + video.title + "\n")
                #print("Downloaded video: " + video.title + "\n")
            except:
                try:
                    video.streams.filter(res="360p").first().download(SAVE_PATH)
                    textbox.insert(INSERT,"Downloaded video: " + video.title + "\n")
                    #print("Downloaded video: " + video.title + "\n")
                except:
                    controlError = 1
                    #print(e)
                    textbox.insert(INSERT,e)
                    #print("Error to download " + video.title + "\n")
                    textbox.insert(INSERT,"Error to download " + video.title + "\n")
                    with open(SAVE_PATH+"/ERROR_"+p.title(), 'a') as f:
                        f.write(video.title + '\n')
                        f.close()

    textbox.insert(INSERT,"Playlist downloaded !\n")
    #print("Playlist downloaded !\n")

    # Get the list of all files and directories
    dir_list = os.listdir(SAVE_PATH)
    #print("Files and directories in '", path, "' :")
    # prints all files
    #print(dir_list)


    file_path = SAVE_PATH + "/"
    folderID = folderfield.get()

    with open(SAVE_PATH+"/ERROR_"+p.title, 'a') as f:
        f.write("\nUploading Error: \n")
        f.close()

    counter = 0
    for filename in dir_list:
        try:
            if(filename != ("ERROR_"+p.title)):
                counter = counter + 1
                textbox.insert(INSERT,f"Uploading: {filename}. Number {counter}/{len(p.videos)}")
                #print(f"Uploading: {filename}. Number {counter}/{len(p.videos)}")
                file1 = drive.CreateFile({'title': filename , 'parents': [{'id': folderID}]})
                file1.SetContentFile(file_path+filename)
                file1.Upload()
                textbox.insert(INSERT,f'Uploaded: {filename}\n')
                #print(f'Uploaded: {filename}\n')
                os.remove(file_path + filename)

        except Exception as e:
            controlError = 1
            textbox.insert(INSERT,e)
            #print(e)
            textbox.insert(INSERT,"\nError to upload " + filename + "\n")
            #print("\nError to upload " + filename + "\n")
            with open(SAVE_PATH+"/ERROR_"+p.title, 'a') as f:
                f.write(filename + '\n')
                f.close()


    dir_list = os.listdir(SAVE_PATH)
    if (controlError == 0):
        textbox.insert(INSERT,"Removing file from pc ...\n")
        #print("Removing file from pc ...\n")
        for filename in dir_list:
            os.remove(file_path + filename)

        os.rmdir(SAVE_PATH)
        textbox.insert(INSERT,"File removed!\n")
        #print("File removed!\n")

    textbox.insert(INSERT,"Finish")
    #print("Finish !")



thread = threading.Thread(target=downloadYTPlaylist)

window = Tk()
window.geometry("700x700")

myButton = Button(window,text="Download",command=startThread)
linklabel = Label(window,text="Youtube Link: ")
linkfield = Entry(window,width=63)
folderlabel = Label(window,text="Drive Folder Link: ")
folderfield = Entry(window,width=63)
textbox = ScrolledText(window,height=45,width=90)

linklabel.grid(row=0, column=0)
linkfield.grid(row=0, column=1)
folderlabel.grid(row=1,column=0)
folderfield.grid(row=1,column=1)
myButton.grid(row=2,column=0,columnspan=2)
textbox.grid(row=3,column=0,columnspan=2)

window.resizable(True, True)
window.mainloop()