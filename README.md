# README #

To install, simply download the ElvantoAPI.py file into your project location, and simply import.

### What is this repository for? ###

* Quick summary
This is an API wrapper to use in conjunction with an Elvanto account. This wrapper can be used by developers to develop
programs for their own churches, or to design integrations to share to other churches using Oauth authentication.
* Version 1.0


###Installation

####Pip installation

The simplest way to install any python library, we recommend this method.

`pip install ElvantoAPI`

####Building from Source
* Download
* Navigate to folder you downloaded the source
* `python setup.py install`

###Without

### How do I get set up? ###


###For Authentication using an API Key:

First get your API key from Settings > Account settings, then in the program.

```python
import ElvantoAPI
connection = ElvantoAPI.Connection(APIKey=string)
```

###For Authentication via Oauth 

First direct users to the required URL.
Use the `_GetURL` function to do this. The arguement `WebOrNon` is used to describe if you are developing a 
WebApp or a Non Web App (Ie, a program not in a browser) - For the most part Oauth would be used for Webapps

```python
import ElvantoAPI
URL = ElvantoAPI._AuthorizeURL(client_id, redirect_uri, scope, WebOrNon)
```


####For Webapps
After the user has logged in, they will be sent back to the specified redirect_uri, with a code, and any state you specify.
For example:


`http://mywebapp.com/login/?code=string`

The next step is to take this code, and get your access tokens. The Code here is the code in the above URL.

```python
tokens = ElvantoAPI._GetTokens(client_id, client_secret, code, redirect_uri)
```

This will return a dict object of the form:

```python
{
  "access_token": "e1e8422f78d9cf3c44b6e3d4beb065833abf",
  "expires_in": 1209600,
  "refresh_token": "6d49263f6fb7671bf1bb79ac81c63c12bc62533221"
}
```

You can now create the connection object. The wrapper will be able to refresh the tokens used when needed.

```python
connection = ElvantoAPI.Connection(AccessToken=string, RefreshToken=string)
```

####For NonWebapps
After the user has logged in, they will be sent back to the specified redirect_uri, with a code. Unlike the WebApp method
this code will be behind a hash.

`http://mywebapp.com/login/#code=string&expiresin=int`

Have the users copy this code into your app. This code will expire in the value provided by the integer, in seconds. 

You can now create the connection object. You can't have it automatically refresh the tokens though.

```python
connection = ElvantoAPI.Connection(AccessToken=string)
```


###Performing Calls

To perform a call, simply use the end point and any arguments required.

```python
connection.post("people/getAll")
connection.post("people/create", firstname = "John", lastname = "Smith")
```

All calls return a dict object, to indicate if it was successful or not.


If the call has an argument that is an object, such as the search field, it needs to be a dict. For example:

```python
search=connection.post("people/search", search={"firstname":"John", "locations":"Nashville"})
```

If the argument is a list, simply use the list. For example:


```python
AllPeople = connection.post("people/getAll", fields=["gender","family"])
```
An example response is as follows:

```python
{
    "status": "ok", 
    "generated_in": "0.128", 
    "people": {
        "on_this_page": 765, 
        "per_page": 1000, 
        "total": 765, 
        "page": 1, 
        "person": [
            {                
                "username": "example.person", 
                "preferred_name": "", 
                "timezone": "", 
                "id": "02509a6a-8309-11e3-9edb-094b5ffbcb0b", 
                "archived": 0, 
                "family_id": "", 
                "family_relationship": "Other", 
                "last_login": "", 
                "email": "", 
                "status": "Active", 
                "picture": "https://d5w68ic4qi8w5.cloudfront.net/img/default_gravatar.png", 
                "firstname": "Example", 
                "lastname": "Person", 
                "phone": "", 
                "date_added": "2014-01-22 02:00:46", 
                "volunteer": 0, 
                "date_modified": "2015-02-26 05:07:06", 
                "admin": 0, 
                "country": "", 
                "mobile": "", 
                "contact": 0, 
                "category_id": "c374a4b8-eb06-11e0-9229-ea942707ad51", 
                "deceased": 0
            },
            ... (764 other responses not shown)
        ]
    }
}
```


###Expired Tokens (Oauth Only)

When using an Ouath authentication, the access tokens expire after a given amount of time. If you're developing
a Web App, the simplest method to do this is to include the `refresh_token` value in your arguments when calling
the Connection object. For example:

```python
import ElvantoAPI
c = ElvantoAPI.Connection(AccessToken=tokens['access_tokens'],RefreshToken=tokens['refresh_token'])
```

When an API call is made, if the response object indicates that the token had expired, it will then automatically
refresh the token for you.

If you're developing a Non Web App, the object that is returned to you will indicate that the token is expired, and 
you will have to direct users to obtain a new token, by logging in with the URL provided in the `_AuthorizeURL` command.

### Contribution guidelines ###

To help contribute to this wrapper, send an email support@elvanto.com

### Who do I talk to? ###

Full API Documentation is available [at our website.](https://www.elvanto.com/api "Elvanto API")

For all enquiries, send an email to support@elvanto.com