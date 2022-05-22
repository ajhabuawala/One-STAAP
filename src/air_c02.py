import requests
import json
import config

API = "https://www.carboninterface.com/api/v1/"
API_KEY = "QiV4C990CEJBzABcGLOhRg"


headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}


def get_co2_data(mot, distance_travelled, weight):

    authenticate()
    data = {
        "type": "shipping",
        "weight_value": weight,
        "weight_unit": "kg",
        "distance_value": distance_travelled,
        "distance_unit": "km",
        "transport_method": mot,
    }

    json_data = json.dumps(data)
    url = f"{API}/estimates"
    response = requests.post(url, data=json_data, headers=headers)

    rd = response.json()["data"]
    value = rd["attributes"][f"carbon_kg"]
    return value


def authenticate():
    """Authenticate API connection"""
    url = f"{API}/auth"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers)
