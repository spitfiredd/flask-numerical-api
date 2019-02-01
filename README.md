# Flask API for Numerical Computing

Simple exmaple for numerical restAPI endpoints.

## Getting Started

Make sure pipenv is install and run `pipenv install` to get your env up and running.

Set Flask Env viables, on windows,

```
set FLASK_APP=flasky_numpy.app
set FLASK_ENV=development
```

Run `flask shell` and then,

```
>>> db.create_all()
>>> user = User(username='wally', password='west')
>>> db.session.add(user)
>>> db.session.commit()
```

Start flask app with `flask run`.

In a separate script (or copy/paste to a separate terminal session),

```
import json
import requests

login_url = 'http://localhost:5000/login'
url = 'http://localhost:5000/api/v1/markovchain'

login_payload = {'username': 'wally', 'password': 'west'}
login_request = requests.post(login_url, json=login_payload).json()
access_token = login_request['access_token']

transition_matrix = [
    [0.8, 0.19, 0.01],
    [0.2,  0.7,  0.1],
    [0.1,  0.2,  0.7]
]
states=['Sunny', 'Rainy', 'Snowy']
current_state='Sunny'
num_obs=10

payload = {
    'transition_matrix': json.dumps(transition_matrix),
    'states': json.dumps(states),
    'current_state': current_state,
    'num_obs': num_obs
}

headers = {
    'Authorization': "Bearer " + access_token
}

r = requests.get(url, data=payload, headers=headers).json()
print(r)
```