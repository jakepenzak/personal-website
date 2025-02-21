# Code base for my [Personal Website](http://jacob-pieniazek.com)

This website was created via [reflex](https://reflex.dev/), a python framework for web apps and websites, and is self-hosted.

## Tech Stack

- [**Reflex**](https://reflex.dev/) - Python web framework
- [**Docker**](https://www.docker.com/) - Containerization framework
- [**Ubuntu Server**](https://ubuntu.com/) - Server for hosting
- [**Cloudflare**](https://www.cloudflare.com/) - Reverse proxy & protection
- [**Nginx Proxy Manager**](https://nginxproxymanager.com/) - Internal reverse proxy
- [**Astral UV**](https://docs.astral.sh/uv/) - Project dependency management

## Dev

1. Create environment via `uv sync --all-extras --all-groups`
2. Initialize Reflex with `reflex init`
3. Run the development server using `reflex run`

## Deployment

1. Build docker container w/ `main.Dockerfile`
2. Leverage in Docker compose stack per needs

## Deployment (in deployment_backup)

Previously utilized when hosting w/ Digital Ocean Droplet.

Used Caddy for webserver and docker compose for frontend and backend.

1. Build production service `DOMAIN={domain} docker compose build`
2. Run production service `DOMAIN={domain} docker compose up`
