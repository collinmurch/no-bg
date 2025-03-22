FROM python:3.12-slim

WORKDIR /app

# Install dependencies for rembg
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy project files first for better caching
COPY pyproject.toml ./

# Install the project in development mode
RUN pip install --no-cache-dir -e .

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p uploads processed

EXPOSE 8080

CMD ["python", "app.py"]