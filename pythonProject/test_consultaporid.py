import requests
import unittest
import HtmlTestRunner

BASE_URL = "https://petstore.swagger.io"

#consuta mascota existente.
def test_consulta_id():
    url = f"{BASE_URL}/v2/pet/100"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_response = response.json()
    print("Respuesta JSON:", json_response)

def test_consulta_id_no_existente():
    url = f"{BASE_URL}/v2/pet/11111100"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 404
    json_response = response.json()
    assert json_response["message"] == "Pet not found"
    print("Respuesta JSON:", json_response)
