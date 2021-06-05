import time 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sorty as sr
from os import getlogin 


#
class FolderHandler(FileSystemEventHandler):
    def on_created(self, event): 						# when file is created
        user = os.getlogin()    						# return the name of the user logged-in
        #user = 'mkart'									# DEBUG
        root_dir = '/Users/{}/Downloads/'.format(user) 
        #root_dir = path								# DEBUG
        files = sr.get_non_hidden_files(root_dir)	    # Returns the files that are not hidden 
        sr.move_files(files)							# calls the function in the sorty program t move files that are returned 
        time.sleep(3)									# delay is added to call the function again if some files are not handled for the first time
        files = sr.get_non_hidden_files(root_dir)       
        sr.move_files(files)


user = os.getlogin() 												# make sure your user folder is as the same name of your username or else it wont work!
observer = Observer()
event_handler = FolderHandler() 									# create event handler

observer.schedule(event_handler, path=f'C:/Users/{user}/Downloads') # set observer to use created handler in directory
observer.start()

# sleep until keyboard interrupt, then stop + rejoin the observer
try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop()

observer.join()




## https://stackoverflow.com/questions/45113304/if-file-and-directory-exists