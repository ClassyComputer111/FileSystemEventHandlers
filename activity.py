import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "folderA"
to_dir = "folderB"

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
       print(f"Hey, {event.src_path} has been created")

    def on_deleted(self, event):
       print(f"Oops,Somone deleted {event.src_path}!")

    def on_modified(self, event):
       print(f"Hey,Someone modified{event.src_path}!")

    def on_moved(self, event):
       print(f"Hey,Someone moved{event.src_path}!")

# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

try:
    
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print('stopped!')
    observer.stop()