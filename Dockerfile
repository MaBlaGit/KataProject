FROM python:2.7

WORKDIR /tmp
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /usr/src/KataProject/
ADD cities/ /usr/src/KataProject/cities/

ADD views/ /usr/src/KataProject/views/

ADD simple_bottle_app.py /usr/src/KataProject/
ADD weather_api_script.py /usr/src/KataProject/

