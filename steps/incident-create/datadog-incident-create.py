#!/usr/bin/env python
# create an incident in datadog from relay

import requests, os
from relay_sdk import Interface, Dynamic as D

relay = Interface()

api_key = relay.get(D.connection.apiKey),

payload = {
  'data': {
    'attributes': {
      'customer_impacted': relay.get(D.customer_impacted),
      'title': relay.get(D.title)
    },
    'type': 'incidents'
  }
}

url = 'https://api.datadoghq.com/api/v2/incidents'

r = requests.post(url, params={'api_key': api_key}, json=payload)

print('Sent request to Datadog API, got response: ', r.text)

r.raise_for_status()