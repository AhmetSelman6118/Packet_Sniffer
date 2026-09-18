import os
from flask import Flask, request, render_template_string, send_from_directory

app = Flask(__name__)

HTML_FORM = """
<!DOCTYPE html>
<html>
<head><title>Local Lab Login</title></head>
<body>
    <h2>Login Page (Local Lab Experiment)</h2>
    <img src="/image/Img02.png" alt="Lab Image" width="300"><br><br>
    <form method="POST" action="/login">
        Username: <input type="text" name="username"><br><br>
        Password: <input type="password" name="password"><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_FORM)

@app.route('/login', methods=['POST'])
def login():
    return "Data Received Locally!"

@app.route('/image/<filename>')
def serve_image(filename):
    # FIX: Explicitly get the directory where web.py is located
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(base_dir, filename)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)