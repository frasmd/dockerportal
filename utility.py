class Utils:

    def _get_repository(self, url):
        return url.replace("http://","").replace("https://","").split(":",1)[0]

    def _repobuilder(self, url, repo_name, image):
        repository = self._get_repository(url)
        return "{}/{}/{}".format(repository, repo_name, image)
    
    def _url_builder(self, baseurl, api):
        return "{}{}".format(baseurl, api)