FROM relaysh/core:latest-python
RUN pip install datadog
COPY "./datadog-incident-timeline-update.py" "/entrypoint.py"
ENTRYPOINT []
CMD ["python3", "/entrypoint.py"]

LABEL "org.opencontainers.image.title"="Datadog Incident Timeline Update"
LABEL "org.opencontainers.image.description"="This step updates an incident timeline with a new cell"
LABEL "com.puppet.nebula.sdk.version"="v1"
