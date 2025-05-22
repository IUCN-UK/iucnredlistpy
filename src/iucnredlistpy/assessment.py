from .constants import API_BASE


class Assessment:
    def __init__(self, client):
        self.client = client

    def find(id):
        url = f"{API_BASE}assessment/{id}"
        return self.client.get(url)
