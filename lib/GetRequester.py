import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

        response = requests.get(URL)
        return response.content
    

def load_json(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
    return data

        