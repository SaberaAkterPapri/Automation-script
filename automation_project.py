import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

WATCH_FOLDER="/home/heheh/papri/automation_app/Automation-script"

class OrganizerHandler(FileSystemEventHandler):
    def on_created(self,event):
        if event.is_directory:
            return
        file_path=event.scr_path
        filename=os.path.basename(file_path)
        extension=filename.split('.')[-1]
        extension_folder=os.path.join(WATCH_FOLDER,extension)

        if not os.path.exists(extension):
            os.makedirs(extension_folder)

        shutil.move(file_path,os.path.join(extension_folder,filename))
        print(f"move file {filename} to {extension}/")

if __name__=="__main__":
    event_handler=OrganizerHandler()
    Observer=Observer()
    Observer.schedule(event_handler,WATCH_FOLDER,recursive=False)
    Observer.start()
    print(f"watching folder: {WATCH_FOLDER}......press Ctrl+C to stop")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    Observer.stop()
Observer.join()



