# domainproperty-extended

Alternative search function for https://www.domain.com.au/

After cloning the repo and following the instructions below, the app can be viewed on your machine at http://127.0.0.1:8000/extendedsearch

## Instructions:

1)  Since the app retrieves data from the Domain Property api (https://developer.domain.com.au/docs/endpoints), you will need to have a credentials file named apiclient_cred.txt located in the same dir as manage.py

* The apiclient_cred file should follow this format:

  + clientid = {your client id}

  + clientpass = {your client secret}

2)  run "python manage.py migrate"

3)  run "python3 manage.py loaddata ./extendedsearch/fixtures/SortKey.json"

4)  run "python manage.py runserver"
  
### TODO:

Add further search features

Improve Search Results page presentation

Store search form parameter lists in local db

Add test coverage

Create syndication service

