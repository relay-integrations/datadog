#!/usr/bin/env python
# extracts an incident's id, given its friendly name

import requests, os
from relay_sdk import Interface, Dynamic as D

relay = Interface()

# the user supplies this as part of the workflow run
public_id = int(relay.get(D.public_id))

headers = {
  'DD-API-KEY': relay.get(D.connection.apiKey),
  'DD-APPLICATION-KEY': relay.get(D.connection.applicationKey),
  'Accept': 'application/json'
}

url = 'https://api.datadoghq.com/api/v2/incidents/'

r = requests.get(url, headers=headers)

r.raise_for_status()

print('Emitted event to Datadog API, got response: ', r.text, "\n\n")

incident_id = 'not_found'

incidents = r.json()

for incident in incidents['data']:
  if incident['attributes']['public_id'] == public_id:
    incident_id = incident['id']
    print('Matched ', public_name, ' to ', incident_id)

if incident_id == 'not_found':
  print("Reached end of incidents with no match")
  exit(1)
else:
  relay.outputs.set("incident_id",incident_id)