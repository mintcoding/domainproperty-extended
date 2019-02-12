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

        try:
            with open('apiclient_cred.txt') as cfile:
                credentials = cfile.readlines()
        except (FileNotFoundError, Exception) as e:
            raise e

        for i in credentials:
            if "clientid" in i:
                start_str = i.index("client_")
                try:
                    self.clientid = i[start_str:].rstrip().replace('"', '').replace("'", '')
                except (ValueError, Exception) as e:
                    raise e
            elif "clientpass" in i:
                start_str = i.index("secret_")
                try:
                    self.clientpass = i[start_str:].rstrip().replace('"', '').replace("'", '')
                except (ValueError, Exception) as e:
                    raise e

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

        try:
            auth_token = json.loads(token.content)["access_token"]
        except json.JSONDecodeError as e:
            raise ValueError(e)

        access_token = "Bearer " + auth_token
        url_header = {
            "Content-Type": "application/json",
            "Authorization": access_token
        }

        r = oauth.post(url=self.search_url, json=query_data, headers=url_header)
        r.raise_for_status()

        r_str = r.content.decode('utf-8')

        try:
            r_dict = json.loads(r_str)
        except json.JSONDecodeError as e:
            raise ValueError(e)

        return r_dict
