FROM python:3.6.4

RUN pip install \
  django==2.0.1 \
  Pillow==5.0.0 \
  django_admin_timeline==1.6.2 \
  django-ckeditor==5.4.0 \
  djangorestframework==3.7.7 \
  django-filter==2.0.0.dev1

COPY ./Djangoproject /code
WORKDIR /code
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
