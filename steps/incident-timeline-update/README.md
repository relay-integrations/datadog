#incident-timeline-update

This step adds a timeline cell to a Datadog Incident.

This requires a Datadog connection with API and application keys.

Workflows should provide the following parameters in the spec:

* `incident_id`: (string) the unique internal identifier of the Incident to update. This is identified by `data.id` in responses from the Datadog `/v2/incidents` endpoint.
* `timeline_cell_content`: (string) Markdown-formatted text that represents the content of the timeline cell