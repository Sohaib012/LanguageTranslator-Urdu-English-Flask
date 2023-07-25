from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    if textToTranslate:
        translated_text = english_to_french(textToTranslate)
        return translated_text
    else:
        return 'No text provided for translation'

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    if textToTranslate:
        translated_text = french_to_english(textToTranslate)
        return translated_text
    else:
        return 'No text provided for translation'

@app.route("/")
def renderIndexPage():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
