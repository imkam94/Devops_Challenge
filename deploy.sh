#!/bin/bash
# Authenticate with AWS
aws configure

# Deploy infrastructure
cd infra
cdk deploy

# Build and push Docker image
aws ecr get-login-password | docker login --username AWS --password-stdin your-account-id.dkr.ecr.us-west-2.amazonaws.com
docker build -t your-account-id.dkr.ecr.us-west-2.amazonaws.com/python-app:latest ./app
docker push your-account-id.dkr.ecr.us-west-2.amazonaws.com/python-app:latest

# Deploy to EKS
aws eks update-kubeconfig --name EksCluster --region us-west-2
helm upgrade --install python-app ./app/helm