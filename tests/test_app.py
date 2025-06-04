import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# Test GET routes
def test_get_length_page(client):
    response = client.get("/length")
    assert response.status_code == 200
    assert b"Length Converter" in response.data


def test_get_weight_page(client):
    response = client.get("/weight")
    assert response.status_code == 200
    assert b"Weight Converter" in response.data


def test_get_temperature_page(client):
    response = client.get("/temperature")
    assert response.status_code == 200
    assert b"Temperature Converter" in response.data


# Test POST routes for correct conversions
def test_post_length_conversion(client):
    response = client.post("/length", data={
        "value": "20",
        "from_unit": "foot",
        "to_unit": "centimeter"
    })
    assert b"20 foot = 609.6 centimeter" in response.data


def test_post_weight_conversion(client):
    response = client.post("/weight", data={
        "value": "1000",
        "from_unit": "gram",
        "to_unit": "kilogram"
    })
    assert b"1000 gram = 1 kilogram" in response.data


def test_post_temperature_conversion(client):
    response = client.post("/temperature", data={
        "value": "0",
        "from_unit": "celsius",
        "to_unit": "fahrenheit"
    })
    assert b"0 celsius = 32 fahrenheit" in response.data
