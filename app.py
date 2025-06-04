# app.py

from flask import Flask, render_template, request, redirect, url_for
from conversions import (
    convert_length, LENGTH_FACTORS,
    convert_weight, WEIGHT_FACTORS,
    convert_temperature, TEMPERATURE_UNITS
)

app = Flask(__name__)


def handle_conversion(category_name, factors_or_units, convert_fn):
    """
    Shared helper to process a form, run conversion, and render converter.html.
    - category_name: e.g. "Length Converter"
    - factors_or_units: an iterable of valid unit keys (for dropdowns)
    - convert_fn: a function(value, from_unit, to_unit) -> float
    """
    result = None
    if request.method == "POST":
        try:
            value = float(request.form["value"])
            frm_unit = request.form["from_unit"]
            to_unit = request.form["to_unit"]
            converted = convert_fn(value, frm_unit, to_unit)
            # Format with :g to trim trailing zeros
            result = f"{value:g} {frm_unit} = {converted:g} {to_unit}"
        except (ValueError, KeyError) as e:
            result = f"Error: {e}"

    return render_template(
        "converter.html",
        heading=category_name,
        units=factors_or_units,
        result=result,
        route_url=url_for(request.endpoint)
    )


@app.route("/length", methods=["GET", "POST"])
def length():
    return handle_conversion(
        "Length Converter",
        LENGTH_FACTORS.keys(),
        convert_length
    )


@app.route("/weight", methods=["GET", "POST"])
def weight():
    return handle_conversion(
        "Weight Converter",
        WEIGHT_FACTORS.keys(),
        convert_weight
    )


@app.route("/temperature", methods=["GET", "POST"])
def temperature():
    return handle_conversion(
        "Temperature Converter",
        TEMPERATURE_UNITS.keys(),
        convert_temperature
    )


@app.route("/")
def home():
    return redirect(url_for("length"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
