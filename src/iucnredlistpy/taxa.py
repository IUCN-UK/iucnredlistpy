from .constants import API_BASE


class Taxa:
    def __init__(self, client):
        self.client = client

    def sis(self, sis_id):
        url = f"{API_BASE}taxa/sis/{sis_id}"
        print(url)
        return self.client.get(url)
