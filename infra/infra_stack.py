from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_eks as eks,
    aws_ecr as ecr,
    CfnOutput
)
from constructs import Construct

class InfraStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # ECR Repository
        ecr_repo = ecr.Repository(self, "DevOpsRepo", repository_name="devops-repo")

        # VPC with NAT Gateway
        vpc = ec2.Vpc(self, "EksVpc", max_azs=2)

        # EKS Cluster (version compatible with CDK 2.140.0)
        cluster = eks.Cluster(
            self, "EksCluster",
            cluster_name="DevOpsCluster",
            vpc=vpc,
            version=eks.KubernetesVersion.V1_29,
            default_capacity=2,
            default_capacity_instance=ec2.InstanceType("t3.micro")
        )

        # Outputs
        CfnOutput(self, "EcrRepoUri", value=ecr_repo.repository_uri)
        CfnOutput(self, "ClusterName", value=cluster.cluster_name)