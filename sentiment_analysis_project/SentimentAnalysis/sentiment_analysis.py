import requests
import json

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    try:
        response = requests.post(url, json=myobj, headers=header)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        response_text_into_json = response.json()
        if response.status_code == 200:
            label = formatted_response['documentSentiment']['label']
            score = formatted_response['documentSentiment']['score']
        elif response.status_code == 500:
            label = None
            score = None
        return {'label': label, 'score': score}
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Error making the request: {e}")
        return {"error": "Network error"}
    except json.JSONDecodeError as e:
        # Handle JSON decoding errors
        print(f"Error decoding JSON: {e}")
        return {"error": "JSON decoding error"}
    except KeyError as e:
        # Handle missing keys in the JSON response
        print(f"Key not found in JSON: {e}")
        return {"error": "Key not found in JSON"}