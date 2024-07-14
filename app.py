from flask import Flask,render_template,request, jsonify
from py_file import url_backend as ur

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def analyze_url():
    
    if request.method == 'POST':
        print(request.form)  # Debug: Print the form data received
        url = request.form['url']
        print(url)  # Debug: Print the URL received
        is_valid, message = ur.imp(url)
        print(is_valid, message)  # Debug: Print the detection results
        return jsonify({'is_valid': is_valid, 'message': message})
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)

