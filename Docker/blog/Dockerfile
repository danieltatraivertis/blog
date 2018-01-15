FROM python:3.6.4
RUN pip install django Pillow django_admin_timeline
COPY ./Djangoproject /code
WORKDIR /code
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
