from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features

def analyze_emotion(text_to_analyze):
    api_key = "GGJCEAZmVaCzEufbXxH2voeWPb6orCy4FvTzx9wuI4sg"
    service_url = "https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/abae839a-ccd1-4ac0-99d5-6ba229ab8cd6"

    authenticator = IAMAuthenticator(api_key)
    nlu = NaturalLanguageUnderstandingV1(
        version='2021-09-01',  # Use the appropriate version
        authenticator=authenticator
    )
    nlu.set_service_url(service_url)

    emotion_options = EmotionOptions()
    features = Features(emotion=emotion_options)

    response = nlu.analyze(
        text=text_to_analyze,
        features=features,
    ).get_result()

    emotions = response['emotion']['document']['emotion']
    max_score = 0
    dominant_emotion = ""

    for emotion, score in emotions.items():
        if score > max_score:
            max_score = score
            dominant_emotion = emotion

    return emotions , dominant_emotion
