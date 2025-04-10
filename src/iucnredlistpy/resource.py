from .constants import API_BASE


class Resource:
    def __init__(self, client, resource_name):
        self.client = client
        self.resource_name = resource_name

    def all(self):
        url = f"{API_BASE}{self.resource_name}"
        response = self.client.session.get(url)
        if response.ok:
            return response.json()
        else:
            raise Exception(f"API Error: {response.status_code} - {response.text}")
