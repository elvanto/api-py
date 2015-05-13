# Elvanto API Python Library

This library is all set to go with version 1.3.2 of the <a href="https://www.elvanto.com/api/" target="_blank">Elvanto API</a>.
This library works for both Python 2.7, and Python 3.4

## Authenticating

The Elvanto API supports authentication using either <a href="https://www.elvanto.com/api/getting-started/#oauth" target="_blank">OAuth 2</a> or an <a href="https://www.elvanto.com/api/getting-started/#api_key" target="_blank">API key</a>.

### What is This For?

* Quick summary
This is an API wrapper to use in conjunction with an Elvanto account. This wrapper can be used by developers to develop programs for their own churches, or to design integrations to share to other churches using OAuth authentication.
* Version 1.3.2

### Installation

#### PIP Installation

PIP is the preferred installation method.

```
python get-pip.py
pip install ElvantoAPI
```

#### Downloading

* Download
* Navigate to folder you downloaded the source
* `python setup.py install`

### For Authentication using an API Key:

First get your API key from Settings > Account Settings, then in the program:

```python
import ElvantoAPI
connection = ElvantoAPI.Connection(APIKey=string)
```

### For Authentication via OAuth 

First direct users to the required URL.
Use the `_AuthorizeURL` function to do this. The arguement `WebOrNon` is used to describe if you are developing a 
WebApp or a Non Web App (Ie, a program not in a browser) - For the most part OAuth would be used for Webapps

```python
import ElvantoAPI
URL = ElvantoAPI._AuthorizeURL(client_id, redirect_uri, scope, WebOrNon)
```

#### For Webapps

After the user has logged in, they will be sent back to the specified redirect_uri, with a code, and any state you specify.
For example:

```python
http://mywebapp.com/login/?code=string
```

The next step is to take this code, and get your access tokens. The code here is the code in the above URL.

```python
tokens = ElvantoAPI._GetTokens(client_id, client_secret, code, redirect_uri)
```

This will return a dict object of the form:

```python
{
	"access_token": "e1e8422f68d8cf3c44b6e3d4beb065722abf",
	"expires_in": 1209600,
	"refresh_token": "6d59273f6fb7671bf1bb79ac81c63c12bc73633421"
}
```

You can now create the connection object. The wrapper will be able to refresh the tokens used when needed.

```python
connection = ElvantoAPI.Connection(AccessToken=string, RefreshToken=string)
```

#### For Non-Webapps

After the user has logged in, they will be sent back to the specified redirect_uri, with a code. Unlike the WebApp method
this code will be behind a hash.

```python
http://mynonwebapp.com/login/#code=string&expiresin=int
```

Have the users copy this code into your app. This code will expire in the value provided by the integer, in seconds. 

You can now create the connection object. You can't have it automatically refresh the tokens though.

```python
connection = ElvantoAPI.Connection(AccessToken=string)
```

### Performing Calls

To perform a call, simply use the end point and any arguments required.

```python
connection._Post("people/getAll")
connection._Post("people/create", firstname = "John", lastname = "Smith")
```

All calls return a dict object, to indicate if it was successful or not.

If an argument is to be a JSON object, enter it as a Dict type object. Arrays can be entered simply as a list.

For example.
```python
search=connection._Post("people/search",search={"firstname":"John", "volunteer":"Yes"}, fields=["birthday","school_grade"])
```


An example response is as follows:

```python
{
    "status": "ok", 
    "generated_in": "0.035", 
    "people": {
        "on_this_page": 2, 
        "per_page": 1000, 
        "total": 2, 
        "page": 1, 
        "person": [
            {
                "username": "john.feeney", 
                "preferred_name": "", 
                "timezone": "", 
                "id": "7a411238-6fbc-11e0-bda8-de12be825216", 
                "archived": 0, 
                "family_id": "", 
                "family_relationship": "Other", 
                "last_login": "", 
                "email": "fee-ney-john@syllables.com", 
                "status": "Active", 
                "picture": "https://d5w68ic4qi8w5.cloudfront.net/assets/logo.png", 
                "school_grade": "", 
                "firstname": "John", 
                "lastname": "Feeney", 
                "phone": "", 
                "birthday": "1984-08-23", 
                "date_added": "2011-04-26 04:20:08", 
                "volunteer": 1, 
                "date_modified": "2015-02-26 05:07:06", 
                "admin": 0, 
                "country": "", 
                "mobile": "0456833923", 
                "contact": 0, 
                "category_id": "c37482a8-eb06-11e0-9229-ea942707ad51", 
                "deceased": 0
            }, 
            {
                "username": "john.hua", 
                "preferred_name": "", 
                "timezone": "", 
                "id": "7bcc31fa-6fbc-11e0-bda8-de12be825216", 
                "archived": 0, 
                "family_id": "", 
                "family_relationship": "Other", 
                "last_login": "", 
                "email": "johnhua@example.com", 
                "status": "Active", 
                "picture": "https://d5w68ic4qi8w5.cloudfront.net/assets/logo.png", 
                "school_grade": "12", 
                "firstname": "John", 
                "lastname": "Hua", 
                "phone": "", 
                "birthday": "1998-11-23", 
                "date_added": "2011-04-26 04:20:08", 
                "volunteer": 1, 
                "date_modified": "2015-02-26 05:07:06", 
                "admin": 0, 
                "country": "", 
                "mobile": "0451783968", 
                "contact": 0, 
                "category_id": "c37482a8-eb06-11e0-9229-ea942707ad51", 
                "deceased": 0
            }
        ]
    }
}
```


## Documentation

Documentation can be found on the <a href="https://www.elvanto.com/api/" target="_blank">Elvanto API website</a>.

## Updates

Follow our <a href="http://twitter.com/ElvantoAPI" target="_blank">Twitter</a> to keep up-to-date with changes in the API.

## Support

For bugs with the API Python Wrapper please use the <a href="https://github.com/elvanto/api-py/issues">Issue Tracker</a>.

For suggestions on the API itself, please <a href="http://support.elvanto.com/support/discussions/forums/1000123316" target="_blank">post in the forum</a> or contact us <a href="http://support.elvanto.com/support/tickets/new/" target="_blank">via our website</a>.