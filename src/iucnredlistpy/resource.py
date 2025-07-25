from .constants import API_BASE


class Resource:
    def __init__(self, client, resource_name):
        self.client = client
        self.resource_name = resource_name

    def list(self):
        url = f"{API_BASE}{self.resource_name}"
        return self.client.get(url)

    def find(self, id, query={}):
        url = f"{API_BASE}{self.resource_name}/{id}"

        return self.client.get(url, query)
