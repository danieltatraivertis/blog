FROM python:3.6.4

RUN pip install \
  django==2.0.2 \
  Pillow==5.0.0 \
  django_admin_timeline==1.6.2 \
  django-ckeditor==5.4.0 \
  djangorestframework==3.7.7 \
  django-filter==2.0.0.dev1 \
  django-debug-toolbar==1.9.1 \
  psycopg2-binary==2.7.4 \
  uwsgi==2.0.16 \
  python-decouple==3.1 \
  coverage==4.5.1 \
  django-rosetta==v0.8.1 \
  django-simple-captcha==0.5.6 \
  django-extensions==1.9.9 \
  Werkzeug==0.14.1 \
  django_compressor==2.2
RUN apt update
RUN apt install -y gettext
RUN pip install git+https://github.com/groveco/django-sql-explorer.git
# COPY ./Djangoproject /code
# WORKDIR /code
# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
