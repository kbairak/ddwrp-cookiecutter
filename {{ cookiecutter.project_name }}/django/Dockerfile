FROM python:3.7
COPY django /django
WORKDIR /django
RUN pip install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:5000
