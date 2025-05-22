# conversions.py

import yaml
from pathlib import Path

# 1) Locate and read the YAML file
YAML_PATH = Path(__file__).parent / "units.yaml"
with open(YAML_PATH, "r") as f:
    _all_units = yaml.safe_load(f)

# 2) Extract the length mapping
LENGTH_FACTORS = _all_units.get("length", {})


def convert(value: float, from_factor: float, to_factor: float) -> float:
    return value * (from_factor / to_factor)


def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    try:
        from_f = LENGTH_FACTORS[from_unit]
        to_f = LENGTH_FACTORS[to_unit]
    except KeyError as e:
        raise ValueError(f"Unsupported length unit: {e.args[0]}")
    return convert(value, from_f, to_f)
