import requests


class IUCNRedListClient:
    API_BASE = "https://api.iucnredlist.org/api/v4/"

    def __init__(self, api_key):
        self.api_key = api_key
        self.session = self._initialize_session()

    def get_biogeographical_realms(self):
        url = f"{self.API_BASE}biogeographical_realms"
        response = self.session.get(url)

        if response.ok:
            return response.json()
        else:
            raise Exception(f"API Error: {response.status_code} - {response.text}")

    def _initialize_session(self):
        session = requests.Session()
        session.headers.update({"Accept": "*/*", "Authorization": self.api_key})
        return session
