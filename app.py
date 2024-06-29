from flask import Flask, render_template, request, redirect, url_for
from main import run_model
import os
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    for file in os.listdir('static/images'):
        os.remove(os.path.join('static/images', file))
    prompt = request.form['prompt']
    prompts = run_model(prompt)
    print(prompts)
    image_urls = [url_for('static', filename=f'images/{file}') for file in os.listdir('static/images')]
    image_urls = sorted(image_urls)
    print(image_urls)
    params = []
    for i in range(len(prompts)):
        params.append({'prompt': prompts[i], 'url': image_urls[i]})
    print(params)
    return render_template('generated.html', params=params)

if __name__ == '__main__':
    app.run(debug=True)