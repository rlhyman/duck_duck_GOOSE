from unittest import TestCase
import requests

class TestGet_response(TestCase):
    url_ddg = "https://api.duckduckgo.com"

    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")

    rsp_data = resp.json()

    assert "DuckDuckGo" in rsp_data["Heading"]
