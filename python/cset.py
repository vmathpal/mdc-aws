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
    StackSetName='my-cft-stackset',
    #Description='string',
    #TemplateBody='string',
    TemplateURL='https://awscftmdcs3bkt.s3.eu-central-1.amazonaws.com/mdc3.template',
    PermissionModel='SERVICE_MANAGED',
    Capabilities=[
        'CAPABILITY_IAM','CAPABILITY_NAMED_IAM','CAPABILITY_AUTO_EXPAND',
    ],
    #UsePreviousTemplate=False,
    AutoDeployment={
        'Enabled': True,
        'RetainStacksOnAccountRemoval': True
    },
)



response = cfn.update_stack_instances(
    StackSetName='my-cft-stackset',
    DeploymentTargets={
        'Accounts': [
            '851725621123',
        ],
 
        'OrganizationalUnitIds': [
            'r-af91',
        ],
        #'AccountFilterType': 'NONE'|'INTERSECTION'|'DIFFERENCE'|'UNION'
    },
    Regions=[
        'eu-central-1',
    ],
    # ParameterOverrides=[
    #     {
    #         'ParameterKey': 'string',
    #         'ParameterValue': 'string',
    #         'UsePreviousValue': True|False,
    #         'ResolvedValue': 'string'
    #     },
    # ],
    OperationPreferences={
        'RegionConcurrencyType': 'SEQUENTIAL',
        # 'FailureToleranceCount': 123,
        # 'FailureTolerancePercentage': 123,
        # 'MaxConcurrentCount': 123,
        # 'MaxConcurrentPercentage': 123,
        #'ConcurrencyMode': 'STRICT_FAILURE_TOLERANCE'|'SOFT_FAILURE_TOLERANCE'
    },
    #OperationId='string',
    CallAs='SELF'
)



# stacksetupdate = cfn.update_stack_set(
#     StackSetName='my-cft-stackset',
#     #Description='string',
#     #TemplateBody='string',
#     TemplateURL='https://awscftmdcs3bkt.s3.eu-central-1.amazonaws.com/mdc3.template',
#     PermissionModel='SERVICE_MANAGED',
#     Capabilities=[
#         'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND',
#     ],
#     #UsePreviousTemplate=False,
#     AutoDeployment={
#         'Enabled': True,
#         'RetainStacksOnAccountRemoval': True
#     },
# )

