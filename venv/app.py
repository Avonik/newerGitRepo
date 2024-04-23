# backend.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_input', methods=['GET'])
def get_input():
    if request.method == 'GET':
        input_value = request.args.get('input_value')
        # Process input_value as needed
        response = {'message': f'Received GET input: {input_value}'}
        return jsonify(response)

@app.route('/post_input', methods=['POST'])
def post_input():
    if request.method == 'POST':
        data = request.get_json()
        input_value = data['input_value']
        # Process input_value as needed
        response = {'message': f'Received POST input: {input_value}'}
        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
