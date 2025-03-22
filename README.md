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

4. Access the application at http://localhost:5000

### Local Development

1. Clone the repository

2. Run the application:

```bash
make run-docker
```

Optionally to run outside of a container:

```bash
make setup
make run
```


3. Access the application at http://localhost:8080

## Usage

1. Click "Choose an image" to select an image from your computer
2. Click "Remove Background" to process the image
3. View the side-by-side comparison of original and processed images
4. Click "Download Result" to save the processed image
5. Click "Try Another Image" to process a different image

## License

MIT
