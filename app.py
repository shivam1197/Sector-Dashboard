from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import pandas as pd
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "headers": "content-type"}})


@app.route('/get_file_names', methods=['GET'])
def get_file_names():
    file_names = os.listdir('Stocks')
    print(file_names)
    response = jsonify(file_names)

    return response


@app.route('/pie_chart_data', methods=['POST'])
def pie_chart_data():
    folder_path = 'Stocks'
    file_name = request.json.get('file_name')
    try:
        file_path = os.path.join(folder_path, file_name)
        data = pd.read_excel(file_path)
        required_columns = ['Issuer Name', 'Market Cap']

        if all(col in data.columns for col in required_columns):
            extracted_data = data[required_columns].dropna()
            json_data = extracted_data.to_dict(orient='list')
            # print(json_data)
            return jsonify(json_data)
        else:
            return jsonify({'error': 'Columns not found in the sheet'})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
