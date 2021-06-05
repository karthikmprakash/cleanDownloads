# code by Karthik M Prakash (mkarthikprakash.work@gmail.com)
# Reference (https://medium.com/swlh/automation-python-organizing-files-5d2b6b933402)

# Libraries Required 
import os                   # Library contains all the functions that returns system dependent functionality
from shutil import move     # Imports move function from shell utilities


user  = os.getlogin()            # defining the current username 

root_dir = '/Users/{}/Downloads/'.format(user)      # Defining the root folder which we want to work on i.e Downloads folder here

Folders = ['Images/','Documents/','Videos/','Softwares/','Compressed/','Codes/','Databases/']  # Declaring names of all the folders for sorted_files 
 
# Code block to check if the folder already exisits , if not create with the name 
for Folder in Folders:
    if not(os.path.exists(root_dir + Folder)):
        os.mkdir(root_dir + Folder)

image_dir = '/Users/{}/Downloads/Images/'.format(user)
document_dir = '/Users/{}/Downloads/Documents/'.format(user)
code_dir = '/Users/{}/Downloads/Codes/'.format(user)
software_dir = '/Users/{}/Downloads/Softwares/'.format(user)
compressed_dir = '/Users/{}/Downloads/Compressed/'.format(user)
database_dir = '/Users/{}/Downloads/Databases/'.format(user)
video_dir = '/Users/{}/Downloads/Videos/'.format(user)

# category wise file types 
doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx', '.md','.rtf','.tex','.pem')
img_types = ('.cr2','.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff','.psd','.bmp')
video_types= ('.3gp','.mkv','.avi','.mov','.mpg','.mpeg','.wmv','.h264')
software_types = ('.exe','.msi')
compressed_types =('.zip','.tar','.rar','.iso','.7z')
programming_types= ('.py','.ino','.m','.java','.js','.html','.htm','.css','.cgi','.sh','.swift','.h','.cpp','.cs')
database_types=('.csv','.dat','.db','.log','.mdb','.sav','.sql','.tar','.xml')

# Function to get all the files in the Downloads folder as a list
def get_non_hidden_files(root_dir):
    return [f for f in os.listdir(root_dir) if os.path.isfile(os.path.join(root_dir,f)) and not f.startswith('.')] 


# Function to move files to their respective directories 
def move_files(files):

    for file in files:
        try:
            if file.lower().endswith(doc_types):
                dest_dir = '/Users/{}/Downloads/Documents/'.format(user)
               
            
            elif file.lower().endswith(img_types):
                dest_dir = '/Users/{}/Downloads/Images/'.format(user)
                
            
            elif file.lower().endswith(video_types):
                dest_dir = '/Users/{}/Downloads/Videos/'.format(user)
                

            elif file.lower().endswith(software_types):
                dest_dir = '/Users/{}/Downloads/Softwares/'.format(user)
               
            
            elif file.lower().endswith(compressed_types):
                dest_dir = '/Users/{}/Downloads/Compressed/'.format(user)

            
            elif file.lower().endswith(programming_types):
                dest_dir = '/Users/{}/Downloads/Codes/'.format(user)

            elif file.lower().endswith(database_types):
                dest_dir = '/Users/{}/Downloads/Databases/'.format(user)


            else : 
                continue

            move(os.path.join(root_dir,file),dest_dir)
            
        except IOError:
            pass

# Calling the sorting function if particularly running this file
if __name__ == "__main__":
    files = get_non_hidden_files(root_dir) 
    move_files(files)


#Uncomment code below for debugging 

#print(files) 







