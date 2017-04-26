FROM alpine:latest
MAINTAINER platform
RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
