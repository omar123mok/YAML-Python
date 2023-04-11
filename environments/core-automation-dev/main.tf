locals {
  environment = "core-automation-dev"
  workload    = "dev"
  alias       = "31312323"
  tags        = merge(local.common-tags, { env = "core-automation-dev" })
}

module "iam" {
  source                  = "../../modules/iam"
  alias                   = local.alias
  tags                    = local.tags
  allow-manual-parameters = true
  ec2-ssm-role            = true
  cloudability-eid        = "31312323"
}

module "config" {
  source = "../../modules/config"
  tags   = local.tags
}

module "s3" {
  source = "../../modules/s3"
}
