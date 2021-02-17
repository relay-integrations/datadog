from relay_sdk import Interface, WebhookServer
from quart import Quart, request
import logging
import json

relay = Interface()
app = Quart('event-fired')

logging.getLogger().setLevel(logging.INFO)

@app.route('/', methods=['POST'])
async def webhook():
    data = await request.get_json()

    logging.info("Received the following webhook payload: \n%s", json.dumps(data, indent=4))

    for key, value in request.headers.items():
        if key.startswith("X-Datadog-"):
            relay.events.emit(data, key=data['id'])
            return {'success': True}

    return {'message': 'not a valid Datadog event'}, 400, {}

if __name__ == '__main__':
    WebhookServer(app).serve_forever()

