FROM alpine:latest

ADD . /bsm
COPY project.toml .


WORKDIR /bsm




RUN pip install uv 
RUN uv pip install -r pyproject.toml

RUN python manage.py migrate
RUN python manage.py runserver

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "bsapi.wsgi"]