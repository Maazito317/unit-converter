from flask import Flask

# 1) Instantiate the Flask application.
#    __name__ tells Flask where to look for templates & static files.
app = Flask(__name__)


# 2) Define a route for the root URL.
@app.route("/")
def home():
    # When someone visits "/", return this simple text.
    return "Hello, World!"


# 3) Run the app if this file is executed directly.
if __name__ == "__main__":
    # debug=True enables live reloading and better error messages.
    # host="0.0.0.0" makes the server accessible from outside the container (for Docker later).
    app.run(debug=True, host="0.0.0.0", port=5001)
