# datadog-trigger-event-fired 

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

## Example

```
parameters:
  body:
    default: ""
  last_updated:
    default: ""
  event_type:
    default: ""
  title:
    default: ""
  date:
    default: ""
  id:
    default: ""

triggers:
- name: datadog-event
  source:
    type: webhook
    image: relaysh/datadog-trigger-event-fired:latest
  binding:
    parameters:
      id: !Data id
      last_updated: !Data last_updated
      event_type: !Data event_type
      title: !Data title
      date: !Data date 
      body: !Data body
```