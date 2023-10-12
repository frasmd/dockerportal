from time import sleep
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler
from threading import Thread
from argparse import ArgumentParser
import yaml
from yaml.loader import SafeLoader
from fileserver import FileServer


def __getData(file):
    with open(file,"r") as f:
        data = yaml.load(f, Loader=SafeLoader)
    return data

def process_new_file(files):
    print(f"Processing file: {files}")
    
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest="input_file", required=True, help="Path to the YAML file.")
    args = parser.parse_args()

    data = __getData(args.input_file)
    
    fobj = FileServer(data)
    fobj.UploadImages([files])


class onMyWatch:

    def __init__(self, watchPath) -> None:
        self.observer = Observer()
        self.watchDirectory = watchPath

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDirectory, recursive=True)
        self.observer.start()

        try:
            while True:
                sleep(5)
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
            thread = Thread(target=process_new_file, args=(event.src_path,))
            thread.start()
        elif event.event_type == 'modified':
            print("Watchdog received modified event - %s"%event.src_path)

def startEvent():
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest="input_file", required=True, help="Path to the YAML file.")
    args = parser.parse_args()
    data = __getData(args.input_file) 
    watch = onMyWatch(data["utilityVM"]["path"])
    watch.run()
