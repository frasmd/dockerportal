import requests as re
from auth import AuthUtils as auth
from utility import Utils
import json
import re as regexsh

# Define a class for interacting with the Image API server
class ImageApiServer:
    
    def __init__(self, userinputs) -> None:
        # Constructor to initialize the ImageApiServer object with user inputs
        self._host = userinputs["utilityVM"]["ip"]
        self._port = userinputs["utilityVM"]["port"]
        self._harborIP = userinputs["harbor"]["ip"]
        self._harborUser = userinputs["harbor"]["user"]
        self._harborPass = userinputs["harbor"]["pass"]
        self._harborRepo = userinputs["harbor"]["reponame"]
        
    @property
    def baseurl(self):
        # Property to get the base URL for API server
        return "http://{host}:{port}".format(host=self._host, port=self._port)
    
    @property
    def repourl(self):
        # Property to get the repository URL for Harbor
        return "http://{host}".format(host=self._harborIP)

    def load_image(self, image_data=None):
        # Method to load an image to the API server
        api = "/images/load"
        utils = Utils()
        url = utils._url_builder(self.baseurl, api)
        print("URL Ready {0}, Posting the image".format(url))
        res = re.post(url, data=image_data, stream=True)
        resdata = json.loads(res.text)
        match = regexsh.search(
                    r'(^Loaded image ID: |^Loaded image: )(.+)$',
                    resdata['stream']
                )
        if match:
            image_name = match.group(2)
        return image_name

    def tag_repo(self, image=None, repository=None):
        # Method to tag an image in the repository
        api = "/v1.41/images/{name}/tag".format(name=image)
        utils = Utils()
        url = utils._url_builder(self.baseurl, api)

        params = {
            'repo': "{host}/{repo}/{image}".format(host=self._harborIP, repo=repository, image=image)
        }

        res = re.post(url, params=params)
        return res.status_code

    def post_image(self, reponame=None, tag=None, auth_config=None, image=None):
        # Method to post an image to the repository
        headers = {}
        utils = Utils()
        repotag = utils._repobuilder(self.repourl, reponame, image)
        api = "/v1.41/images/{image}/push".format(image=repotag)
        
        if auth_config is None:
            # If auth_config is not provided, create authentication header using harbor credentials
            authObj = auth(self._harborUser, self._harborPass)
            header = authObj._get_auth_cfg()
            
            if header:
                headers['X-Registry-Auth'] = header
        else:
            # If auth_config is provided, use it directly in the header
            headers["X-Registry-Auth"] = auth.encode_header(auth_config)

        url = utils._url_builder(self.baseurl, api)
        print("Pushing the images to: {}".format(repotag))
        res = re.post(url, headers=headers)
        for progress in res:
            decoded_status = progress.decode('UTF-8')
            print(decoded_status)
        return res.status_code