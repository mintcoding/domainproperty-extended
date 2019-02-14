# domainproperty-extended

!!! Users wishing to run this code in dev will need to run "python3 manage.py createcachetable" - currently working on a fix

Alternative search function for https://www.domain.com.au/

After cloning the repo and starting a local default Django instance, the app can be viewed at http://127.0.0.1:8000/extendedsearch

Since the app retrieves data from the Domain Property api (https://developer.domain.com.au/docs/endpoints), you will need to have a credentials file named apiclient_cred.txt located in the same dir as manage.py

The apiclient_cred file should follow this format:

clientid = {your client id}

clientpass = {your client secret}
  
TODO:
Add further search features

Improve Search Results page presentation

Store search form parameter lists in local db

Add test coverage

Create syndication service

