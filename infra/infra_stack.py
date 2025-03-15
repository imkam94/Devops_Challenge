from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_eks as eks,
    aws_ecr as ecr,
    aws_iam as iam,
    CfnOutput
)

from constructs import Construct
from aws_cdk import App
from aws_cdk.aws_eks import KubectlV26Layer

class InfraStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create ECR repository
        ecr_repo = ecr.Repository(
            self, "DevOpsRepo",
            repository_name="devops-repo"
        )

        # Create VPC
        vpc = ec2.Vpc(
            self, "EksVpc",
            max_azs=2
        )

        # Add IAM role for GitHub Actions (if needed)
        github_role = iam.Role(
            self, "GitHubActionsRole",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
            managed_policies=[iam.ManagedPolicy.from_aws_managed_policy_name("AdministratorAccess")]
        )


        # Create EKS cluster
        cluster = eks.Cluster(
            self, "EksCluster",
            cluster_name="DevOpsCluster",
            vpc=vpc,
            default_capacity=2,
            default_capacity_instance=ec2.InstanceType("t3.micro"),
            version=eks.KubernetesVersion.V1_30
        )

        # Outputs for GitHub Actions
        CfnOutput(self, "EcrRepoUri", value=ecr_repo.repository_uri)
        CfnOutput(self, "ClusterName", value=cluster.cluster_name)
