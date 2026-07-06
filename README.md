# azure-healthcare-devops-pipeline
# Healthcare Dashboard CI/CD Pipeline

This repository contains the source code, infrastructure configurations, and automation workflows for the Healthcare Dashboard application.

## CI/CD Workflow Documentation

The Continuous Integration and Continuous Delivery (CI/CD) engine is fully automated using **GitHub Actions** via the configuration file located at `.github/workflows/ci.yml`.

### How the Automation Works:
1. **Trigger:** The pipeline automatically triggers every time a developer runs a `git push` command to the `main` branch.
2. **Environment Setup:** A virtual cloud runner (`ubuntu-latest`) spins up to isolate and execute the deployment phases safely.
3. **Repository Checkout:** The runner pulls down the latest application source code, infrastructure files, and configurations.
4. **Secure Registry Authentication:** The runner securely logs into Docker Hub using encrypted credentials configured inside **GitHub Secrets** (`DOCKER_USERNAME` and `DOCKER_PASSWORD`).
5. **Container Compilation:** The engine compiles a fresh, production-ready container image using the repository's root `Dockerfile`.
6. **Cloud Delivery:** The finalized image is automatically tagged and pushed to the public container registry (`muskan9208/healthcare-dashboard:latest`), ensuring the latest build is immediately ready for deployment.