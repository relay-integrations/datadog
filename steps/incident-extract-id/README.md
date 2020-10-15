# incident-extract-id

This step extracts an internal ID for a Datadog Incident, given a friendly name.

This requires a Datadog connection with API and User keys.

It's useful because the API requires IDs for operations on existing incidents, but these IDs are not exposed to users, only the "public name".

* `public_id`: (string) the numeric part of incident's identifier, for example to look up "IR-2", supply "2"

It sets an output variable `incident_id` with the internal identifier of the ID.
