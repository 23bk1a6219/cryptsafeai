from flask import Flask, render_template, request, redirect, url_for, flash
import os
app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flash messages

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if file:
        # Simulate scanning logic here
        flash('File scanned successfully! No ransomware detected.', 'success')
    else:
        flash('No file selected.', 'danger')
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Render will pass PORT as env variable
    app.run(host='0.0.0.0', port=port, debug=True)
