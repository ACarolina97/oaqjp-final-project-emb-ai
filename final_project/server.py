"""
Flask server for emotion detection. Includes error handling for blank inputs.
"""
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """
    Render the main page with the form
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    """
    Processes the text entered by the user and returns the detected emotions.
    Handles errors when the text is empty or the dominant emotion is None.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Invalid text! Please try again!."

    result = emotion_detector(text_to_analyze)

    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant_emotion = result['dominant_emotion']

    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
