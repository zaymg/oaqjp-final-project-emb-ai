''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request


# Import the sentiment_analyzer function from the package created: 
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    '''Retrieve the text to analyze from the request arguments'''
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the dominant emotion from the response
    dom_emo = response['dominant_emotion']
    if dom_emo is None:
        return_text = "Invalid text! Please try again."
    else:
        result_text = ''
        for k in response:
            if (k != 'dominant_emotion'):
                result_text = result_text + k + ": " + str(response[k]) + ", "
        #replace last comma with full stop
        result_text = result_text[0:len(result_text)-2] + ". "
            
        given_text = "For the given statement, the system response is"
        return_text = f"{given_text} {result_text} The dominant emotion is {dom_emo}."
    return return_text

@app.route("/")
def render_index_page():
    '''return the render index page'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)