from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_eks as eks,
    aws_ecr as ecr,
    aws_iam as iam,
    CfnOutput
)
from constructs import Construct

class InfraStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create ECR repository
        ecr_repo = ecr.Repository(self, "DevOps")

        # Create VPC
        vpc = ec2.Vpc(self, "eksVpc")

        # Create EKS cluster with IAM role for GitHub Actions
        cluster = eks.Cluster(
            self, "EksCluster",
            cluster_name="DevOps",
            vpc=vpc,
            default_capacity=1,
            default_capacity_instance=ec2.InstanceType("t3.micro"),
            version=eks.KubernetesVersion.V1_30,
            kubectl_layer=eks.KubectlLayer(self, "KubectlLayer")
        )

        # Outputs for GitHub Actions
        CfnOutput(self, "EcrRepoUri", value=ecr_repo.repository_uri)
        CfnOutput(self, "ClusterName", value=cluster.cluster_name)
        