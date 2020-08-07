# datadog-step-event-post

This step posts an event to the Datadog event stream.

This requires a datadog connection with API and User keys.

Workflows should provide the following parameters in the spec:

* `event_title`: (string) the title for the event
* `event_text`: (string) the body of the event
* `event_type`: (string) one of: error, warning, info, success

Example usage:

```yaml
parameters:
  event_payload:
  event_title:
    default: An event from Relay
  event_text:
    default: Override this from the body
  event_type:
    default: info

steps:
  - name: send-event
    image: relaysh/datadog-step-event-post
    spec:
      connection:  !Connection {type: "datadog", name: "my-datadog-keys"}
      event_title: !Parameter event_title
      event_text:  !Parameter event_text
      event_type:  !Parameter event_type
```
