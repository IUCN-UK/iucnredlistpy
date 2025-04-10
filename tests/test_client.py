import iucnredlistpy


def test_get_biogeographical_realms(requests_mock):
    api_key = "fake-api-key"
    client = iucnredlistpy.Client(api_key=api_key)

    mock_url = f"https://api.iucnredlist.org/api/v4/biogeographical_realms"
    mock_response = {
        "biogeographical_realms": [
            {"description": {"en": "Afrotropical"}, "code": "0"},
            {"description": {"en": "Antarctic"}, "code": "1"},
            {"description": {"en": "Australasian"}, "code": "2"},
            {"description": {"en": "Indomalayan"}, "code": "3"},
            {"description": {"en": "Nearctic"}, "code": "4"},
            {"description": {"en": "Neotropical"}, "code": "5"},
            {"description": {"en": "Oceanian"}, "code": "6"},
            {"description": {"en": "Palearctic"}, "code": "7"},
        ]
    }

    requests_mock.get(mock_url, json=mock_response)

    result = client.biogeographical_realms.list()
    assert result == mock_response
