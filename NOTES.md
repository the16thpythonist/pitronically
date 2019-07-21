# NOTES

This file will contain important notes for how to handle certain things 
with this project and overall things, that I have learned over the course 
of working on it

### How to run the local environment

Using the docker-compose command, the whole web server together with the 
database can be started with:

```bash
$ docker-compose -f local.yml up
```

To run any django manage.py operations:

```bash
$ docker-compose -f local.yml run --rm django python manage.py [COMMAND]
```

### Does the production.yml work here locally?

No, it does not. This is because the production.yml attempts to start 
its own Gunicorn web server on port 80. This causes a conflict because I already 
have an apache server running on this laptop, which also operates on port 80

### How to access the docker containers

To access the terminal of the docker containers the "sh" command has to be ran on them:

```bash
$ docker-compose -f local.yml run --rm django sh
```

And then a terminal from within the container will open, where stuff can be performed
