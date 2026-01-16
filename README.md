# Personal Website

Live site: http://jacob-pieniazek.com

A self-hosted personal website built with [Reflex](https://reflex.dev/) (Python).

---

## Tech Stack

- **App:** [Reflex](https://reflex.dev/) (Python 3.11)
- **Dependencies:** [uv](https://docs.astral.sh/uv/)
- **Containerization:** [Docker](https://www.docker.com/)
- **Hosting:** Ubuntu Server
- **Edge / Security:** Cloudflare
- **Reverse proxy:** Nginx Proxy Manager

---

## Local Development

### Prerequisites

- Python `>=3.11`
- [`uv`](https://docs.astral.sh/uv/)
- (Optional) Docker

### Setup

```bash
uv sync --all-extras --all-groups
reflex init
```

### Run

```bash
reflex run
```

---

## Docker Deployment

This repo includes a production Dockerfile: `main.Dockerfile`.

```bash
docker build -f main.Dockerfile -t personal-website .
```

The container starts the app with:

```bash
reflex db migrate && reflex run --env prod
```

---

## CI

GitHub Actions runs Reflex export and a Docker build on PRs:

- `/.github/workflows/integration-tests.yml`
- `/.github/workflows/end-to-end-tests.yml`
