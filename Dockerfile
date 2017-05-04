FROM ubuntu

WORKDIR /tmp

RUN mkdir -p /usr/src/KataProject/
ADD cities/ /usr/src/KataProject/cities/
ADD ./cities/city_list.txt /usr/src/KataProject/cities/

ADD views/ /usr/src/KataProject/views/
ADD .views/current_weather.tpl /usr/src/KataProject/views/
ADD ./views/current_weather_more_cities.tpl /usr/src/KataProject/views/
ADD ./views/error_page.tpl /usr/src/KataProject/views/
ADD ./views/index_page.tpl /usr/src/KataProject/views/
ADD ./views/selected_city_from_cities.tpl /usr/src/KataProject/views/

ADD simple_bottle_app.py /usr/src/KataProject/
ADD weather_api_script.py /usr/src/KataProject/
RUN apt-get update
RUN apt-get install python-pip -y

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

EXPOSE 8080
ENTRYPOINT ["/usr/bin/python", "/usr/src/KataProject/simple_bottle_app.py"]

