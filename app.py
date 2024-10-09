import os
from flask import Flask, request, jsonify, render_template, send_from_directory

def create_app(test_config=None):
    app = Flask(__name__)
    
    # Configuration
    app.config['IMG_FOLDER'] = 'images'
    
    # Ensure the folder exists
    if not os.path.exists(app.config['IMG_FOLDER']):
        os.makedirs(app.config['IMG_FOLDER'])
    
    @app.route('/')
    def home():
        photo_count = len(os.listdir(app.config['IMG_FOLDER']))
        photos = os.listdir(app.config['IMG_FOLDER'])
        return render_template('index.html', photo_count=photo_count, photos=photos)
    
    @app.route('/photo', methods=['POST'])
    def upload_photo():
        if 'image' not in request.files:
            return jsonify({"error": "No image part in the request"}), 400
        
        file = request.files['image']
        
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        
        if file:
            filepath = os.path.join(app.config['IMG_FOLDER'], file.filename)
            file.save(filepath)
            return jsonify({"message": "Image uploaded successfully!", "filepath": filepath}), 201
    
    @app.route('/photo/<filename>', methods=['GET'])
    def get_photo(filename):
        return send_from_directory(app.config['IMG_FOLDER'], filename)
    
    @app.route('/photo', methods=['GET'])
    def list_photos():
        files = os.listdir(app.config['IMG_FOLDER'])
        return jsonify({"photos": files})
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)