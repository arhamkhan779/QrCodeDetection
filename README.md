# QR Code Decoder

## Demo Video

Watch the demo of the application here:  
[![Watch the demo](https://img.youtube.com/vi/zmxgpEPUWH8/0.jpg)](https://youtu.be/zmxgpEPUWH8)

## Overview

The QR Code Decoder is a web application built using Streamlit that allows users to upload images containing QR codes. The application processes the uploaded image, decodes the QR code, and displays the decoded information alongside the processed image.

## Project Structure

```
.
├── .gitignore
├── LICENSE
├── MainApplication.py
├── README.md
├── main
└── requirements.txt
```

## Getting Started

### Prerequisites

- Python 3.x
- pip
- [Anaconda](https://www.anaconda.com/products/distribution) (recommended for package management)

### Required Libraries

To run this project, you will need to install the following libraries:

- Streamlit
- OpenCV-Python
- Pillow
- NumPy
- PyZbar

You can install these libraries using pip by running the following command:

```bash
pip install streamlit opencv-python pillow numpy pyzbar
```

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/qr-code-decoder.git
   cd qr-code-decoder
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv env_name
   source env_name/bin/activate  # On Windows use `env_name\Scripts\activate`
   ```

3. **Install Required Libraries**:  
   Use the command provided above to install the required libraries.

### Running the Application

1. **Start the Streamlit Application**:
   Run the following command to start the Streamlit application:
   ```bash
   streamlit run MainApplication.py
   ```

## Workflow

1. **Image Upload**:
   - Users can upload an image file (JPEG or PNG) containing a QR code.

2. **Image Processing**:
   - The uploaded image is processed to convert it to an OpenCV format, resized for better UI fit, and prepared for QR code decoding.

3. **QR Code Decoding**:
   - The application uses the PyZbar library to decode the QR code and extract the encoded information.

4. **Display Results**:
   - The decoded text and the processed image are displayed side by side, allowing users to view the QR code and its contents simultaneously.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request to enhance the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Special thanks to the contributors and tools that facilitated the project, including libraries for image processing and QR code decoding.
