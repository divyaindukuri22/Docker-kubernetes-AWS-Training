# Docker-kubernetes-AWS-Training

## Key Concepts & Tasks

### 1. **Docker and Kubernetes on AWS EKS**
   - **Objective**: Deploy a simple Flask application ("Hello, Divya!") using Docker and Kubernetes on AWS EKS.
   - **Key Services**: AWS EKS, ECR, Docker, Kubernetes
   - **Steps Taken**:
     - Built a Docker container for a Flask app.
     - Pushed the image to AWS ECR (Elastic Container Registry).
     - Created an EKS cluster and deployed the Flask app on it using Kubernetes.

### 2. **Deploying a Python Application to AWS Lambda**
   - **Objective**: Deploy a Python (.py) application to AWS Lambda.
   - **Key Services**: AWS Lambda
   - **Steps Taken**:
     - Created a Python application.
     - Packaged it for Lambda deployment.
     - Deployed the function to AWS Lambda, testing it with sample events.

### 3. **Provisioning an AWS EC2 Instance with Terraform**
   - **Objective**: Automate the creation of an AWS EC2 instance using Terraform.
   - **Key Services**: AWS EC2, Terraform
   - **Steps Taken**:
     - Wrote Terraform scripts to provision an EC2 instance.
     - Initialized Terraform and applied the configuration to create the instance on AWS.

### 4. **Learning the AWS SDK for Java**
   - **Objective**: Get hands-on experience with the AWS SDK for Java.
   - **Key Services**: AWS SDK for Java
   - **Steps Taken**:
     - Started learning how to interact with AWS services using Java.
     - Explored SDK features like interacting with S3, EC2, and other AWS services.

### 5. **Terraform Basics**
   - **Objective**: Start learning Terraform for Infrastructure as Code (IaC).
   - **Key Services**: Terraform
   - **Steps Taken**:
     - Wrote Terraform scripts to provision AWS EC2 instances and resources.
     - Used `terraform init`, `terraform plan`, and `terraform apply` commands to manage resources.


## Prerequisites

- **AWS Account**: You need an AWS account to use AWS services like EKS, Lambda, EC2, etc.
- **Terraform**: Make sure Terraform is installed on your machine.
- **Docker**: Docker should be installed for containerization.
- **kubectl**: You need `kubectl` to interact with Kubernetes.
- **AWS CLI**: AWS CLI for managing AWS services locally.

## Instructions

1. **Deploy Flask App to EKS**:
   - Build the Docker image: `docker build -t flask-app .`
   - Push to AWS ECR: `aws ecr create-repository --repository-name flask-app`
   - Deploy on EKS using Kubernetes.

2. **Deploy Python Application to Lambda**:
   - Package the Python function for Lambda.
   - Deploy using the AWS Management Console or AWS CLI.

3. **Provision EC2 with Terraform**:
   - Initialize Terraform: `terraform init`
   - Plan and Apply: `terraform plan` and `terraform apply`

4. **Set Up AWS SDK for Java**:
   - Use Maven or Gradle to set up dependencies.
   - Write code to interact with AWS services.
