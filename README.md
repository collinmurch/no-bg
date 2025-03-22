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
- Image Processing: rembg, Pillow
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
