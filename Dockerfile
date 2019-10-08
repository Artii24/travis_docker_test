FROM alpine:latest

RUN apk add bash python3
WORKDIR /work
COPY *.py
CMD bash "/work/script.py"
