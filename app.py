from flask import Flask, render_template, request, redirect, url_for, flash
import os
import requests
app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flash messages

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if file:
        files = {'file': (file.filename, file.stream, file.mimetype)}
        ml_api_url = 'https://abcd1234.ngrok.io/predict'  # your API URL
        
        try:
            response = requests.post(ml_api_url, files=files, timeout=10)
            prediction = response.json().get('result', 'Unknown')
            
            # Display result based on prediction
            if prediction == "No Threat Detected":
                flash(f"✅ {prediction}", "success")
            elif prediction == "Ransomware Detected":
                flash(f"🚨 {prediction}", "danger")
            else:
                flash(f"⚠️ {prediction}", "warning")
        except Exception as e:
            flash(f"API Error: {str(e)}", "danger")
    else:
        flash('No file selected.', 'danger')
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Render will pass PORT as env variable
    app.run(host='0.0.0.0', port=port, debug=True)
