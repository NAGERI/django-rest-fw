# Running a python API using drf

This project involves a demo client in the `/py-client` folder.
The backend, having the drf (Django Rest Framework) is located in the `/backend` folder.

## Installation.

- Clone the project into a folder name of your choice by replacing `<folder-name>` below.

```git
git clone https://github.com/NAGERI/django-rest-fw.git <folder-name>
```

- Install `python 3.10.7` on your machine.
- Configure your the virtual environment using `pip` package manager.

  ```
  pip install virtualenv
  ```

- Inside the project folder create the virtual environment.

  ```
  virtualenv env
  ```

- Activate your virtual environment.

  ```ps1
  env/Scripts/Activate.ps1   # for windows
  or
  source env/Scripts/activate # for bash
  ```

- Install the requirements
  ```cmd
  pip install -r requirements.txt
  ```

## Usage

### Running the backend

Navigate to the `/backend` folder and run the server:

```cmd
python manage.py runserver 8000
```

### Running the client

Navigate `/py-client` folder and run:

```py
python basic.py # or create.py or detail.py to test the API endpoints.
```
