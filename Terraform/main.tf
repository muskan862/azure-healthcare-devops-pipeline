# 1. Configure the Azure Provider
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

# 2. Create a Resource Group
resource "azurerm_resource_group" "devops_rg" {
  name     = "rg-devops-pipeline-prod"
  location = "East US"
}

# 3. Create a Virtual Network
resource "azurerm_virtual_network" "devops_vnet" {
  name                = "vnet-devops-core"
  location            = azurerm_resource_group.devops_rg.location
  resource_group_name = azurerm_resource_group.devops_rg.name
  address_space       = ["10.0.0.0/16"]
}

# 4. Create a Subnet for your AKS Cluster
resource "azurerm_subnet" "aks_subnet" {
  name                 = "sub-aks-nodes"
  resource_group_name  = azurerm_resource_group.devops_rg.name
  virtual_network_name = azurerm_virtual_network.devops_vnet.name
  address_prefixes     = ["10.0.1.0/24"]
}