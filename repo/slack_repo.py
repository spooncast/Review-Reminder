import json
import os
import requests

base_url = "https://slack.com/api"
auth_token = "Bearer " + os.environ.get('TOKEN_SLACK')
headers = {
    "Authorization": auth_token
}

def sendSlackMessage(message):
    channelName = os.environ.get('SLACK_CHANNEL_NAME')
    print(str(channelName))
    print(channelName)
    response = requests.post(
        base_url + "/chat.postMessage",
        headers=headers,
        data={
            "channel": "#" + channelName,
            "text": message,
            "unfurl_links": True
        }
    )
    print(f'Response Body: {json.dumps(response.json(), indent=2)}')
