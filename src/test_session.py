import json
from models.user_model import UserModel
from providers.auth.base_auth import BasicAuth
from api.clients.web.web import WebAPIClient
from providers.config.config import CONFIG

auth_provider = BasicAuth

user = UserModel(
    email=CONFIG.EMAIL,
    password=CONFIG.PASSWORD
    )

api_client = WebAPIClient(auth_provider)
api_client.login(user)
print(json.dumps(api_client.get_dashboard_items(), indent=4, sort_keys=True))