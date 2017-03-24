import requests
import configRead
from requests_oauthlib import OAuth1
from flask import session

# POST for qbo sandbox
def post(req_data):
    payload = req_data['payload']
    url = req_data['url']
    tokens = configRead.get_consumer_tokens()
    try:
        access_tokens = session.get('qbo_token')
        access_key = access_tokens[0]
        access_sec = access_tokens[1]
    except (IndexError,KeyError) as e:
        access_key = None
        access_sec = None
        print 'ERROR: '+ e
        
    auth = OAuth1(tokens['consumer_key'], tokens['consumer_sec'], access_key, access_sec)
    headers = {'Accept': 'application/json', 'content-type': 'application/json; charset=utf-8'}
    req = requests.post(url, auth=auth, headers=headers, json=payload)

    req_status_content = {}
    req_status_content['status_code'] = req.status_code
    req_status_content['content'] = req.content
    return req_status_content
