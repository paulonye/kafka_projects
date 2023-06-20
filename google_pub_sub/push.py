"""This script is used to push notifications to slack using """

import os
import json
slack_webhook = os.getenv('slack_webhook')

def push_error(error: str):
    #convert the data to string
    push_data = json.dumps({'text': error})
    #print(push_data)
    os.system(f"curl -X POST --data '{push_data}' '{slack_webhook}' ")

if __name__ == '__main__':
    var  = {'code': 429, 'message': "Quota exceeded for quota metric 'Read requests' and limit \
            'Read requests per minute per user' of service 'sheets.googleapis.com' for consumer 'project_number:760429159638'."}
    x = var['message'].replace('\'', '').replace('.','')
    push_error(x)



