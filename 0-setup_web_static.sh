#!/usr/bin/env bash
# A Bash script that sets up your web servers for the deployment of web_static
if ! which nginx; then
  sudo apt-get update
  sudo apt-get upgrade -y
  sudo apt-get install -y nginx
fi

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

HTML=\
"<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

echo "${HTML}" | sudo tee /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

NEW_CONFIG='location /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n'

sed -i "/listen 80 default_server;/a\        ${NEW_CONFIG}" /etc/nginx/sites-enabled/default

service nginx restart
