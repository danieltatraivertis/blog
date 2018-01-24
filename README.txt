Requirements:
Docker version 17.12.0-ce, build c97c6d6
Docker-compose version 1.18.0, build 8dd22a9

How to install:
sudo ./init-project.sh
cd /blog
$sudo docker-compose up -d
$sudo docker-compose exec django bash
$$cd /code
$$sudo init-django.sh
