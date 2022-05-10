FROM python:latest
WORKDIR /usr/app
COPY Morsecode.py ./
CMD [ "python", "./Morsecode.py"]