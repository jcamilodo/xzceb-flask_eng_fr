from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator", static_folder='static')

@app.route("/englishToFrench")
def englishToFrench():
    text_to_translate = request.args.get('textToTranslate')
    english_to_french = translator.english_to_french(text_to_translate)
    return english_to_french

@app.route("/frenchToEnglish")
def frenchToEnglish():
    text_to_translate = request.args.get('textToTranslate')
    french_to_english = translator.french_to_english(text_to_translate)
    return french_to_english

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
