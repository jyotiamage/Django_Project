FROM python:3

RUN mkdir /hello 

RUN mkdir /code

WORKDIR /code

ADD requirements.txt /code/

RUN pip install -r requirements.txt

ADD . /code/

EXPOSE 8090

CMD ["python", "./manage.py","runserver", "0.0.0.0:8090"]
