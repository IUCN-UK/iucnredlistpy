import iucnredlistpy


def test_assessment_find(requests_mock):
    api_key = "fake-api-key"
    client = iucnredlistpy.Client(api_key=api_key)

    mock_url = "https://api.iucnredlist.org/api/v4/assessment/123"
    mock_response = {
        "assessment_id": 123,
        "assessment_date": "2023-01-27T00:00:00.000Z",
        "year_published": "2024",
    }

    requests_mock.get(mock_url, json=mock_response)

    result = client.assessment.find(123)
    assert result == mock_response
