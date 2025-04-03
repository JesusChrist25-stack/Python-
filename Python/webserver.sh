#!/bin/bash

sudo systemctl install httpd -y
sudo systemctl start httpd 
sudo systemctl enable httpd 
wget https://www.free-css.com/assets/files/free-css-templates/download/page296/listrace.zip
unzip listrace.zip
cp -r listrace-v1.0/*  /var/www/html/
 
 