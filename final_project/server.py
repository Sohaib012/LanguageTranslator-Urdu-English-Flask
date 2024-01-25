from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToUrdu")
def englishToUrdu():
    textToTranslate = request.args.get('textToTranslate')
    if textToTranslate:
        translated_text = english_to_urdu(textToTranslate)
        return translated_text
    else:
        return 'No text provided for translation'

@app.route("/UrduToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    if textToTranslate:
        translated_text = urdu_to_english(textToTranslate)
        return translated_text
    else:
        return 'No text provided for translation'

@app.route("/")
def renderIndexPage():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
