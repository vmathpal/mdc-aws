import boto3
from botocore.exceptions import ClientError

# Create a CloudFormation client
cfn = boto3.client('cloudformation',region_name='eu-central-1')

# Create a change set for the stack
#change_set_name = 'my-change-set'
stack_name = "my-cloudformation-stack"
StackSetName='my-cft-stackset'

stackupdate = cfn.update_stack(
    StackName=stack_name,
    TemplateURL='https://awscftmdcs3bkt.s3.eu-central-1.amazonaws.com/mdc3.template',
    Capabilities=[
        'CAPABILITY_IAM','CAPABILITY_NAMED_IAM','CAPABILITY_AUTO_EXPAND'
     ]
)

stacksetupdate = cfn.update_stack_set(
    
    #Description='string',
    TemplateBody='string',
    TemplateURL='https://awscftmdcs3bkt.s3.eu-central-1.amazonaws.com/mdc3.template',
    # UsePreviousTemplate=True|False,
    # Parameters=[
    #     {
    #         'ParameterKey': 'string',
    #         'ParameterValue': 'string',
    #         'UsePreviousValue': True|False,
    #         'ResolvedValue': 'string'
    #     },
    # ],
    Capabilities=[
        'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND',
    ],
    # Tags=[
    #     {
    #         'Key': 'string',
    #         'Value': 'string'
    #     },
    # ],
    # OperationPreferences={
    #     'RegionConcurrencyType': 'SEQUENTIAL'|'PARALLEL',
    #     'RegionOrder': [
    #         'string',
    #     ],
    #     'FailureToleranceCount': 123,
    #     'FailureTolerancePercentage': 123,
    #     'MaxConcurrentCount': 123,
    #     'MaxConcurrentPercentage': 123,
    #     'ConcurrencyMode': 'STRICT_FAILURE_TOLERANCE'|'SOFT_FAILURE_TOLERANCE'
    # },
    # AdministrationRoleARN='string',
    # ExecutionRoleName='string',
    # DeploymentTargets={
    #     'Accounts': [
    #         'string',
    #     ],
    #     'AccountsUrl': 'string',
    #     'OrganizationalUnitIds': [
    #         'string',
    #     ],
    #     'AccountFilterType': 'NONE'|'INTERSECTION'|'DIFFERENCE'|'UNION'
    # },
    PermissionModel='SERVICE_MANAGED', #|'SELF_MANAGED',
    AutoDeployment={
        'Enabled': True,
        'RetainStacksOnAccountRemoval': True
    },
    # OperationId='string',
    # Accounts=[
    #     'string',
    # ],
    # Regions=[
    #     'string',
    # ],
    # CallAs='SELF'|'DELEGATED_ADMIN',
    # ManagedExecution={
    #     'Active': True|False
    # }
)
