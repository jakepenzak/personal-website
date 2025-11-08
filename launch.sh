#!/bin/bash

# Activate virtual environment
source .venv/bin/activate

# Pull latest changes
git pull

# Build and run docker stack
sudo docker compose -f ../external-docker-compose.yml -f ../internal-docker-compose.yml up -d --force-recreate --build personal-website
