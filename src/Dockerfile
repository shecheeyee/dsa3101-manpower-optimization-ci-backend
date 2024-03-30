FROM python:latest

EXPOSE 5000

COPY . /src

WORKDIR /src

RUN pip install -r requirements.txt

CMD python app.py