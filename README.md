# Django-Sample-Blog

## Initial create project

### Migrate

```
docker-compose run python3 python manage.py migrate
```

### Create superuser

```
docker-compose run python3 python manage.py createsuperuser
```

```log
Username (leave blank to use 'root'): root 
Email address: root@sample.com
Password:
Password (again):
Superuser created successfully.
```
