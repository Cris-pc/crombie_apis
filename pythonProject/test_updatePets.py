import requests
import unittest
import HtmlTestRunner
import json

BASE_URL = "https://petstore.swagger.io"


def test_update_pets():
    url = f"{BASE_URL}/v2/pet"
    payload = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available" }
    headers = {"accept": "application/json"}
    response = requests.put(url, json=payload, headers=headers)
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["status"] == "available"
    assert json_response["name"] == "doggie"
    print("Respuesta JSON:", json_response)

