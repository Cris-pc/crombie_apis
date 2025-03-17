import requests
import unittest
import HtmlTestRunner
import json

BASE_URL = "https://petstore.swagger.io"


def test_delete_pets():
    url = f"{BASE_URL}/v2/pet/10"
    headers = {"accept": "application/json"}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 200
    json_response = response.json()
    print("Respuesta JSON:", json_response)

