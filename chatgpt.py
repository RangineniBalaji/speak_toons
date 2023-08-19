

from ASR import asr
import json
import requests

f = asr()

text = f.text

class chatgpt(object):
    def __init__(self):
        
        
        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZTdmYjAxNDctNWQ2OC00MTVlLTg1OTMtNzZhYzU4ZGQxYjJlIiwidHlwZSI6ImFwaV90b2tlbiJ9.w4BYXRL_aa_PlhAUExp7hmdwsNL23Sj3E2xVWC1oxl0"}
        
        url = "https://api.edenai.run/v2/text/generation"
        payload = {
            "providers": "openai,cohere",
            "text": text,
            "temperature": 0.2,
            "max_tokens": 250
        }
        
        response = requests.post(url, json=payload, headers=headers)
        
        result = json.loads(response.text)
        #print(result)
        
        if 'openai' in result and 'generated_text' in result['openai']:
            self.gpt_response = result['openai']['generated_text']
        else:
            print("Generated text not found in the response.")
            return
        

if __name__ == '__main__':
    chatgpt()