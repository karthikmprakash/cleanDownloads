import time 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sorty as sr
from os import getlogin 

class ExampleHandler(FileSystemEventHandler):
    def on_created(self, event): # when file is created
        user = getlogin()
        root_dir = '/Users/{}/Downloads/'.format(user)
        files = sr.get_non_hidden_files(root_dir) # Returns the files that are not hidden 
        sr.move_files(files)

observer = Observer()
event_handler = ExampleHandler() # create event handler
# set observer to use created handler in directory
observer.schedule(event_handler, path='C:/Users/mkart/Downloads')
observer.start()

# sleep until keyboard interrupt, then stop + rejoin the observer
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()




## https://stackoverflow.com/questions/45113304/if-file-and-directory-exists