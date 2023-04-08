#!/usr/bin/env bash
# A Bash script that sets up your web servers for the deployment of web_static
if ! which nginx; then
  sudo apt-get update
  sudo apt-get upgrade -y
  sudo apt-get install -y nginx
fi

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

HTML_CONTENT=\
"
<html>
	<head></head>
	<body>
		<h1> Welcome to static site deployment </h1>
	</body>
</html>
"
echo "${HTML_CONTENT}" | sudo tee /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

NEW_CONFIG="listen 80 default_server;\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}\n"

sed -i "s/listen 80 default_server;/${NEW_CONFIG}/" /etc/nginx/sites-enabled/default

service nginx restart
