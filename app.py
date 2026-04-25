from flask import Flask, render_template, request, jsonify
from googletrans import Translator
import pyttsx3

app = Flask(__name__)

translator = Translator()

# text to speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 170)

voices = engine.getProperty("voices")
if voices:
    engine.setProperty("voice", voices[0].id)


def speak_text(text):
    engine.say(text)
    engine.runAndWait()


@app.route("/", methods=["GET", "POST"])
def home():
    translated_text = ""
    original_text = ""
    src_lang = "en"
    dest_lang = "hi"

    if request.method == "POST":
        original_text = request.form["text"]
        src_lang = request.form["src_lang"]
        dest_lang = request.form["dest_lang"]

        result = translator.translate(
            original_text,
            src=src_lang,
            dest=dest_lang
        )

        translated_text = result.text

    return render_template(
        "index.html",
        translated=translated_text,
        original=original_text,
        src=src_lang,
        dest=dest_lang
    )


@app.route("/speak", methods=["POST"])
def speak():
    text = request.form["speak_text"]

    if text:
        speak_text(text)

    return jsonify({"status": "success"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)