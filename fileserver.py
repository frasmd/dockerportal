import os
from apiserver import ImageApiServer
import shutil
#import magic

# Define a class for handling file server operations
class FileServer:
    def __init__(self, userinputs):
        # Constructor to initialize the FileServer object with user inputs
        self._folder = userinputs["utilityVM"]["path"]
        self._userinputs = userinputs

    def UploadImages(self, images):
        # Method to upload images to the API server
        imgobj = ImageApiServer(self._userinputs)
        for imagetar in images:
            print("Uploading image: {}".format(imagetar))
            self.__apiserverCall(imagetar, imgobj)
    
    def __getFiles(self):
        # Private method to get a list of files in the specified folder
        return [file for file in os.listdir(self._folder)]

    def __isDockerFile(self, image):
        # Private method to check if the file is a Dockerfile
        mime = magic.Magic(mime=True)
        file_mime_type = mime.from_file(image)
        return file_mime_type == 'text/x-dockerfile'
    
    def __apiserverCall(self, imagetar, imgobj):
        # Private method to make API server calls to load and push images
        with open("{}".format(imagetar), 'rb') as f:
            data = f.read()
            
        imagename = imgobj.load_image(data)
    
        tagging_status = imgobj.tag_repo(imagename, self._userinputs["harbor"]["reponame"])
    
        if tagging_status == 200:
            print("Tagging is done, Initiating image Push ...")
        
        response_status = imgobj.post_image(reponame=self._userinputs["harbor"]["reponame"], image=imagename)
        
        if response_status == 200:
            print("Image push successful.")
        
        self.__movetobackup(imagetar)
    
    def __movetobackup(self, imagename):
        # Private method to move the image to the backup folder
        backup_folder = "/root/backup"
        if not os.path.exists(backup_folder):
            os.makedirs(backup_folder)
        stripImageName = imagename.split("/")[-1]
        new_location = os.path.join(backup_folder, os.path.basename(stripImageName))
        shutil.move(imagename, new_location)
        print("Image {} moved to backup".format(imagename))
