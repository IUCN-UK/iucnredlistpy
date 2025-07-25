from .constants import API_BASE, TAXA_LEVELS
from .resource import Resource


class Taxa:
    def __init__(self, client):
        self.client = client
        self._resource_cache = {}

        self._define_resource_methods()

    def sis(self, sis_id):
        url = f"{API_BASE}taxa/sis/{sis_id}"
        return self.client.get(url)

    def _define_resource_methods(self):
        for name in TAXA_LEVELS:

            def make_method(resource_name):
                def method(self):
                    attr_name = f"_{resource_name}"
                    if not hasattr(self, attr_name):
                        setattr(
                            self,
                            attr_name,
                            Resource(self.client, f"taxa/{resource_name}"),
                        )
                    return getattr(self, attr_name)

                return method

            setattr(self.__class__, name, property(make_method(name)))
