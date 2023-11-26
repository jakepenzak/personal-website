# Welcome to the code base for my [Personal Website](http://jacob-pieniazek.com)!

This website was created via [reflex](https://reflex.dev/), a python framework for web apps and websites, and hosted on a personal cloud-based linux server via [Digital Ocean](https://www.digitalocean.com/). 

## Technology Stack Utilized
* [**Reflex**](https://reflex.dev/)
* [**Python**](https://www.python.org/)
* [**Docker**](https://www.docker.com/)
* [**Ubuntu Server**](https://ubuntu.com/)
* [**Digital Ocean**](https://www.digitalocean.com/)
* [**Caddy**](https://caddyserver.com/)
* [**Conda**](https://docs.conda.io/en/latest/)
* HTML/CSS

## Development Instructions
1. Clone the repository using `git clone`
2. Create environment via `conda env create -f env/environment.yml`
3. Initialize Reflex with `reflex init`
4. Run the development server using `reflex run`

## Deployment Instructions
*Note: This website was self-deployed and executed in a cloud-based linux VM. Proper caution and consideration should always be utilized when opening yourself up to the web.*
1. Build production service `DOMAIN={domain} docker compose build`
2. Run production service `DOMAIN={domain} docker compose up`
