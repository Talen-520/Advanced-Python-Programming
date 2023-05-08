'''
import sys
print(sys.executable)
C:\msys64\mingw64\bin\python.exe -m pip install openai
'''
from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "Y4omYKr3LnYqhggXd3M7T3BlbkFJ7dTX0WrUdX57IAp8C7ND"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return jsonify({'response': response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run(debug=True)
