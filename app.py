import os
import uuid
from pathlib import Path

from flask import Flask, render_template, request, send_from_directory
from PIL import Image
from rembg import remove


def create_app():
    app = Flask(__name__)

    app.config.update(
        UPLOAD_FOLDER=Path("uploads"),
        PROCESSED_FOLDER=Path("processed"),
        ALLOWED_EXTENSIONS={".png", ".jpg", ".jpeg"},
        DEBUG=True,
    )

    # Create necessary folders
    app.config["UPLOAD_FOLDER"].mkdir(exist_ok=True)
    app.config["PROCESSED_FOLDER"].mkdir(exist_ok=True)

    return app


app = create_app()


def allowed_file(filename):
    return os.path.splitext(filename)[1].lower() in app.config["ALLOWED_EXTENSIONS"]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/remove-bg", methods=["POST"])
def remove_bg():
    if "file" not in request.files:
        return "No file part", 400

    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400

    if not allowed_file(file.filename):
        return "Invalid file type", 400

    # Generate a unique filename
    file_ext = os.path.splitext(file.filename)[1].lower()
    unique_filename = f"{uuid.uuid4()}{file_ext}"

    # Save the uploaded file
    upload_path = app.config["UPLOAD_FOLDER"] / unique_filename
    file.save(upload_path)

    # Process the image
    input_image = Image.open(upload_path)
    output_image = remove(input_image)

    # Save the processed image
    output_filename = f"nobg_{unique_filename}"
    output_path = app.config["PROCESSED_FOLDER"] / output_filename
    output_image.save(output_path, format="PNG")

    return {"filename": output_filename}


@app.route("/processed/<filename>")
def processed_file(filename):
    return send_from_directory(app.config["PROCESSED_FOLDER"], filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
