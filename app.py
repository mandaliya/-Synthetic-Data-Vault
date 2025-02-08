# app.py
from sdv import SDV
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/generate', methods=['GET'])
def generate_data():
    # Example SDV usage
    sdv = SDV()
    synthetic_data = sdv.generate(num_rows=100)
    return jsonify(synthetic_data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)