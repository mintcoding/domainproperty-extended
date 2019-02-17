from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth
import json
from django.core.cache import cache


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

        oauth, auth_token = self.retrieve_token()

        access_token = "Bearer " + auth_token
        url_header = {
            "Content-Type": "application/json",
            "Authorization": access_token
        }

        r = oauth.post(url=self.search_url, json=query_data, headers=url_header)
        r.raise_for_status()
        r_str = r.content.decode('utf-8')
        r_dict = {}
        if len(r_str.strip()) > 2:
            try:
                r_dict = json.loads(r_str)
            except json.JSONDecodeError as e:
                raise ValueError(e)

        return r_dict

    def retrieve_token(self):

        client = BackendApplicationClient(client_id=self.clientid)
        basic_auth = HTTPBasicAuth(self.clientid, self.clientpass)
        oauth = OAuth2Session(client=client)

        cached_token = cache.get('cached_token')
        print("cached_token: " + str(cached_token))
        if not cached_token:
            print("Get new token")
            token = oauth.post(self.token_url, auth=basic_auth, data=self.token_url_params)
            try:
                token_content = json.loads(token.content)
                auth_token = token_content["access_token"]
            except json.JSONDecodeError as e:
                raise ValueError(e)

            try:
                token_expires_in = token_content['expires_in']
                print(str(token_expires_in))
            except Exception as e:
                raise e

            try:
                cache.set('cached_token', auth_token, timeout=(token_expires_in - 500))
            except Exception as e:
                raise e
        else:
            print("Use cached token")
            auth_token = cached_token

        return oauth, auth_token
