import json
import requests
from flask_babel import _
from app import app
import requests, uuid, json


def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or \
            not app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')

    subscription_key = app.config['MS_TRANSLATOR_KEY']
    endpoint = "https://api.cognitive.microsofttranslator.com"

    location = "westeurope"

    path = '/translate'

    params = {
        'api-version': '3.0',
        'from': source_language,
        'to': dest_language
    }

    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
        'text': text
    }]

    r = requests.post(constructed_url, params=params, headers=headers, json=body)

    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return json.loads(r.content.decode('utf-8-sig')) #.decode('utf-8-sig') json.loads(
    #return json.dumps(r, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))
