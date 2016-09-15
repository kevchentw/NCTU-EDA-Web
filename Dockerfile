FROM ubuntu:16.04
RUN apt update -y
RUN apt upgrade -y
RUN apt install -y python python-pip git
RUN pip install --upgrade pip
RUN pip install django
EXPOSE 8080
COPY eda.sh /eda.sh
ENTRYPOINT ["bash", "eda.sh"]
