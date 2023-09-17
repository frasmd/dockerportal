# Import the required classes and modules
from apiserver import ImageApiServer
from fileserver import FileServer
import yaml
from yaml.loader import SafeLoader
import argparse
from eventmanager import onMyWatch

# Check if the script is being run as the main module
if __name__ == '__main__':

    # Parse command-line arguments using argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", dest="input_file", required=True, help="Path to input YAML file.")
    args = parser.parse_args()

    # Open the input YAML file and load its content using the SafeLoader
    with open(args.input_file,"r") as f:
        data = yaml.load(f, Loader=SafeLoader)

    watch = onMyWatch()
    watch.run()

    images = []

    # Create a FileServer object and pass the YAML data to it
    fobj = FileServer(data)

    # Call the UploadImages() method of the FileServer object to upload images
    fobj.UploadImages(images)

    # Print a message indicating that all images are uploaded in the target
    print("All the images are uploaded in the target.")