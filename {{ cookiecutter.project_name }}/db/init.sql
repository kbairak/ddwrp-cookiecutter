CREATE USER {{ cookiecutter.project_name }};
CREATE DATABASE {{ cookiecutter.project_name }};
GRANT ALL PRIVILEGES ON DATABASE {{ cookiecutter.project_name }} TO {{ cookiecutter.project_name }};
