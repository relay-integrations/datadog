FROM relaysh/core:latest-python
RUN pip install datadog
COPY "./datadog-incident-extract-id.py" "/entrypoint.py"
ENTRYPOINT []
CMD ["python3", "/entrypoint.py"]

LABEL "org.opencontainers.image.title"="Datadog Incident ID Extraction"
LABEL "org.opencontainers.image.description"="This step extracts an incident ID from the friendly name"
LABEL "com.puppet.nebula.sdk.version"="v1"
