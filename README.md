# Cloud App Deployment with ECS and Fargate

## Overview
This project deploys a Python REST API to AWS ECS with Fargate using a CI/CD pipeline. The API has two endpoints:
1. `/health` - Returns application health status.
2. `/data` - Returns dummy data (requires basic authentication: `admin:secret`).

## Prerequisites
- AWS Free Tier account
- Azure DevOps or GitHub account
- Docker installed locally (optional)

## Setup
1. Clone the repository.
2. Deploy the CloudFormation stack (`infra/cloudformation.yaml`) to create the ECS infrastructure.
3. Create an ECR repository named `cloud-app`.
4. For Azure DevOps:
   - Configure AWS and ECR service connections.
   - Push code to trigger `azure-pipelines.yml`.
5. For GitHub Actions:
   - Add `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` to GitHub Secrets.
   - Push code to trigger `.github/workflows/deploy.yml`.

## Testing
- Health: `curl http://<load-balancer-dns>/health`
- Data: `curl -u admin:secret http://<load-balancer-dns>/data`

## Infrastructure
- ECS Cluster: `CloudAppCluster`
- ECS Service: `CloudAppService`
- Load Balancer: ALB exposing port 80


## Testing the Application
1. Get the load balancer DNS:

2. Test the endpoints:
- Health: `curl http://<load-balancer-dns>/health`
  - Expected: `{"status": "healthy", "message": "Application is running"}`
- Data: `curl -u admin:secret http://<load-balancer-dns>/data`
  - Expected: `{"items": [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]}`