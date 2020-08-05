#!/usr/bin/env python

# posts an event to datadog from relay

from datadog import initialize, api
from relay_sdk import Interface, Dynamic as D

relay = Interface()

options = {
  'api_key': relay.get(D.connection.apiKey),
  'app_key': relay.get(D.connection.applicationKey)
}

initialize(**options)

event_payload = {
  source_type_name: "puppet",
  title: relay.get(D.event_title),
  text: relay_get(D.event_text),
  alert_type: relay_get(D.event_type)
}

api.Event.create(event_payload)

print('Emitted event to Datadog API: {}'.format(event_payload))
