# datadog-step-incident-timeline-update

This step adds a timeline cell to a Datadog Incident.

This requires a Datadog connection with API and User keys.

Workflows should provide the following parameters in the spec:

* `incident_id`: (string) the unique internal identifier of the Incident to update. This is identified by `data.id` in responses from the Datadog `/v2/incidents` endpoint.
* `timeline_cell_content`: (string) Markdown-formatted text that represents the content of the timeline cell

Example usage:

```yaml
parameters:
  incident_id:
    description: unique ID of the incident to update
  timeline_cell_content:
    description: Content to include in the update

steps:
  - name: timeline-update
    image: relaysh/datadog-step-incident-timeline-update
    spec:
      connection:  !Connection {type: "datadog", name: "my-datadog-keys"}
      timeline_cell_content: !Parameter timeline_cell_content
      incident_id:  !Parameter incident_id
```
