#!/bin/bash
################################################################################
# Script for installing third-party modules in Odoo V8
# Author: Luigi Sison
#-------------------------------------------------------------------------------
# Go to Ubuntu directory where you want to install the software.
# cd /odoo/custom
# cd addons
################################################################################
sudo git clone --depth 1 --branch 8.0 https://github.com/OCA/department.git odoo/custom/addons
sudo git clone --depth 1 --branch 8.0 https://github.com/odoomrp/odoomrp-wip.git odoo/custom/addons
sudo git clone --depth 1 --branch 8.0 https://github.com/odoomrp/odoomrp-utils.git odoo/custom/addons/odoomrp-utils
sudo git clone --depth 1 --branch 8.0 https://github.com/OCA/sale-workflow.git odoo/custom/addons/sale-workflow
#--------------------------------------------------
# Change server configuration file
#--------------------------------------------------
echo -e "* Change server config file"
echo -e "sudo nano /etc/odoo-server.conf"
echo -e "Add /odoo/custom/addons/<repository> to end of addons_path"
echo -e "Save: Ctrl+X. Then, restart machine."
# Alternative: sudo su root -c "echo 'addons_path=/odoo/odoo-server/addons,/odoo/custom/addons,/odoo/custom/addons/department' >> /etc/odoo-server.conf"


