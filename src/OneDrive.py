import requests
import json


class OneDrive:
    def __init__(self, *, client_id, client_secret, tenant, redirect_uri, path_credentials):
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = 'files.readwrite.all offline_access'
        self.redirect_uri = redirect_uri
        self.tenant = tenant
        self.access_token = None
        self.refresh_token = None
        self.path_credentials = path_credentials

    def get_token(self, auth_code, grant_type):
        url, params = self.build_request(auth_code, grant_type)
        response = requests.post(url, data=params)
        json_response = json.loads(response.text)
        self.access_token = json_response['access_token']
        new_refresh_token = json_response['refresh_token']
        self.refresh_token = new_refresh_token
        return json_response

    def build_request(self, auth_code, grant_type):
        params = {
            'client_id': self.client_id,
            'scope': self.scope,
            'redirect_uri': self.redirect_uri,
            'grant_type': grant_type,
            'client_secret': self.client_secret,
        }
        params.update(auth_code)
        url = 'https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token'.format(tenant=self.tenant)
        return url, params

    def create_tokens_file(self, credentials):
        with open(self.path_credentials, 'w') as outfile:
            json.dump(credentials, outfile)

    def get_items(self):
        headers = {
            'Authorization': 'Bearer ' + self.access_token
        }
        url = "https://graph.microsoft.com/v1.0/me/drive/root/children"
        response = requests.get(url, headers=headers)
        print(response.text)
        return response




