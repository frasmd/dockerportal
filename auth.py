import json, base64

# Define a class for handling authentication utilities
class AuthUtils:
    def __init__(self, user, password) -> None:
        # Constructor to initialize the user and password
        self._user = user
        self._password = password
    
    def _get_auth_cfg(self):
        # Private method to create authentication configuration
        auth_cfg = {
            "username": self._user,
            "password": self._password
        }
        # Return the encoded header using the encode_header method
        return self.encode_header(auth_cfg)

    def encode_header(self, auth_config):
        # Method to encode the authentication configuration as a base64 URL-safe string
        auth_json = json.dumps(auth_config).encode('ascii')
        return base64.urlsafe_b64encode(auth_json)