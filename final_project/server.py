from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET", "POST"])
def detect_emotion():
    if request.method == "POST":
        text_to_analyze = request.form['text']
    else:
        text_to_analyze = request.args.get('textToAnalyze')
        
    result = emotion_detector(text_to_analyze)

    response_text = (
        f"Para la declaración dada, la respuesta del sistema es "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} y "
        f"'sadness': {result['sadness']}. "
        f"La emoción dominante es {result['dominant_emotion']}."
    )

    return response_text

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
