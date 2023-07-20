# Help you to create json file and provide you to read json data
import json


def get_payload_auth():
    # read from the auth.json and return json
    file_data = open("src/resources/auth.json")
    data = json.loads(file_data)
    file_data.close()
    return data
