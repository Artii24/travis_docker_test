FROM alpine:latest

RUN apk add bash python3
WORKDIR /work
COPY script.sh
CMD bash "/work/script.sh"
