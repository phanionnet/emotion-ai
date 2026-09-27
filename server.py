"""
Emotion Detection Flask Application.

This module sets up a web server that provides an endpoint for detecting
emotions in a given text using the EmotionDetection package.
"""

from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze the provided text and return the emotion scores.

    Retrieves 'textToAnalyze' from the request arguments, passes it to the
    emotion_detector, and formats the result into a readable string.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)

    if emotions is None:
        return "Invalid text! Please try again!"

    dominant_emotion = max(emotions, key=emotions.get)
    emotions['dominant_emotion'] = dominant_emotion

    return (
        f"For the given statement, the system response is 'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, "
        f"'joy': {emotions['joy']} and 'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {emotions['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """
    Render and serve the main index HTML page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
