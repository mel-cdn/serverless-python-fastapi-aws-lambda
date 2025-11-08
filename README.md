# Serverless Python FastAPI on AWS Lambda

## 📖 Overview

This repository demonstrates deploying a **[FastAPI](https://fastapi.tiangolo.com/)** application to **AWS Lambda** using serverless architecture.

## ✨ Highlights

- ![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white) Python FastAPI application
- ![AWS](https://img.shields.io/badge/AWS-FF9900?logo=amazon-aws&logoColor=white) Amazon Web Services (AWS)

---

## 🚀 Getting Started

### Prerequisites

Ensure the following tools are installed:

- **Python**
    - Install [Python 3.12+](https://www.python.org/)
- **Amazon Web Services (AWS)**
    - Create a Free Tier [AWS Account](https://aws.amazon.com/)
    - Install [AWS CLI](https://aws.amazon.com/cli/)
    - Configure AWS CLI with
      your [AWS Access Key ID and Secret Access Key](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)
    - Install [AWS Serverless Application Model (AWS SAM)](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

---

### Installation

On your terminal, run the following commands:

```bash
# Clone repository
git clone git@github.com:mel-cdn/serverless-python-fastapi-aws-lambda.git
cd serverless-python-fastapi-aws-lambda

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r src/requirements.txt

# Run locally
./run-local-service.sh

# Access on your browser
http://localhost:8000/
```

## 🌍 Deployment

Using AWS SAM

```bash
# Verify SAM installation
sam --version

# Export your AWS profile
export AWS_PROFILE="your-aws-profile-name"

# Build
sam build

# Deploy
sam deploy --guided

# Check the deployed API
aws apigatewayv2 get-apis
{
  ...,
  "ApiEndpoint": "https://<your-api-id>.execute-api.ap-southeast-1.amazonaws.com",
  ...,
}
```