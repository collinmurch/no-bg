FROM python:3.11-slim

WORKDIR /app

# Install dependencies for rembg
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install uv

# Copy requirements file
COPY requirements.txt .

# Install dependencies with uv
RUN uv pip install --system -r requirements.txt

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p uploads processed

EXPOSE 5000

CMD ["python", "app.py"]