# datadog-step-incident-create

This step creates a new Datadog Incident.

This requires a Datadog connection with API and User keys.

Workflows should provide the following parameters in the spec:


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
