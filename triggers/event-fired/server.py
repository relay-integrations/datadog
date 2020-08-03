from relay_sdk import Interface, WebhookServer
from quart import Quart, request

relay = Interface()
app = Quart('event-fired')

@app.route('/', methods=['POST'])
async def webhook():
    data = await request.get_json()

    for key, value in request.headers.items():
        if key.startswith("X-Datadog-"):
            relay.events.emit(data)
            return {'success': True}

    return {'message': 'not a valid Datadog event'}, 400, {}

if __name__ == '__main__':
    WebhookServer(app).serve_forever()

