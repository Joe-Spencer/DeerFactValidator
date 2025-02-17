from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

@app.route('/validate', methods=['POST'])
def validate_fact():
    fact = request.json.get('fact')
    
    messages = [{
        "role": "system",
        "content": """You are a deer fact validator. Determine if the input contains factual information about deer species.
        Respond in JSON format: {"valid": boolean, "explanation": "your explanation"}
        Known deer species: white-tailed, red deer, caribou, reindeer, moose, water deer, muntjac, axis deer, 
        chital deer, elk, sika deer, eld's deer, sambar deer, visayan spotted deer, fallow deer, key deer, 
        mule deer, pampas deer, pudu, roe deer."""
    }, {
        "role": "user",
        "content": fact
    }]

    try:
        response = client.chat.completions.create(
            messages=messages,
            model="gpt-4",
            temperature=0.7
        )
        # Parse the response content as JSON
        result = json.loads(response.choices[0].message.content)
        return jsonify(result)
    except Exception as e:
        print(f"Error: {str(e)}")  # Add logging
        return jsonify({"valid": False, "explanation": str(e)}), 500

if __name__ == '__main__':
    print("Server starting on http://localhost:5000")
    app.run(port=5000, debug=True)