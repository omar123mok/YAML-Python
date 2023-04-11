locals {

  landing-zone-private-cidr = "100.64.0.0/12"

  common-tags = {
    app   = "landing-zone"
    owner = "arch.platform-architecture"
  }
}

