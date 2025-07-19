# Kubeshot Image Resizer

A lightweight Flask-based microservice to resize uploaded images to 200x200 pixels.
Built with Python Slim, Dockerized, and ready for Kubernetes deployment.

## API

- `POST /resize` — Upload an image as `multipart/form-data` under the key `image`.

## Technologies

- Python 3.12
- Flask & Pillow
- Docker
- Kubernetes

## Usage

Build and run locally:
```bash
docker build -t kubeshot .
docker run -p 5000:5000 kubeshot
