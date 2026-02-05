# Use an official lightweight Python image.
FROM python:3.11

# Set the working directory to /app.
WORKDIR /app

RUN python3  -m venv venv

# Copy the requirements file and install dependencies.
# Copying requirements first allows Docker to cache dependencies if they haven't changed.
COPY requirements.txt .
RUN ./venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code.
COPY . .
COPY .env .

# Run the application.
# Ensure your application listens on port 8000.
EXPOSE 8000
CMD ["./venv/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]