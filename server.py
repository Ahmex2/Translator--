from flask import Flask, render_template, request
from translator import translate_english_to_french, translate_french_to_english

app = Flask(__name__, template_folder='/data/data/com.termux/files/home/downloads')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/french_to_english')
def route_french_to_english():
    text = request.args.get('text')
    translation = translate_french_to_english(text)
    return {'translation': translation}

@app.route('/english_to_french')
def route_english_to_french():
    text = request.args.get('text')
    translation = translate_english_to_french(text)
    return {'translation': translation}

if __name__ == '__main__':
    app.run(debug=True, port=5004)