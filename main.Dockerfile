# This docker file is intended to be used with docker compose to deploy a production
# instance of a Reflex app.

# Stage 1: init
FROM python:3.11 as init

ARG uv=/root/.cargo/bin/uv

# Install `uv` for faster package boostrapping
ADD --chmod=755 https://astral.sh/uv/0.4.30/install.sh /install.sh
RUN /install.sh && rm /install.sh

# Copy local context to `/app` inside container (see .dockerignore)
WORKDIR /app
COPY . .
RUN mkdir -p /app/data /app/uploaded_files

# Create virtualenv which will be copied into final container
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN $uv venv

# Install app requirements and reflex inside virtualenv
RUN $uv pip install -r env/requirements.txt -r env/reflex_requirements.txt

# Deploy templates and prepare app
RUN reflex init

# Needed until Reflex properly passes SIGTERM on backend.
STOPSIGNAL SIGKILL

EXPOSE 3000
EXPOSE 8000

# Always apply migrations before starting the backend.
CMD reflex db migrate && reflex run --env prod
