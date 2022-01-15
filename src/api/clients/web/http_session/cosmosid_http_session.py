
from providers.config.config import CONFIG

import urllib.parse
import requests
# from requests.adapters import HTTPAdapter

class CosmosHttpSession:
    def __init__(self):
        self.user = None
        self._http_session = None
        self.expires = None
        self.token = None
    
    @property
    def http_session(self):
        if self._http_session is None:
            self._http_session = requests.Session()

        return self._http_session

    def add_headers(self, additional_headers):
        self.http_session.headers.update(additional_headers)
        return self

    def _prepare_url(self, url):
        return urllib.parse.urljoin(CONFIG.BASE_URL, url)       

    def get(self, url_path, *args, **kwargs):
        return self.http_session.get(url=self._prepare_url(url_path), *args, **kwargs)

    def put(self, url_path, *args, **kwargs):
        return self.http_session.put(url=self._prepare_url(url_path), *args, **kwargs)

    def post(self, url_path, *args, **kwargs):
        return self.http_session.post(url=self._prepare_url(url_path), *args, **kwargs)

    def delete(self, url_path, *args, **kwargs):
        return self.http_session.delete(url=self._prepare_url(url_path), *args, **kwargs)
