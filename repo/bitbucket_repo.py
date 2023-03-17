import os
import requests
import json

base_url = "https://api.bitbucket.org/2.0/repositories/spooncast/spooncast-android"
auth_token = "Bearer " + os.environ.get('TOKEN_BITBUCKET')
headers = {
  "Accept": "application/json",
  "Authorization": auth_token
}

def getPullRequests():
    response = requests.request(
        "GET",
        base_url + "/pullrequests",
        headers=headers
    )
    
    return json.loads(response.text)['values']


def getPullRequest(prId):
    response = requests.request(
        "GET",
        base_url + "/pullrequests/" + str(prId),
        headers=headers
    )
    
    return json.loads(response.text)