import os
import shutil 

from_dir="C:/Users/u/Desktop/New folder"
to_dir="C:/Users/u/Desktop"

list_of_songs=os.listdir(from_dir)

for song_name in list_of_songs:
    name,extension =os.path.splitext(song_name)
    if extension=="":
        continue
    if extension in ['.m4a']:
        path1=from_dir+'/'+song_name
        path2=to_dir+'/'+"song"
        path3=to_dir+'/'+"song"+'/'+song_name   
        if os.path.exists(path2):
            shutil.move(path1,path3) 
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)      