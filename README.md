# Background Remover App

A simple web application that removes backgrounds from images using the rembg Python package.

## Features

- Upload images (PNG, JPG, JPEG)
- Automatic background removal
- Side-by-side comparison of original and processed images
- Download processed images

## Tech Stack

- Backend: Flask (Python)
- Frontend: HTML, CSS, JavaScript
- Image Processing: rembg
- Package Management: uv
- Linting: ruff
- Containerization: Docker

## Setup and Installation

### Using Docker

1. Clone the repository
2. Build the Docker image:

```bash
docker build -t bg-remover .
```

3. Run the Docker container:

```bash
docker run -p 5000:5000 bg-remover
```

4. Access the application at http://localhost:5000

### Local Development

#### Using Makefile (Recommended)

1. Clone the repository
2. Set up the development environment:

```bash
make setup
```

3. Run the application:

```bash
make run
```

4. Access the application at http://localhost:5000

5. Other available commands:

```bash
make setup-uv   # Alternative setup using uv directly
make lint       # Run linting checks
make format     # Format code using ruff
make test       # Run tests
make clean      # Clean up temporary files
make run-docker # Build and run with Docker
make help       # Display all available commands
```

#### Using uv for Virtual Environment (Alternative)

[uv](https://github.com/astral-sh/uv) is a fast Python package installer and resolver that can also create virtual environments.

1. Clone the repository
2. Install uv if you don't have it already:

```bash
pip install uv
```

3. Create a virtual environment and install dependencies in one step:

```bash
uv venv
uv pip install -r requirements.txt
```

4. Activate the virtual environment:

```bash
# On Unix/macOS
source .venv/bin/activate

# On Windows
.venv\Scripts\activate
```

5. Run the application:

```bash
python app.py
```

6. Access the application at http://localhost:5000

#### Manual Setup (Traditional venv)

1. Clone the repository
2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies using uv:

```bash
pip install uv
uv pip install -r requirements.txt
```

4. Install ruff for linting:

```bash
uv pip install ruff
```

5. Run the application:

```bash
python app.py
```

6. Access the application at http://localhost:5000

## Usage

1. Click "Choose an image" to select an image from your computer
2. Click "Remove Background" to process the image
3. View the side-by-side comparison of original and processed images
4. Click "Download Result" to save the processed image
5. Click "Try Another Image" to process a different image

## License

MIT
