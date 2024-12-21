from flask import Flask, render_template, request, jsonify
from scripts.LetterWriter import LetterWriter

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    job_description = request.form['job_description']
    resume = request.form['resume']
    letter_writer = LetterWriter()
    letter = letter_writer.generate_letter(job_description, resume)
    return jsonify({'letter': letter})

if __name__ == '__main__':
    app.run(debug=True)
