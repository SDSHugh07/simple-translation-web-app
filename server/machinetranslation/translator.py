"""
docstring
"""

import os
import urllib
import urllib.request
import json

API_KEY='XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXXXXXXX'
URL_TEXT_TRANSLATION='https://api-translate.systran.net/translation/text/translate?'

def englishToFrench(english_text):
    """
    docstring
    """

    if english_text != "":
        params = urllib.parse.urlencode({'key':API_KEY, 'source':'en', 'target':'fr', 'withInfo':'false',
                                         'input':english_text})
        html = urllib.request.urlopen(URL_TEXT_TRANSLATION+params)
        translation_output = html.read().decode("utf-8")
        my_json = json.loads(translation_output)
        return my_json['outputs'][0]['output']
    return "Null input"


def frenchToEnglish(french_text):
    """
    docstring
    """

    if french_text != "":
        params = urllib.parse.urlencode({'key':API_KEY, 'source':'fr', 'target':'en', 'withInfo':'false',
                                         'input':french_text})
        html = urllib.request.urlopen(URL_TEXT_TRANSLATION+params)
        translation_output = html.read().decode("utf-8")
        my_json = json.loads(translation_output)
        return my_json['outputs'][0]['output']
    return "Null input"
