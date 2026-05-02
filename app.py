from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route("/", methods=["GET", "POST"])
def home():
    translated = ""
    original = ""
    src = "en"
    dest = "hi"

    if request.method == "POST":
        original = request.form["text"]
        src = request.form["src_lang"]
        dest = request.form["dest_lang"]

        result = translator.translate(original, src=src, dest=dest)
        translated = result.text

    return render_template("index.html",
                           translated=translated,
                           original=original,
                           src=src,
                           dest=dest)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)