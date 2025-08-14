from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from search_cli import search

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    summary, profile_pic_url = search(name=name)
    return jsonify(
    {
        "summary_and_facts": summary.to_dict(),
        "photoUrl": profile_pic_url
    }
)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)