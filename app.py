import os
import uuid

from flask import Flask, render_template, request, send_from_directory
from PIL import Image
from rembg import remove

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['PROCESSED_FOLDER'] = 'processed'

# Create necessary folders
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['PROCESSED_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    # Generate a unique filename
    original_filename = file.filename
    file_ext = os.path.splitext(original_filename)[1].lower()
    if file_ext not in ['.png', '.jpg', '.jpeg']:
        return 'Invalid file type', 400

    unique_filename = f"{uuid.uuid4()}{file_ext}"

    # Save the uploaded file
    upload_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
    file.save(upload_path)

    # Process the image
    input_image = Image.open(upload_path)
    output_image = remove(input_image)

    # Save the processed image
    output_filename = f"nobg_{unique_filename}"
    output_path = os.path.join(app.config['PROCESSED_FOLDER'], output_filename)
    output_image.save(output_path, format="PNG")

    return {'filename': output_filename}

@app.route('/processed/<filename>')
def processed_file(filename):
    return send_from_directory(app.config['PROCESSED_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
