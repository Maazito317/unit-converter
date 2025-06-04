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
        to_f   = WEIGHT_FACTORS[to_unit]
    except KeyError as e:
        raise ValueError(f"Unsupported weight unit: {e.args[0]}")
    return convert(value, from_f, to_f)