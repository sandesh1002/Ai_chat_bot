from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = "your-openai-api-key"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    try:
        # Call OpenAI API to generate a response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use GPT-3.5-turbo model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        bot_response = response['choices'][0]['message']['content']
    except Exception as e:
        bot_response = "Sorry, I couldn't process your request. Please try again."
    
    return jsonify({"reply": bot_response})

if __name__ == '__main__':
    app.run(port=5000)