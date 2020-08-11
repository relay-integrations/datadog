# datadog-step-incident-extract-id

This step extracts an internal ID for a Datadog Incident, given a friendly name.

This requires a Datadog connection with API and User keys.

It's useful because the API requires IDs for operations on existing incidents, but these IDs are not exposed to users, only the "public name".

* `public_id`: (string) the numeric part of incident's identifier, for example to look up "IR-2", supply "2"

It sets an output variable `incident_id` with the internal identifier of the ID.

Example usage:

```yaml
parameters:
  public_id:
    description: friendly ID of the incident to extract

steps:
  - name: extract-id
    image: relaysh/datadog-step-incident-extract-id
    spec:
      connection:  !Connection {type: "datadog", name: "my-datadog-keys"}
      public_id:  !Parameter public_id
```
