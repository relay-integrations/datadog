FROM relaysh/core:latest-python

COPY "./server.py" "/relay/datadog-event-fired.py"
ENTRYPOINT []
CMD ["python3", "/relay/datadog-event-fired.py"]

LABEL "org.opencontainers.image.title"="Datadog Event Trigger"
LABEL "org.opencontainers.image.description"="This trigger handles Datadog events and notifications"
LABEL "com.puppet.nebula.sdk.version"="v1"
