import os
import cv2
import numpy as np
from flask import Flask, request, jsonify, render_template, send_from_directory
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)

# Set up a folder for uploaded files (ensure this folder exists or create it)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to detect QR code and extract data
def detect_qr_code(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)

    # Use OpenCV's QR code detector
    detector = cv2.QRCodeDetector()

    # Correct method to use is detectAndDecode()
    value, pts, qr_code = detector.detectAndDecode(gray_image)

    if value:
        return value  # If QR code is detected, return the data
    else:
        return "No QR code detected."

@app.route('/')
def index():
    return render_template('index.html')  # Render the HTML template for the frontend

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        # Save the file temporarily
        file.save(file_path)

        # Open the image
        image = Image.open(file_path)

        # Detect QR code and get its data
        try:
            qr_data = detect_qr_code(image)
            return jsonify({'qr_data': qr_data, 'image_url': f'/uploads/{filename}'})
        except Exception as e:
            return jsonify({'error': f'Error during QR code detection: {str(e)}'}), 500
    else:
        return jsonify({'error': 'Invalid file format'}), 400

# Route to serve the uploaded image
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    # Ensure the upload folder exists
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    # Run the Flask app
    app.run(debug=True, host="0.0.0.0", port=5000)
