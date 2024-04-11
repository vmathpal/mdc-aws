terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 3.0.0"
    }
  }
}

provider "aws" {
  region = "eu-central-1"  # Specify your desired region
}

data "aws_iam_policy_document" "AWSCloudFormationStackSetAdministrationRole_assume_role_policy" {
  statement {
    actions = ["sts:AssumeRole"]
    effect  = "Allow"

    principals {
      identifiers = ["cloudformation.amazonaws.com"]
      type        = "Service"
    }
  }
}

resource "aws_iam_role" "AWSCloudFormationStackSetAdministrationRole" {
  assume_role_policy = data.aws_iam_policy_document.AWSCloudFormationStackSetAdministrationRole_assume_role_policy.json
  name               = "AWSCloudFormationStackSetAdministrationRole"
}



resource "aws_cloudformation_stack_set" "my_stackset" {
  name                 = "my-cft-stackset"
  #administration_role_arn = aws_iam_role.AWSCloudFormationStackSetAdministrationRole.arn
  permission_model = "SERVICE_MANAGED"
  call_as = "SELF"
  template_url         = "https://awscftmdcs3bkt.s3.eu-central-1.amazonaws.com/mdc3-init.json"
#   parameters = {
#     VPCCidr = "10.0.0.0/16"
#     # Add other parameters as needed
#   }
  auto_deployment {
    enabled = true
    retain_stacks_on_account_removal = false
  }
  capabilities  = ["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM","CAPABILITY_AUTO_EXPAND"] #["CAPABILITY_NAMED_IAM"]
}

resource "aws_cloudformation_stack_set_instance" "example" {
  deployment_targets {
    organizational_unit_ids = ["r-af91"]
  }

  region         = "eu-central-1"
  stack_set_name = aws_cloudformation_stack_set.my_stackset.name
  
}



data "aws_iam_policy_document" "AWSCloudFormationStackSetAdministrationRole_ExecutionPolicy" {
  statement {
    actions   = ["sts:AssumeRole"]
    effect    = "Allow"
    resources = ["arn:aws:iam::*:role/${aws_cloudformation_stack_set.my_stackset.execution_role_name}"]
  }
}

resource "aws_iam_role_policy" "AWSCloudFormationStackSetAdministrationRole_ExecutionPolicy" {
  name   = "ExecutionPolicy"
  policy = data.aws_iam_policy_document.AWSCloudFormationStackSetAdministrationRole_ExecutionPolicy.json
  role   = aws_iam_role.AWSCloudFormationStackSetAdministrationRole.name
}

resource "aws_cloudformation_stack" "my_stack" {
  name         = "my-cloudformation-stack"
  template_url = "https://awscftmdcs3bkt.s3.eu-central-1.amazonaws.com/mdc3-init.json"
  # Other optional parameters can be added here
  capabilities  = ["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM","CAPABILITY_AUTO_EXPAND"]
}

# resource "aws_cloudformation_change_set" "my_change_set" {
#   stack_name = "my-cloudformation-stack"
#   template_body = file("/Users/apple/Downloads/stackmdc01.json")
#   # Other parameters like parameters, tags, etc.
# }


# resource "aws_organizations_delegated_administrator" "example" {
#   account_id        = "934612421956"
#   service_principal = "account.amazonaws.com"
#MDCContainersK8sRole
# }