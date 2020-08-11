#!/usr/bin/env python
# posts an event to datadog from relay

import requests, os
from relay_sdk import Interface, Dynamic as D

relay = Interface()

# this value needs to come from datadog 
incident_id = relay.get(D.incident_id)

# these are encrypted in the Connection
api_key = relay.get(D.connection.apiKey)
app_key = relay.get(D.connection.applicationKey)

# content of the message to post, in markdown
timeline_cell_content = relay.get(D.timeline_cell_content)

event_payload = {
  'data': {
    'type': 'incident_timeline_cells',
    'attributes': {
      'source': 'relay',
      'cell_type': 'markdown',
      'content': {
        'content': timeline_cell_content
      }
    }
}

url = 'https://api.datadoghq.com/api/v2/incidents/' + incident_id + '/timeline'

r = requests.post(url, params={'api_key': api_key, 'app_key': app_key}, json=event_payload)

print('Emitted event to Datadog API, got response: ', r.text)

r.raise_for_status()
