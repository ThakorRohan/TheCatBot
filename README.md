# CatBot

Welcome to the CatBot repository! CatBot is an engaging Telegram bot designed to share random cat images. This project is particularly focused on demonstrating Kubernetes deployment and is an excellent resource for those learning about bot development, Docker, and Kubernetes.

## Project Structure

- `main.py`: The core Python script powering the CatBot.
- `requirements.txt`: Contains all necessary Python dependencies.
- `Dockerfile`: Docker instructions to build the bot's image.
- `k8s/`: Kubernetes deployment manifests for orchestrating the bot on a cluster.

## Features

- **Interactive Commands**: Users can interact with CatBot through `/start` and `/cat` commands.
- **Docker Deployment**: Easily deployable in Docker environments.
- **Kubernetes Integration**: Ready for deployment on Kubernetes with provided manifest files.

## Getting Started

### Prerequisites

- Docker (for Docker deployment)
- Access to a Kubernetes cluster (for Kubernetes deployment)
- A Telegram bot token and TheCatApi key

### Deployment

#### Docker

1. Build and run the Docker image:
   ```bash
   docker build -t cat .
   docker run -d -e BOT_TOKEN=your-bot-token -e CAT_API_KEY=your-cat-api-key cat

#### Kubernetes

1. Encode your Telegram bot token and TheCatApi key in base64:
     ```bash
    echo -n 'your-bot-token' | base64
    echo -n 'your-cat-api-key' | base64

2. Fill in the BOT_TOKEN and CAT_API_KEY in the k8s/secret.yaml file with the generated base64 values.
   Apply the Kubernetes manifests:
    ```bash
    kubectl apply -f k8s/

#### Usage
Interact with your deployed Telegram bot using /start and /cat commands.

#### Contributing
This is an open-source project and we welcome contributions. Feel free to fork, improve, and submit pull requests. 
Contributions can range from new features and bug fixes to documentation enhancements.


### Notes:

- Replace placeholders like `your-image-name`, `your-bot-token`, and `your-cat-api-key` with the actual values relevant to your setup.
- The instructions assume basic familiarity with command-line operations and Kubernetes. You might want to add more detailed instructions if your target audience includes beginners.

