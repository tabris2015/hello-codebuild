# FastAPI as a lambda function example

This is an example of a fastapi application that can be packaged and deployed as a lambda
function on AWS.

## Requirements

- AWS CLI
- SAM CLI
- Python 3.7+
- Virtualenv or Conda for virtual environments management
- Docker + docker compose for local development

## Local development

You can start local service using `docker compose`

```bash
$ docker-compose up
```

And then access to `localhost:8000/docs`
