# conversions.py

# 1) A mapping from unit name → “how many meters is one of these?”
LENGTH_FACTORS = {
    "millimeter": 0.001,
    "centimeter": 0.01,
    "meter":      1.0,
    "kilometer":  1000.0,
    "inch":       0.0254,
    "foot":       0.3048,
    "yard":       0.9144,
    "mile":       1609.34,
}


def convert(value: float, from_factor: float, to_factor: float) -> float:
    """
    Convert `value` from a unit with factor `from_factor` to one with `to_factor`.
    E.g., if from_factor=0.01 (cm→m) and to_factor=0.3048 (ft→m), then:
        value_cm * (0.01 / 0.3048) = value in feet.
    """
    return value * (from_factor / to_factor)


def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert `value` from `from_unit` to `to_unit` within LENGTH_FACTORS.
    Raises KeyError if a unit isn’t supported.
    """
    from_f = LENGTH_FACTORS[from_unit]
    to_f = LENGTH_FACTORS[to_unit]
    return convert(value, from_f, to_f)


def safe_convert_length(value, from_unit, to_unit):
    try:
        return convert_length(value, from_unit, to_unit)
    except KeyError as e:
        raise ValueError(f"Unsupported length unit: {e.args[0]}")
