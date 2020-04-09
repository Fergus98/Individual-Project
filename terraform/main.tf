provider "azurerm" {

  version = "=1.30.1"

}



module "master" {

  source = "./modules/master"

  admin_user = "jenkins"

  resource_group = azurerm_resource_group.default

  virtual_network = azurerm_virtual_network.default

}



module "worker" {

  source = "./modules/worker"

  admin_user = "jenkins"

  resource_group = azurerm_resource_group.default

  virtual_network = azurerm_virtual_network.default

}



resource "azurerm_resource_group" "default" {

  name = terraform.workspace

  location = "uksouth"

}



resource "azurerm_virtual_network" "default" {

  name = "${terraform.workspace}-vnet"

  address_space = ["10.0.0.0/16"]

  location = azurerm_resource_group.default.location

  resource_group_name = azurerm_resource_group.default.name

}
