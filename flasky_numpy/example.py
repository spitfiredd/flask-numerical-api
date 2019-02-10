'''Example script, flask server must be up and running
first, then run this script in a separate shell (if developing
locally).
'''

import json
import requests

login_url = 'http://localhost:5000/login'
url = 'http://localhost:5000/api/v1/markovchain'

creds = requests.post(
    login_url,
    json={'username': 'wally', 'password': 'west'}
).json()

transition_matrix = [
    [0.8, 0.19, 0.01],
    [0.2, 0.7, 0.1],
    [0.1, 0.2, 0.7]
]
states = ['Sunny', 'Rainy', 'Snowy']
current_state = 'Sunny'
num_obs = 10

payload = {
    'transition_matrix': json.dumps(transition_matrix),
    'states': json.dumps(states),
    'current_state': current_state,
    'num_obs': num_obs
}

headers = {
    'Authorization': "Bearer " + creds['access_token']
}

r = requests.get(url, data=payload, headers=headers).json()
print(r)
