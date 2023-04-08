#!/usr/bin/env bash
# A Bash script that sets up your web servers for the deployment of web_static

# Install Nginx if it not already installed
# Create the folder /data/ if it doesn’t already exist
# Create the folder /data/web_static/ if it doesn’t already exist
# Create the folder /data/web_static/releases/ if it doesn’t already exist
# Create the folder /data/web_static/shared/ if it doesn’t already exist
# Create the folder /data/web_static/releases/test/ if it doesn’t already exist
# Create a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)
#	Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder. If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
# Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist). This should be recursive; everything inside should be created/owned by this user/group.
# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static). Don’t forget to restart Nginx after updating the configuration:
#	Use alias inside your Nginx configuration

# install and configure nginx to serve some content
if ! which nginx > /dev/null 2>&1; then
  sudo apt-get update
  sudo apt-get upgrade -y
  sudo apt-get install -y nginx
fi

sudo mkdir -p /data/web_static/shared
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
