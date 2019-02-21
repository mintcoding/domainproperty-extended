from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth
import json
from django.core.cache import cache


class DomainApi:

    token_url = "https://auth.domain.com.au/v1/connect/token"
    scope = "api_listings_read api_listings_write"
    token_url_params = {"grant_type": "client_credentials",
                        "scope": "api_listings_read"
                        }
    search_url = "https://api.domain.com.au/v1/listings/residential/_search"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.clientid = ""
        self.clientpass = ""
        self.auth_token = ''
        self.cached_token = ''
        self.access_token = "Bearer " + self.auth_token
        self.client = BackendApplicationClient(client_id=self.clientid)
        self.basic_auth = HTTPBasicAuth(self.clientid, self.clientpass)
        self.oauth = OAuth2Session(client=self.client)
        self.response_data_raw = []
        self.response_data = []

    def retrieve_credentials_from_file(self):
        # See README.md for recommended file format
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

    def retrieve_credentials(self):
        # If instance credentials (clientid, clientpass) are empty, call retrieve_credentials_from_file method
        if not self.clientid and not self.clientpass:
            self.retrieve_credentials_from_file()

    def retrieve_approved_data(self, query_data):
        # query_data is a dict in the format specified here:
        # https://developer.domain.com.au/docs/endpoints/listings/listings_detailedresidentialsearch
        self.retrieve_token()
        self.access_token = "Bearer " + self.auth_token
        url_header = {
            "Content-Type": "application/json",
            "Authorization": self.access_token
        }

        r = self.oauth.post(url=self.search_url, json=query_data, headers=url_header)
        r.raise_for_status()
        self.response_data_raw = r.json()
        self.prepare_response_data()

        return self.response_data

    def retrieve_token(self):
        # Checks cache for OAuth token; if none, request new one
        self.client = BackendApplicationClient(client_id=self.clientid)
        self.basic_auth = HTTPBasicAuth(self.clientid, self.clientpass)
        self.oauth = OAuth2Session(client=self.client)

        self.cached_token = cache.get('cached_token')
        if not self.cached_token:
            print("Get new token")
            token = self.oauth.post(self.token_url, auth=self.basic_auth, data=self.token_url_params)
            try:
                token_content = json.loads(token.content)
                self.auth_token = token_content["access_token"]
            except json.JSONDecodeError as e:
                raise ValueError(e)

            try:
                token_expires_in = token_content['expires_in']
                print(str(token_expires_in))
            except Exception as e:
                raise e

            try:
                cache.set('cached_token', self.auth_token, timeout=(token_expires_in - 500))
            except Exception as e:
                raise e
        else:
            print("Use cached token")
            self.auth_token = self.cached_token

    def prepare_response_data(self):
        # Parses the raw JSON response to return required data only to the display template
        for l_iter in self.response_data_raw:
            if l_iter:
                listing_dict = {}
                try:
                        listing_dict.update({'displayPrice': l_iter['listing']['priceDetails'].get('displayPrice', 0)})
                        listing_dict.update({'propertyType': l_iter['listing']['propertyDetails'].get('propertyType', "")})
                        listing_dict.update({'bathrooms': l_iter['listing']['propertyDetails'].get('bathrooms', 0)})
                        listing_dict.update({'bedrooms': l_iter['listing']['propertyDetails'].get('bedrooms', 0)})
                        listing_dict.update({'carspaces': l_iter['listing']['propertyDetails'].get('carspaces', 0)})
                        listing_dict.update({'displayableAddress': l_iter['listing']['propertyDetails'].get('displayableAddress', "")})
                        listing_dict.update({'landArea': l_iter['listing']['propertyDetails'].get('landArea', 0)})
                        listing_dict.update({'listingSlug': l_iter['listing'].get('listingSlug', "")})
                        media = l_iter['listing'].get('media')
                        if media:
                            listing_dict.update({'pic': media[0]['url']})
                except (ValueError, Exception) as e:
                    raise e
                self.response_data.append(listing_dict)
