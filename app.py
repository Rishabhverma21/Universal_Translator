from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

translator = Translator()

@app.route("/", methods=["GET", "POST"])
def home():
    original = ""
    translated = ""
    dest = "en"

    if request.method == "POST":
        text = request.form["text"]
        src_lang = request.form["src_lang"]
        dest_lang = request.form["dest_lang"]

        original = text
        dest = dest_lang

        if text.strip():
            result = translator.translate(text, src=src_lang, dest=dest_lang)
            translated = result.text

    return render_template(
        "index.html",
        original=original,
        translated=translated,
        dest=dest
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)