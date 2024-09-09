from flask import Flask, request, jsonify, render_template, send_from_directory
import os

app = Flask(__name__)

# Folder where uploaded photos are stored
IMG_FOLDER = 'images'
app.config['IMG_FOLDER'] = IMG_FOLDER

# Ensure the folder exists
if not os.path.exists(IMG_FOLDER):
    os.makedirs(IMG_FOLDER)

# Route to display how many photos are available on the home page
@app.route('/')
def home():
    # Count the number of images in the upload folder
    photo_count = len(os.listdir(app.config['IMG_FOLDER']))
    photos = os.listdir(app.config['IMG_FOLDER'])
    return render_template('index.html', photo_count=photo_count, photos=photos)

# Route to upload a photo (POST request)
@app.route('/photo', methods=['POST'])
def upload_photo():
    if 'image' not in request.files:
        print("No image part in the request")
        return jsonify({"error": "No image part in the request"}), 400

    file = request.files['image']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        filepath = os.path.join(app.config['IMG_FOLDER'], file.filename)
        file.save(filepath)
        return jsonify({"message": "Image uploaded successfully!", "filepath": filepath}), 201

# Route to retrieve a photo by filename (GET request)
@app.route('/photo/<filename>', methods=['GET'])
def get_photo(filename):
    return send_from_directory(app.config['IMG_FOLDER'], filename)

# Route to list all photos (GET request)
@app.route('/photo', methods=['GET'])
def list_photos():
    files = os.listdir(app.config['IMG_FOLDER'])
    return jsonify({"photos": files})

if __name__ == '__main__':
    app.run(debug=True)
