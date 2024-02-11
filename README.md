# CatBot

Welcome to the CatBot repository! CatBot is an engaging Telegram bot designed to share random cat images. This project is particularly focused on demonstrating Kubernetes deployment and is an excellent resource for those learning about bot development, Docker, and Kubernetes.

## Project Structure

- `main.py`: The core Python script powering the CatBot.
- `requirements.txt`: Contains all necessary Python dependencies.a
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

# Automated Kubernetes Deployment with Jenkins and GitHub Webhooks

This repository includes a Jenkins pipeline script for the automated deployment of CatBot. The pipeline handles fetching the repository, building the Docker image, pushing it to DockerHub, and deploying to Kubernetes. Additionally, the setup integrates GitHub webhooks for a complete CI/CD experience.

## Jenkins Pipeline Setup

### Jenkins Agent Configuration

- Ensure your Jenkins environment is set up with an agent labeled 'eks-cluster' that has access to your Kubernetes cluster.
- Alternatively, you can use `agent any` in the pipeline script if your Jenkins master or other agents are configured to interact with Kubernetes.

### DockerHub Credentials

- Add your DockerHub credentials in Jenkins with the ID `dockerhub` ('Manage Jenkins' > 'Manage Credentials').

### Pipeline Execution

- Add the pipeline script to your Jenkins setup and run the pipeline through your Jenkins dashboard.

## GitHub Webhooks for CI/CD Automation

### Configuring GitHub Webhooks

- In your GitHub repository, navigate to 'Settings' > 'Webhooks' > 'Add webhook'.
- Enter your Jenkins URL with `/github-webhook/` appended (e.g., `http://your-jenkins-url/github-webhook/`).
- Select 'Just the push event' for the trigger.

### Configuring Jenkins

- In Jenkins, under your project's configuration, select 'Git' under 'Source Code Management'.
- Enter your repository URL and credentials if required.
- Check 'GitHub hook trigger for GITScm polling' under 'Build Triggers'.

## End-to-End CI/CD Flow

- Pushes to the repository trigger the GitHub webhook.
- Jenkins automatically triggers the pipeline, performing the tasks of fetching the repo, building the Docker image, pushing it to DockerHub, and deploying to Kubernetes.

## Final Steps

- Ensure Jenkins has proper network access to GitHub and your Kubernetes cluster.
- Verify Jenkins server reachability from GitHub via the webhook URL.
- Test the setup by pushing changes to your repository.

## Kubernetes Deployment

### Kubernetes Secret Configuration

1. Encode your Telegram bot token and TheCatApi key in base64:
    ```bash
    echo -n 'your-bot-token' | base64
    echo -n 'your-cat-api-key' | base64
    ```

2. Fill in the `BOT_TOKEN` and `CAT_API_KEY` in the `k8s/secret.yaml` file with the generated base64 values.
3. Apply the Kubernetes manifests:
    ```bash
    kubectl apply -f k8s/
    ```

#### Usage
Interact with your deployed Telegram bot using /start and /cat commands.

#### Contributing
This is an open-source project and we welcome contributions. Feel free to fork, improve, and submit pull requests. 
Contributions can range from new features and bug fixes to documentation enhancements.


### Notes:

- Replace placeholders like `your-image-name`, `your-bot-token`, and `your-cat-api-key` with the actual values relevant to your setup.
- The instructions assume basic familiarity with command-line operations and Kubernetes. You might want to add more detailed instructions if your target audience includes beginners.

