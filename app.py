from flask import Flask, request, render_template, redirect, url_for
from conversions import convert_length, LENGTH_FACTORS, convert_weight, WEIGHT_FACTORS

# 1) Instantiate the Flask application.
#    __name__ tells Flask where to look for templates & static files.
app = Flask(__name__)


# 2) Define a route for the root URL.
@app.route("/")
def home():
    # When someone visits "/", return this simple text.
    return redirect(url_for("length"))


@app.route("/length", methods=["GET", "POST"])
def length():
    result = None
    if request.method == "POST":
        # Parse the form data.
        try:
            value = float(request.form["value"])
            frm_unit = request.form["from_unit"]
            to_unit = request.form["to_unit"]

            # Perform the conversion.
            converted = convert_length(value, frm_unit, to_unit)

            # Format display
            result = f"{value:g} {frm_unit} = {converted:.2f} {to_unit}"
        except (ValueError, KeyError) as e:
            # Handle errors gracefully.
            result = f"Error: {str(e)}"
    return render_template(
        "length.html",
        result=result,
        units=LENGTH_FACTORS.keys()  # Pass available units to the template.
    )


@app.route("/weight", methods=["GET", "POST"])
def weight():
    result = None
    if request.method == "POST":
        # Parse the form data.
        try:
            value = float(request.form["value"])
            frm_unit = request.form["from_unit"]
            to_unit = request.form["to_unit"]

            # Perform the conversion.
            converted = convert_weight(value, frm_unit, to_unit)

            # Format display
            result = f"{value:g} {frm_unit} = {converted:.2f} {to_unit}"
        except (ValueError, KeyError) as e:
            # Handle errors gracefully.
            result = f"Error: {str(e)}"
    return render_template(
        "weight.html",
        result=result,
        units=LENGTH_FACTORS.keys()  # Pass available units to the template.
    )


@app.route("/temperature", methods=["GET", "POST"])
def temperature():
    # Same stub behavior until we implement these later
    return redirect(url_for("length"))

# 3) Run the app if this file is executed directly.
if __name__ == "__main__":
    # debug=True enables live reloading and better error messages.
    # host="0.0.0.0" makes the server accessible from outside the container (for Docker later).
    app.run(debug=True, host="0.0.0.0", port=5001)
