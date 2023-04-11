terraform {
  backend "s3" {
    bucket               = "eis-shared-services-terraform-state"
    key                  = "infrastructure/core-automation-dev.tfstate"
    region               = "us-east-1"
    encrypt              = true
    dynamodb_table       = "eis-shared-services-terraform-state"
    workspace_key_prefix = "workspaces"
  }
}
