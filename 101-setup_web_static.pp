# A puppet script that configure a web static
exec {'Command':
command  => 'sudo apt-get update && sudo apt-get -y install nginx && sudo mkdir -p /data/web_static/releases/test/ && sudo mkdir -p /data/web_static/shared/ && sudo touch /data/web_static/releases/test/index.html && echo "Sample Content" | sudo tee /data/web_static/releases/test/index.html && sudo ln -sf /data/web_static/releases/test/ /data/web_static/current && sudo chown -R ubuntu /data/ && sudo chgrp -R ubuntu /data/ && sudo sed -i "36i \ \tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n}" /etc/nginx/sites-available/default && sudo service nginx restart',
provider => shell,
}
