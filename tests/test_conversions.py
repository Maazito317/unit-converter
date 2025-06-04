import pytest
from conversions import convert_length, convert_weight, convert_temperature


# Tests for length conversion
@pytest.mark.parametrize("value, from_unit, to_unit, expected", [
    (100, "centimeter", "meter", 1.0),
    (1, "mile", "kilometer", pytest.approx(1.60934, rel=1e-6)),
    (12, "inch", "foot", 1.0),
    (5, "meter", "centimeter", 500.0),
])
def test_convert_length(value, from_unit, to_unit, expected):
    assert convert_length(value, from_unit, to_unit) == expected


# Tests for weight conversion
@pytest.mark.parametrize("value, from_unit, to_unit, expected", [
    (1000, "gram", "kilogram", 1.0),
    (16, "ounce", "pound", 1.0),
    (1, "kilogram", "gram", 1000.0),
    (2.20462, "pound", "kilogram", pytest.approx(1.0, rel=1e-5)),
])
def test_convert_weight(value, from_unit, to_unit, expected):
    assert convert_weight(value, from_unit, to_unit) == expected


# Tests for temperature conversion
@pytest.mark.parametrize("value, from_unit, to_unit, expected", [
    (0, "celsius", "fahrenheit", 32.0),
    (32, "fahrenheit", "celsius", pytest.approx(0, abs=1e-6)),
    (300, "kelvin", "celsius", pytest.approx(26.85, abs=1e-2)),
    (100, "celsius", "kelvin", pytest.approx(373.15, abs=1e-6)),
    (212, "fahrenheit", "kelvin", pytest.approx(373.15, abs=1e-2)),
])
def test_convert_temperature(value, from_unit, to_unit, expected):
    assert convert_temperature(value, from_unit, to_unit) == expected
