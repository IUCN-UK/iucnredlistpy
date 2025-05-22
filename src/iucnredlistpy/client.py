import requests
from .constants import RESOURCE_NAMES
from .resource import Resource
from .assessment import Assessment


class Client:
    def __init__(self, api_key):
        self.api_key = api_key
        self.session = self._initialize_session()
        self._define_resource_methods()
        self.assessment = Assessment(self)

    def get(self, url, params=None):
        response = self.session.get(url, params=params)
        if response.ok:
            return response.json()
        else:
            raise Exception(f"API Error: {response.status_code} - {response.text}")

    def _define_resource_methods(self):
        for name in RESOURCE_NAMES:

            def make_method(resource_name):
                def method(self):
                    attr_name = f"_{resource_name}"
                    if not hasattr(self, attr_name):
                        setattr(self, attr_name, Resource(self, resource_name))
                    return getattr(self, attr_name)

                return method

            setattr(self.__class__, name, property(make_method(name)))

    def _initialize_session(self):
        session = requests.Session()
        session.headers.update({"Accept": "*/*", "Authorization": self.api_key})
        return session
