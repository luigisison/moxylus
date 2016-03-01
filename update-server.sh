#!/bin/bash
################################################################################
# Script for installing updates.
# Original Source: http://askubuntu.com/questions/196768/how-to-install-updates-via-command-line
#-------------------------------------------------------------------------------
# This script will install Odoo Community on your Ubuntu 14.04 server.
# It can install multiple Odoo instances in one Ubuntu because of the different xmlrpc_ports.
#-------------------------------------------------------------------------------
# Go to Ubuntu directory where you want to install the software. For example:
# cd /opt
# Place this script in the directory:
# sudo wget https://raw.githubusercontent.com/luigisison/moxylus/master/update-server.sh
# Make the file executable:
# sudo chmod +x update-server.sh
# Execute the script:
# ./update-server.sh
################################################################################

sudo apt-get update        # Fetches the list of available updates
sudo apt-get upgrade       # Strictly upgrades the current packages
sudo apt-get dist-upgrade  # Installs updates (new ones)
