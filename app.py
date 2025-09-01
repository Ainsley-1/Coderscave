from flask import Flask, request, jsonify
from flask_cors import CORS
import urllib.parse
import requests

app = Flask(__name__)  # Fixed: __name__ instead of _name_
CORS(app)

@app.route('/generate_recipe', methods=['GET'])
def generate_recipe():
    recipe_name = request.args.get('recipe_name')
    budget = request.args.get('budget', '10')
    region = request.args.get('region', 'global')

    if not recipe_name:
        return jsonify({'error': 'Missing recipe_name parameter'}), 400

    prompt = f"Suggest 4 simple, low-cost, high-nutrition recipes with {recipe_name} for {region}. Ensure the total cost does not exceed ${budget}. Prioritize the cheapest available ingredients like rice, lentils, and vegetables. Provide: 1. A brief description 2. A complete list of ingredients with measurements and estimated cost per serving 3. Step-by-step cooking instructions 4. Any serving suggestions. Format with clear section headings."

    encoded_prompt = urllib.parse.quote(prompt)
    ai_url = f"https://genini-mu.vercel.app/api/gemini-text?text={encoded_prompt}"

    print(f"Calling AI API with URL: {ai_url}")

    try:
        response = requests.get(ai_url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get('success'):
            result = data.get('result')
            if not isinstance(result, str) or not result.strip():
                return jsonify({'error': 'Invalid or empty recipe data from AI API'}), 500
            return jsonify({'result': result})
        else:
            return jsonify({'error': 'AI API returned unsuccessful response'}), 500
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Request error: {str(e)}'}), 500
    except ValueError as e:
        return jsonify({'error': f'JSON parsing error: {str(e)}'}), 500

@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No JSON data received'}), 500
        
    recipe_name = data.get('recipe_name')
    ingredients = data.get('ingredients')
    instructions = data.get('instructions')

    if not all([recipe_name, ingredients, instructions]):
        return jsonify({'error': 'Missing required fields'}), 400

    return jsonify({'message': 'Recipe submitted successfully'}), 200

if __name__ == '__main__':  # Fixed: __name__ and __main__ with double underscores
    app.run(port=5000)