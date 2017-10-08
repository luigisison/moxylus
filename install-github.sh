#!/bin/bash
################################################################################
# Script for installing GitHub
# Original Author: Luigi Sison
#-------------------------------------------------------------------------------
# This script will install GitHub on your Ubuntu 16.04 server.
#-------------------------------------------------------------------------------
# Go to Ubuntu directory where you want to install the software. For example:
# cd /opt
# Place this script in the directory:
# sudo wget https://raw.githubusercontent.com/luigisison/moxylus/master/install-github.sh
# Make the file executable:
# sudo chmod +x install-github.sh
# Execute the script to install Odoo:
# ./install-github.sh

##fixed parameters
#Choose the GitHub version which you want to install.
OE_VERSION="2.9.5"
#set your GitHub Account
OE_USER=\”Luigi Sison\”
OE_USER_EMAIL="lsison@moxylus.com"

#--------------------------------------------------
# Install GitHub
#--------------------------------------------------
echo -e "\n---- Install GitHub dependencies ----"
sudo apt-get install build-essential libssl-dev libcurl4-gnutls-dev libexpat1-dev gettext unzip

echo -e "\n---- Install Git ----"
cd /opt
sudo wget "https://github.com/git/git/archive/v$OE_VERSION.zip" -O git.zip
sudo unzip git.zip
cd git-*
sudo make prefix=/usr/local install

echo -e "\n---- Register GitHub account ----"
git config --global user.name "Luigi Sison"
git config --global user.email $OE_USER_EMAIL
git config --list

echo "Done! Your GitHub Account is set up. Specifications:"
echo "User Name: Luigi Sison"
echo "User service: $OE_USER_EMAIL"
