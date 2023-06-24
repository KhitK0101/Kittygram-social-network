 server {
    server_name 84.201.179.250 mynote2023test.ddns.net;

    location /api/ {
        proxy_pass http://127.0.0.1:8000;
    }

    location /admin/ {
        proxy_pass http://127.0.0.1:8000;
    }

    location / {
        root   /var/www/taski;
        index  index.html index.htm;
        try_files $uri /index.html;
    }


    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/mynote2023test.ddns.net/fullchain.pem; # managed by Certbot  
    ssl_certificate_key /etc/letsencrypt/live/mynote2023test.ddns.net/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}

 server {
    if ($host = mynote2023test.ddns.net) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    listen 80;
    server_name 84.201.179.250 mynote2023test.ddns.net;
    return 404; # managed by Certbot


}

 server {
    server_name 84.201.179.250 kittygramorig.myvnc.com;

    location /api/ {
        proxy_pass http://127.0.0.1:8080;
    }

    location /admin/ {
        proxy_pass http://127.0.0.1:8080;
    }

    location / {
        root   /var/www/infra_sprint1;
        index  index.html index.htm;
        try_files $uri /index.html;
    }

    location /media/ {
        alias /var/www/infra_sprint1/media/;
    }


    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/kittygramorig.myvnc.com/fullchain.pem; # managed by Certbot  
    ssl_certificate_key /etc/letsencrypt/live/kittygramorig.myvnc.com/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}


 server {
    if ($host = kittygramorig.myvnc.com) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    server_name 84.201.179.250 kittygramorig.myvnc.com;
    listen 80;
    return 404; # managed by Certbot


}