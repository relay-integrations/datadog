#!/usr/bin/env python
# create an incident in datadog from relay

import requests, os
from relay_sdk import Interface, Dynamic as D

relay = Interface()

api_key = relay.get(D.connection.apiKey)
application_key = relay.get(D.connection.applicationKey)

payload = {
  'data': {
    'attributes': {
      'title': relay.get(D.title)
    },
    'type': 'incidents'
  }
}

url = 'https://api.datadoghq.com/api/v2/incidents'

r = requests.post(url, headers={'DD-API-KEY': api_key, 'DD-APPLICATION-KEY': application_key}, json=payload)

print('Sent request to Datadog API, got response: ', r.text)

r.raise_for_status()

incident = r.json()

relay.outputs.set("incident_id", incident['data']['id'])