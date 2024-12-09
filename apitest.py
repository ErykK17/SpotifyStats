import json 
from dotenv import load_dotenv
import os
import base64
from requests import post

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

def get_access_token():
    client_auth_string = client_id + ":" + client_secret
    client_auth_bytes = base64.b64encode(bytes(client_auth_string, 'utf-8'))
    client_auth_b64 = client_auth_bytes.decode('utf-8')

    url = 'https://accounts.spotify.com/api/token'

    data = {'grant_type' : 'client_credentials'}

    headers = {
        'Authorization': "Basic " + client_auth_b64,
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    result = post(url, data=data, headers=headers)
    result_content = json.loads(result.content)
    token = result_content["access_token"]
    return token

auth_token = get_access_token()
print(auth_token)