# conversions.py

import yaml
from pathlib import Path

# Locate and read the YAML file
YAML_PATH = Path(__file__).parent / "units.yaml"
with open(YAML_PATH, "r") as f:
    _all_units = yaml.safe_load(f)

# Extract the mapping
LENGTH_FACTORS = _all_units.get("length", {})
WEIGHT_FACTORS = _all_units.get("weight", {})
TEMPERATURE_UNITS = _all_units.get("temperature", {})


def convert(value: float, from_factor: float, to_factor: float) -> float:
    return value * (from_factor / to_factor)


def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    try:
        from_f = LENGTH_FACTORS[from_unit]
        to_f = LENGTH_FACTORS[to_unit]
    except KeyError as e:
        raise ValueError(f"Unsupported length unit: {e.args[0]}")
    return convert(value, from_f, to_f)


def convert_weight(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert `value` from `from_unit` to `to_unit` within WEIGHT_FACTORS (grams-based).
    Raises ValueError if an unsupported unit is provided.
    """
    try:
        from_f = WEIGHT_FACTORS[from_unit]
        to_f = WEIGHT_FACTORS[to_unit]
    except KeyError as e:
        raise ValueError(f"Unsupported weight unit: {e.args[0]}")
    return convert(value, from_f, to_f)


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert `value` between Celsius, Fahrenheit, and Kelvin.
    Steps:
    1) Convert input (`value`) to an intermediate in Celsius.
    2) Convert from Celsius to the target unit.
    Raises ValueError if `from_unit` or `to_unit` is unsupported.
    """
    # 1) Validate units exist
    if from_unit not in TEMPERATURE_UNITS:
        raise ValueError(f"Unsupported temperature unit: {from_unit}")
    if to_unit not in TEMPERATURE_UNITS:
        raise ValueError(f"Unsupported temperature unit: {to_unit}")

    # 2) Normalize input to Celsius:
    if from_unit == "celsius":
        celsius = value
    elif from_unit == "fahrenheit":
        celsius = (value - 32) * 5.0 / 9.0
    elif from_unit == "kelvin":
        celsius = value - 273.15
    else:
        # This should never trigger because we validated above
        raise ValueError(f"Unsupported temperature unit: {from_unit}")

    # 3) Convert from Celsius to target unit:
    if to_unit == "celsius":
        return celsius
    elif to_unit == "fahrenheit":
        return celsius * 9.0 / 5.0 + 32
    elif to_unit == "kelvin":
        return celsius + 273.15
    else:
        # Likewise, should be unreachable
        raise ValueError(f"Unsupported temperature unit: {to_unit}")
