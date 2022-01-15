import requests
from api.clients.web.http_session.cosmosid_http_session import CosmosHttpSession
from api.clients.web.urls.web import CIDEndpoints
from providers.auth.base_auth_class import Auth
from providers.config.config import CONFIG
from models.user_model import UserModel
from requests.auth import HTTPBasicAuth

class BasicAuth(Auth):
    DEFAULT_TOKEN_EXPIRE = CONFIG.DEFAULT_TOKEN_EXPIRE
    HEADER = 'X-Token'

    @staticmethod
    def login(user: UserModel, expires=None):
        # obtain 'expires' request parameter 
        # either from function call parameter
        # or from the default config value
        _expires = None
        if expires is not None:
            _expires = {"expires": expires}
        else:
            _expires = {"expires": BasicAuth.DEFAULT_TOKEN_EXPIRE}

        # POST actual login request
        r = requests.post(
            url=CONFIG.BASE_URL + CIDEndpoints.login,
            params=_expires,  
            auth=HTTPBasicAuth(user.email, user.password),
        )
        # raise error in case 400 status code or higher
        r.raise_for_status()

        # default session initialized
        session = CosmosHttpSession()

        # populate session parameters stored in properties
        session.user = user
        session.expires = r.json()["expires"]
        session.token = r.json()["token"]

        # add headers to work with server
        session.add_headers({BasicAuth.HEADER: session.token})

        return session       
 