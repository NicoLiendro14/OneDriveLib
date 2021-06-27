# OneDriveLib

A wrapper to One Drive (Microsoft Graph API)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the bot and how to install them

```
Python 3 (up to 3.6)
```
### Auth
You need these items: client_id, client_secret, tenant, redirect_uri. To get the basics about auth and get those items, read this [docs](https://github.com/reddit-archive/reddit/wiki/OAuth2). Depend of what kind of user are you, read [this](https://docs.microsoft.com/en-us/graph/auth-v2-user) or [this](https://docs.microsoft.com/en-us/graph/auth-v2-service)

### Example auth

1. Login to Azure Portal (App Registrations)
2. Create an application. Set a name.
3. Under "Supported account types" choose "Accounts from any organization directory and Microsoft personal accounts (e.g. Skype, Xbox, Outlook.com)".
4. Set the redirection uri (Web) : https://login.microsoftonline.com/common/oauth2/nativeclient and click on register.
5. Write down the application (client) ID. You will need this value.
6. In "Certificates and secrets", generate a new client secret. Set the expiration date to preferably never. Make a note of the value of the client secret created now. It will be hidden later.
7. Under API Permissions, add the following permissions, under delegated and application permissions: 
    1. Files.Readwrite.All


### Code example

```python
import OneDrive
client_id = "xxxxxxxxxxxxxx"
client_secret = "xxxxxxxxxxxxxx"
tenant = "xxxxxxxxxxxxxx"
redirect_uri = "localhost:5000"
path_credentials = "credentials.json"
onedrive = OneDrive.OneDrive(client_id, client_secret, tenant, redirect_uri, path_credentials)
auth_code = "xxxxxxxxx"
onedrive.get_token(auth_code, "code")
```

## Authors

- **Nicolás Liendro** - _Initial work_ - [GitLab](https://gitlab.com/NicoLiendro14),
  [GitHub](https://github.com/NicoLiendro14) and
  [LinkedIn](https://www.linkedin.com/in/nicol%C3%A1s-liendro-00248a178/)
