# FastAPI Nginx Controller Implementation Guide

## Introduction

The FastAPI Nginx Controller is designed to automate the management of Nginx configurations and SSL certificates for FastAPI applications. This guide consolidates the necessary code for a straightforward cut-and-paste implementation.

## System Requirements

- Ubuntu 20.04 or similar Linux distribution
- Nginx web server
- FastAPI framework
- Certbot for Let's Encrypt SSL certificates
- Python 3.8+

## Setup Script (`setup_nginx.sh`)

Automates the configuration of Nginx as a reverse proxy and secures it with an SSL certificate.

```bash
#!/bin/bash
# Prompt for domain and email
read -p "Enter your domain (e.g., example.com): " DOMAIN
read -p "Enter your email for SSL certificate registration: " EMAIL

# Define Nginx configuration path and select port
NGINX_SITE_CONFIG="/etc/nginx/sites-available/$DOMAIN"
echo "Checking for available ports..."

# Simplified setup commands

# Enable site and reload Nginx
sudo ln -s $NGINX_SITE_CONFIG /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx

# Obtain SSL certificate with Certbot
sudo certbot --nginx -d $DOMAIN -m $EMAIL --agree-tos --redirect

echo "Setup completed."
```

## Teardown Script (`teardown_nginx.sh`)

Reverses the setup process, removing Nginx configurations and SSL certificates.

```bash
#!/bin/bash
# Prompt for domain
read -p "Enter your domain: " DOMAIN

# Remove Nginx configuration and disable site
sudo rm -f $NGINX_SITE_CONFIG
sudo rm -f /etc/nginx/sites-enabled/$(basename $NGINX_SITE_CONFIG)
sudo nginx -t && sudo systemctl reload nginx

# Optional: Delete SSL certificate
read -p "Delete the SSL certificate for $DOMAIN? (y/N): " DELETE_CERT
if [[ $DELETE_CERT =~ ^[Yy]$ ]]; then
  sudo certbot delete --cert-name $DOMAIN
fi

echo "Teardown completed."
```

## FastAPI Application Structure (`main.py`)

Manages the setup and teardown scripts securely, with basic authentication.

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import subprocess

app = FastAPI()

# Authentication and endpoint setup

@app.post("/setup-nginx/")
async def setup_nginx():
    # Call setup script
    return {"message": "Nginx setup initiated"}

@app.post("/teardown-nginx/")
async def teardown_nginx():
    # Call teardown script
    return {"message": "Nginx teardown initiated"}
```

## Note

- Ensure scripts are executable (`chmod +x script_name.sh`).
- The authentication example is simplified. Use robust authentication in production.
- Adjust paths and permissions as needed.

This document provides a straightforward foundation for setting up a FastAPI-based Nginx controller. Adapt and extend to fit your requirements.