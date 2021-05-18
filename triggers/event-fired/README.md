# event-fired

This [Datadog](https://www.datadoghq.com) trigger fires when an event is fired.

For more information about Datadog webhooks, check out the [documentation](https://docs.datadoghq.com/integrations/webhooks/).

## Setup Instructions

### Step 1: Create a new webhook in Datadog
- Go to your Datadog dashboard and install the webhooks integration (if not already installed)
- Create a "New" webhook and supply a name (e.g. "Relay")
- Copy the webhook URL from your Relay workflow and paste it into the "URL" field

### Step 2: Configure a monitor with your webhook
- Navigate to your chosen alert [monitor](https://docs.datadoghq.com/monitors/monitor_types/)
- Click Edit and scroll down to the "Say what's happening" section
- Configure your webhook (e.g. "@webhook-relay")
- Click "Save"
