# app.py

import joblib
from flask import Flask, request, jsonify
from utils import find_similarity

# Save the find_similarity function to a joblib file
joblib.dump(find_similarity, 'model.pkl')

app = Flask(__name__)

# Load the find_similarity function from the joblib file
find_similarity = joblib.load('model.pkl')

@app.route('/calculate_similarity', methods=['GET', 'POST'])
def calculate_similarity():
    data = request.get_json()
    text1 = data.get('text1', '')
    text2 = data.get('text2', '')
    
    similarity_score = find_similarity(text1, text2)
    
    response = {
        'similarity_score': similarity_score
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
