FROM python:3.11.5

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY src/requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY src /usr/src/app/

EXPOSE 3000

ENTRYPOINT [ "gunicorn" ]
CMD ["--workers", "4", "--bind", "0.0.0.0:3000", "swagger_server.__main__:app"]