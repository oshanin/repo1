from providers.auth.base_auth_class import Auth
from api.clients.web.urls.web import CIDEndpoints


class WebAPIClient:
    def __init__(self, auth_provider: Auth) -> None:
        self.auth_provider = auth_provider
        self.session = None

    def login(self, user):
        self.session = self.auth_provider.login(user)
        return self

    def get_dashboard_items(self):
        """
        Get full folder content for Layer Cake implementation
        :param folder_id: if None return root folder content
        :return: respond json
        """
        res = self.session.get(CIDEndpoints.dashboard)
        res.raise_for_status()
        return res.json()["files"]