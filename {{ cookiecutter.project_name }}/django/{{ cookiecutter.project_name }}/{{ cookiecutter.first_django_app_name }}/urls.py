import {{ cookiecutter.project_name }}.{{ cookiecutter.first_django_app_name }}.views

from django.urls import path

urlpatterns = [
    path('', {{ cookiecutter.project_name }}.{{ cookiecutter.first_django_app_name }}.views.index, name="index")
]
