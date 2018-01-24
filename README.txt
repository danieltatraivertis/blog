Requirements:
Docker version 17.12.0-ce, build c97c6d6
Docker-compose version 1.18.0, build 8dd22a9


How to install:
$docker-compose build
creating .env based on .env-SAMPLE
$docker-compose exec django bash
$django-admin migrate
$django-admin collectstatic
