# unit-converter

````markdown
# Flask Unit Converter

A simple Flask-based web application that converts between various units of measurement (length, weight, temperature). The app is fully data-driven (unit factors stored in `units.yaml`), includes unit tests, and is Dockerized for easy deployment.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Prerequisites](#prerequisites)
3. [Installation & Setup](#installation--setup)
4. [Running Locally](#running-locally)
5. [Testing](#testing)
6. [Docker Usage](#docker-usage)
7. [Project Structure](#project-structure)
8. [Contributing](#contributing)
9. [License](#license)

---

## Project Overview

This project provides:

- Three conversion categories:
  - **Length**: millimeter, centimeter, meter, kilometer, inch, foot, yard, mile
  - **Weight**: milligram, gram, kilogram, ounce, pound
  - **Temperature**: Celsius, Fahrenheit, Kelvin
- A simple HTML/CSS interface with a two-panel layout:
  - Left panel for form input (value, “from” unit, “to” unit)
  - Right panel to display the converted result
- Data-driven unit tables in `units.yaml` for easy maintenance or expansion
- Conversion logic isolated in `conversions.py`
- Unit tests for both conversion functions and Flask routes (using pytest)
- Dockerfile and `.dockerignore` to build and run the app in a container

---

## Prerequisites

Before you begin, ensure you have the following installed:

- **Git** (≥ 2.0)  
- **Python 3.12** (or any 3.7+ interpreter)  
- **pip** (package installer for Python)  
- **Docker** (for building and running the container; optional if running locally)  

---

## Installation & Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/<your-username>/unit-converter.git
   cd unit-converter
````

2. **Create a Python virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # On Windows: `.\venv\Scripts\activate`
   ```

3. **Install dependencies**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Verify the YAML file**
   The file `units.yaml` holds all unit definitions. You should see entries for `length`, `weight`, and `temperature`. No further action is needed here unless you want to add/modify units.

---

## Running Locally

1. **Activate your virtual environment** (if not already active)

   ```bash
   source venv/bin/activate
   ```

2. **Set Flask environment variables** (optional in development)

   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development      # Enables debug mode and auto-reload
   ```

3. **Start the Flask development server**

   ```bash
   flask run --host=0.0.0.0 --port=5001
   ```

   The app will be available at:

   * [http://localhost:5001/length](http://localhost:5001/length)
   * [http://localhost:5001/weight](http://localhost:5001/weight)
   * [http://localhost:5001/temperature](http://localhost:5001/temperature)

4. **Use the web interface**

   * Navigate to one of the above URLs.
   * Enter a numeric value, select the “From” unit and “To” unit, then click **Convert**.
   * The converted result appears on the right panel, with a **Reset** link that reloads the form.

---

## Testing

Unit tests cover both the conversion logic and the Flask routes.

1. **Ensure pytest is installed**

   ```bash
   pip install pytest
   ```

2. **Run all tests**

   ```bash
   pytest
   ```

   * You should see tests for `convert_length`, `convert_weight`, `convert_temperature`, and GET/POST route checks for `/length`, `/weight`, `/temperature`.
   * Test files are located under `tests/`. Pytest automatically reads `conftest.py` to configure the import path.

3. **Interpreting results**

   * A successful run shows “`n passed in …`”.
   * If any tests fail, the output will indicate which assertion did not match expectations, allowing you to debug.

---

## Docker Usage

A Dockerfile is provided to build and run the app inside a container.

### 1. Build the Docker image

From the project root (where `Dockerfile` and `.dockerignore` reside), run:

```bash
docker build -t unit-converter:latest .
```

* `unit-converter:latest` is the image tag; feel free to change it.
* The `.dockerignore` file excludes files/folders like `venv/`, `tests/`, and `__pycache__/` to keep the image minimal.

### 2. Run the container

Map port 5001 on your host to port 5001 in the container:

```bash
docker run --rm -p 5001:5001 unit-converter:latest
```

* **`--rm`** cleans up the container when it stops.
* Once running, open your browser to the same local URLs:

  * [http://localhost:5001/length](http://localhost:5001/length)
  * [http://localhost:5001/weight](http://localhost:5001/weight)
  * [http://localhost:5001/temperature](http://localhost:5001/temperature)

### 3. Production considerations

* In production, consider replacing the Flask development server with a production-grade WSGI server (e.g., Gunicorn). For example, modify the final `CMD` in your Dockerfile to:

  ```dockerfile
  CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]
  ```
* Pin your base image to a specific patch version (e.g., `python:3.12.3-slim`) to ensure reproducible builds over time.

---

## Project Structure

```
unit-converter/
├── .dockerignore            # Excludes unnecessary files from Docker build context
├── Dockerfile               # Defines how to build the Docker image
├── app.py                   # Flask application entrypoint and routes
├── conversions.py           # Unit-conversion logic (length, weight, temperature)
├── requirements.txt         # Python dependencies (Flask, PyYAML, etc.)
├── units.yaml               # Data file containing unit definitions/factors
├── templates/
│   ├── base.html            # Base layout with navigation bar
│   ├── length.html          # Length converter page (or shared converter.html)
│   ├── weight.html          # Weight converter page
│   └── temperature.html     # Temperature converter page
├── static/
│   └── css/
│       └── styles.css       # CSS for layout, form, and result panels
└── tests/
    ├── conftest.py          # Pytest configuration (adds project root to PYTHONPATH)
    ├── test_conversions.py  # Unit tests for conversion functions
    └── test_app.py          # Integration tests for Flask routes (GET & POST)
```

* **`app.py`** defines three routes: `/length`, `/weight`, `/temperature`. Each route handles both GET (show form) and POST (process form, display result).
* **`conversions.py`** contains:

  * `LENGTH_FACTORS`, `WEIGHT_FACTORS`, `TEMPERATURE_UNITS` (loaded from `units.yaml`)
  * `convert_length()`, `convert_weight()`, `convert_temperature()` helpers
* **`units.yaml`** drives all supported units. To add more (e.g., volume, area), simply append new mappings.
* **Tests** ensure correctness and prevent regressions.

---

## Contributing

Contributions are welcome! To contribute:

1. **Fork** the repository.
2. **Create a feature branch** (`git checkout -b feature/your-feature`).
3. **Make your changes**, then commit with clear, descriptive messages.
4. **Run tests** locally (`pytest`) to verify nothing breaks.
5. **Push** to your fork and open a **Pull Request** against the `main` branch.

Please adhere to existing code style, write meaningful tests for new functionality, and ensure all CI checks pass before merging.

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute as you see fit.

```
```


https://roadmap.sh/projects/unit-converter