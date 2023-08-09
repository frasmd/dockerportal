import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler


class onMyWatch:
    watchDirectory = "D:\programming\dockerPortal"
    

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
        elif event.event_type == 'modified':
            print("Watchdog received modified event - %s"%event.src_path)

if __name__ == '__main__':
    watch = onMyWatch()
    watch.run()