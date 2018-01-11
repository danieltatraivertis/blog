FROM python:3.6.4
COPY ./Djangoproject /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
