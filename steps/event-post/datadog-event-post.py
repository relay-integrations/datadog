#!/usr/bin/env python
# posts an event to datadog from relay

import requests, os
from relay_sdk import Interface, Dynamic as D

relay = Interface()

api_key = relay.get(D.connection.apiKey),

event_payload = {
  'source_type_name': 'relay',
  'title': relay.get(D.event_title),
  'text': relay.get(D.event_text),
  'alert_type': relay.get(D.event_type)
}

url = 'https://api.datadoghq.com/api/v1/events'

r = requests.post(url, params={'api_key': api_key}, json=event_payload)

print('Emitted event to Datadog API, got response: ', r.text)

if r.status.code != requests.codes.ok:
  exit(1)