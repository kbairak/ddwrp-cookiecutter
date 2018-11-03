from django.apps import AppConfig


class {{ cookiecutter.first_django_app_name|capitalize }}Config(AppConfig):
    name = '{{ cookiecutter.first_django_app_name }}'
