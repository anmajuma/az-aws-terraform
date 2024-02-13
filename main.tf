
terraform {
  #backend "azurerm" {}
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "3.53.0"
    }
    # databricks = {
    #   source  = "databricks/databricks"
    #   version = "1.15.0"
    # }
  }
}

provider "azurerm" {
  features {}
}
module "resource_group_network" {
  source = "git::https://github.com/Azure/azure-data-labs-modules.git//terraform/resource-group?ref=v1.5.0&depth=1"

  basename = "lexcorprg-dev"
  location = "North Europe"
}
module "virtual_network" {
  source              = "git::https://github.com/Azure/azure-data-labs-modules.git//terraform/virtual-network?ref=v1.5.0&depth=1"
  basename            = "lexcorp-dev"
  address_space       = ["10.0.0.0/16"]
  location            = "North Europe"
  resource_group_name = module.resource_group_network.name
}

module "subnet_default"  {
  source = "git::https://github.com/Azure/azure-data-labs-modules.git//terraform/subnet?ref=v1.5.0&depth=1"

  name                                      = "lexcorp-dev"
  resource_group_name                       = module.resource_group_network.name
  vnet_name                                 = module.virtual_network.name
  address_prefixes                          = ["10.0.1.0/24", "10.0.1.0/32"]
  private_endpoint_network_policies_enabled = true
}