import requests
import unittest
import HtmlTestRunner
import json

BASE_URL = "https://petstore.swagger.io"


def test_add_pets():
    url = f"{BASE_URL}/v2/pet"
    payload = {
               "id": 122,
               "category": {
               "id": 0,
               "name": "string"
               },
               "name": "doggie-ecuador",
               "photoUrls": [
               "string"
               ],
               "tags": [
              {
               "id": 0,
              "name": "string"
               }
            ],
           "status": "available"
    }
    headers = {"accept": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 200
    json_response = response.json()
    print("Respuesta JSON:", json_response)


def test_add_pets_error():
    url = f"{BASE_URL}/v2/pet/"
    payload = {
               "id": "AA",
               "category": {
               "id": "AA",
               "name": "string"
               },
               "name": "doggie-ecuador",
               "photoUrls": [
               "string"
               ],
               "tags": [
              {
               "id": "AA",
              "name": "string"
               }
            ],
           "status": "available"
    }
    headers = {"accept": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 500
    json_response = response.json()
    print("Respuesta JSON:", json_response)