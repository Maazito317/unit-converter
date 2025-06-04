# 1) Use an official lightweight Python runtime as a parent image
FROM python:3.12-slim

# 2) Set a working directory inside the container
WORKDIR /usr/src/app

# 3) Copy only requirements first to leverage Docker layer caching
COPY requirements.txt ./

# 4) Install system dependencies (if any). For a simple Flask app, none are strictly needed
#    but ensure pip is up to date and install wheel (optional).
RUN pip install --upgrade pip wheel \
    && pip install --no-cache-dir -r requirements.txt

# 5) Copy the rest of the application code
COPY . .

# 6) Expose the port Flask will run on
EXPOSE 5001

# 7) Set environment variables
#    - PYTHONUNBUFFERED ensures logs appear immediately
#    - FLASK_APP tells Flask which module to run
#    - FLASK_RUN_HOST makes Flask listen on 0.0.0.0 inside the container
ENV PYTHONUNBUFFERED=1 \
    FLASK_APP=app.py \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_RUN_PORT=5001

# 8) Define the default command to run the app
#    Using Flask CLI for development; in production you’d use gunicorn or uwsgi
CMD ["flask", "run"]
