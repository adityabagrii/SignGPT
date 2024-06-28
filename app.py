from flask import Flask, render_template, request, redirect, url_for
from main import run_model
import os
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    for file in os.listdir('images'):
        os.remove(f'images/{file}')
    prompt = request.form['prompt']
    prompts = run_model(prompt)
    # save the prompts in a file
    with open('./templates/prompts.txt', 'w') as f:
        for prompt in prompts:
            f.write(prompt + '\n')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()