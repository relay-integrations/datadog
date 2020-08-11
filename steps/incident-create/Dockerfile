FROM relaysh/core:latest-python
RUN pip install datadog
COPY "./datadog-incident-create.py" "/entrypoint.py"
ENTRYPOINT []
CMD ["python3", "/entrypoint.py"]

LABEL "org.opencontainers.image.title"="Datadog Incident Creation"
LABEL "org.opencontainers.image.description"="This step creates a new Incident on the linked Datadog account"
LABEL "com.puppet.nebula.sdk.version"="v1"
