# code by Karthik M Prakash (mkarthikprakash.work@gmail.com)
# Reference (https://medium.com/swlh/automation-python-organizing-files-5d2b6b933402)

# Libraries Required 
import os                   # Library contains all the functions that returns system dependent functionality
from shutil import move     #


user  = "mkart"             # defining the current username 

root = '/Users/{}/Downloads/'.format(user)      #Defining the root folder which we wan to work on i.e Downloads folder here

Folders = ['Images/','Documents/','Videos/','Softwares/','Compressed/'] 

for Folder in Folders:
    if not(os.path.exists(root + Folder)):
        os.mkdir(root + Folder)
        



