from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth
import json


class Auth:
    clientid = ""
    clientpass = ""
    token_url = "https://auth.domain.com.au/v1/connect/token"
    scope = "api_listings_read api_listings_write"
    token_url_params = {"grant_type": "client_credentials",
                        "scope": "api_listings_read"
                        }
    search_url = "https://api.domain.com.au/v1/listings/residential/_search"

    def retrieve_credentials_from_file(self):
        with open('apiclient_cred.txt') as cfile:
            credentials = cfile.readlines()

        for i in credentials:
            if "clientid" in i:
                start_str = i.index("client_")
                self.clientid = i[start_str:].rstrip().replace('"', '').replace("'", '')
            elif "clientpass" in i:
                start_str = i.index("secret_")
                self.clientpass = i[start_str:].rstrip().replace('"', '').replace("'", '')
        return self.clientid, self.clientpass

    def retrieve_credentials(self):
        if not self.clientid and not self.clientpass:
            self.clientid, self.clientpass = self.retrieve_credentials_from_file()
        return self.clientid, self.clientpass

    def retrieve_approved_data(self, query_data):
        client = BackendApplicationClient(client_id=self.clientid)

        basic_auth = HTTPBasicAuth(self.clientid, self.clientpass)
        oauth = OAuth2Session(client=client)
        token = oauth.post(self.token_url, auth=basic_auth, data=self.token_url_params)

        auth_token = json.loads(token.content)["access_token"]
        access_token = "Bearer " + auth_token
        url_header = {
            "Content-Type": "application/json",
            "Authorization": access_token
        }
        r = oauth.post(url=self.search_url, json=query_data, headers=url_header)

        rstr = r.content.decode('utf-8')
        rdict = json.loads(rstr)
        return rdict
