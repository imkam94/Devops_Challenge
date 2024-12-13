# Devops_Challenge
This repository for Merk group Devops Challenge

# EKS Deployment with CI/CD

## Overview
This demonstrates deploying a Python REST API to an EKS cluster using a CI/CD pipeline. The project includes CloudFormation templates for infrastructure setup, Dockerized application deployment, Helm charts for Kubernetes, and CI/CD configurations for Azure DevOps and AWS CodePipeline.

## Prerequisites
- AWS CLI and AWS account
- kubectl
- Helm CLI
- Docker
- Azure DevOps account
- GitHub repository
- AWS Free Tier for EKS setup

## Steps
1. Deploy infrastructure using CloudFormation templates.
2. Build and push the Docker image to ECR.
3. Deploy the application using Helm charts.
4. Configure CI/CD pipelines for automated deployments.

## Infrastructure Setup
1. Deploy VPC: `infrastructure/vpc-stack.yaml`
2. Deploy EKS: `infrastructure/eks-cluster.yaml`

## Application
The Python REST API provides:
- Health-check endpoint: `/health`
- Dummy data endpoint: `/data` (requires authentication).
- 
## Authentication
- The `/data` endpoint requires JWT authentication. 

## CI/CD Pipelines
1. Azure DevOps pipeline: `pipeline/azure-pipeline.yml`
2. AWS CodePipeline: `pipeline/aws-pipeline.yml`

