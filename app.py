from flask import Flask, jsonify, request
from openai import OpenAI
from dotenv import load_dotenv
import os

app = Flask(__name__)
app.debug=True
load_dotenv()
client = OpenAI()
client.api_key=os.getenv("OPENAI_API_KEY")
@app.route('/', methods=['POST'])
def home():
  mymessage = request.get_json()["prompt"]
  response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": mymessage}
  ]
)
  return jsonify(response.choices[0].message.content)

if __name__ == '__main__':
    app.run(debug=True)