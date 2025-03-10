from aws_cdk import (
    aws_eks as eks,
    aws_ec2 as ec2,
    aws_iam as iam,
    core,
)

class InfraStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Create VPC
        vpc = ec2.Vpc(self, "Vpc")

        # Create EKS Cluster
        cluster = eks.Cluster(
            self, "EksCluster",
            version=eks.KubernetesVersion.V1_21,
            vpc=vpc,
            default_capacity=2,
            default_capacity_instance=ec2.InstanceType("t3.small"),
        )

        # Grant Azure DevOps IAM role permissions to interact with EKS
        azure_devops_role = iam.Role(
            self, "AzureDevOpsRole",
            assumed_by=iam.AccountPrincipal("YOUR_AWS_ACCOUNT_ID"),
        )
        cluster.aws_auth.add_masters_role(azure_devops_role)
