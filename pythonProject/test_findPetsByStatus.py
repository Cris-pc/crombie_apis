import requests
import unittest
import HtmlTestRunner

BASE_URL = "https://petstore.swagger.io"

#consuta mascota disponible.
def test_consulta_pet_available():
    url = f"{BASE_URL}/v2/pet/findByStatus?status=available"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_response = response.json()
    print("Respuesta JSON:", json_response)

#consuta mascota pending.
def test_consulta_pet_pending():
    url = f"{BASE_URL}/v2/pet/findByStatus?status=pending"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_response = response.json()
    print("Respuesta JSON:", json_response)

# consuta mascota sold.
def test_consulta_pet_sold():
    url = f"{BASE_URL}/v2/pet/findByStatus?status=sold"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_response = response.json()
    print("Respuesta JSON:", json_response)

