UPLOAD_FOLDER = 'static/uploaded-images'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
        filename.split('.')[-1] in ALLOWED_EXTENSIONS
