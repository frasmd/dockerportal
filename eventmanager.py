import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler
import threading
import argparse
import yaml
from yaml.loader import SafeLoader
from fileserver import FileServer


def process_new_file(files):
    print(f"Processing file: {files}")
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", dest="input_file", required=True, help="Path to the YAML file.")
    args = parser.parse_args()
    
    with open(args.input_file,"r") as f:
        data = yaml.load(f, Loader=SafeLoader)
    
    fobj = FileServer(data)
    fobj.UploadImages([files])


class onMyWatch:
    watchDirectory = "/root/changecheckfolder"
    

    def __init__(self) -> None:
        self.observer = Observer()
    
    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDirectory, recursive=True)
        self.observer.start()

        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer stopped")
        
        self.observer.join()


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
        
        elif event.event_type == 'created':
            print("watchdog recieved created event - %s" %event.src_path)
            thread = threading.Thread(target=process_new_file, args=(event.src_path,))
            thread.start()
        elif event.event_type == 'modified':
            print("Watchdog received modified event - %s"%event.src_path)

if __name__ == '__main__':
    watch = onMyWatch()
    watch.run()