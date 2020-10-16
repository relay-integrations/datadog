# event-fired 

This [Datadog](https://datadog.com) trigger fires when an event is fired.

For more information about Datadog webhooks, check out the [documentation](https://docs.datadoghq.com/integrations/webhooks/).

## Data Emitted

| Name | Data type | Description |
|------|-----------|-------------|
| body | string | Body text of the event |
| last_updated | datetime | Last time the event was updated |
| event_type | string | Type of event |
| title | string | Title of event |
| date | datetime | Date event occurred |
| id | integer | Event ID |  

## Example Raw Data

```
{
  "body": "%%%\n@webhook-relay-test\n@webhook-relay-prod-demo\n@webhook-relay\n\nTest notification triggered by kenaz@puppet.com.\n\n\n\nThe monitor was last triggered at Wed Jun 03 2020 20:43:04 UTC.\n\n- - -\n\n[[Monitor Status](https://app.datadoghq.com/monitors#18692904?)] · [[Edit Monitor](https://app.datadoghq.com/monitors#18692904/edit)]\n%%%",
  "last_updated": "1591216985000",
  "event_type": "service_check",
  "title": "[Triggered] [TEST] Host Cluster Alert",
  "date": "1591216985000",
  "org": {
    "id": "415600",
    "name": "Puppet"
  },
  "id": "5485379890863845239"
}
```
