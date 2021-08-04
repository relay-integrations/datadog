# datadog-step-event-post

This step posts an event to the Datadog event stream.

This requires a datadog connection with API and appplication keys.

Workflows should provide the following parameters in the spec:

* `event_title`: (string) the title for the event
* `event_text`: (string) the body of the event
* `event_type`: (string) one of: error, warning, info, success
