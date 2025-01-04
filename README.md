# PhotoVault

PhotoVault is a lightweight photo library application built with Flask and Waitress. It allows users to upload, view, and download photos via a simple web interface and provides API endpoints for programmatic interaction.

## Features

- **Upload Photos**: Easily upload photos to your library.
- **View Photos**: Browse your photo library with a clean, responsive gallery.
- **Download Photos**: Download photos directly from the gallery.
- **REST API**: Use API endpoints for uploading, retrieving, and listing photos programmatically.

---

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [API Endpoints](#api-endpoints)
4. [Gallery Preview](#gallery-preview)
5. [Contributing](#contributing)
6. [License](#license)

---

## Installation and Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/PhotoVault.git
   cd PhotoVault
2. Run the application:
   ```bash
   py ./WSGU.py

   The application will start on http://127.0.0.1:1935.

## Usage
### Web Interface
Navigate to http://127.0.0.1:1935 in your browser.
Use the "Upload Photo" form to add new photos.
View the uploaded photos in the gallery.
Click on a photo to download it.

## API Endpoints
---
|Method	|Endpoint	        |Description
|-----|--------------------|--------------
|POST	|/photo	            |Upload a photo
|GET	|/photo	            |List all uploaded photos
|GET	|/photo/<filename>	|Retrieve a specific photo

## Contributing
Contributions are welcome! Here's how you can help:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/your-feature-name).
3. Make your changes and commit them (git commit -am 'Add some feature').
4. Push to the branch (git push origin feature/your-feature-name).
5. Open a pull request.
