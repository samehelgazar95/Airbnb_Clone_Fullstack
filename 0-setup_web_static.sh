#!/usr/bin/env bash
# Fuck Fabric3==1.14.post1 installation guide,
# It took me almost 5 hours!


sudo apt -y update
sudo apt -y install nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

cd /data/web_static/releases/test || exit
echo 'Yel3an abo el Fabric3==1.14.post1' > index.html

sudo ln -sf  /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo tee /etc/nginx/sites-available/default > /dev/null << 'EOF'
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;

        server_name _;

        error_page 404 /error_404.html;

        add_header X-Served-By $hostname;

        location /hbnb_static {
            alias /data/web_static/current;
        }

        location / {
            try_files $uri $uri/ =404;
        }
}
EOF

sudo service nginx restart
