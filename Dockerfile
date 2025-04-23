FROM ubuntu:latest
LABEL authors="kacpe"

ENTRYPOINT ["top", "-b"]