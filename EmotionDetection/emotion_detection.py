'''Import the requests library to handle HTTP requests'''
import requests  
'''Import json library to format the output'''
import json

def emotion_detector(text_to_analyze):
    '''emotion_detector function accept input "text_to_analyze" and analyze it using Watson AI Library'''
    # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }  
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)  
    if(response.status_code == 400):
        #create emotion_dict with None values
        emotion_dict = dict({'anger':None, 'disgust':None, 'fear':None, 'joy':None, 'sadness':None, 'dominant_emotion':None})
    else:
        #format the response text to json and dictionary
        formatted_response = json.loads(response.text)
        emotion_dict = formatted_response['emotionPredictions'][0]['emotion']
        #find the dominant emotion
        dominant_emotion = max(emotion_dict,key=emotion_dict.get)
        #add dominant emotion to dictionary
        emotion_dict['dominant_emotion'] = dominant_emotion
    return emotion_dict

