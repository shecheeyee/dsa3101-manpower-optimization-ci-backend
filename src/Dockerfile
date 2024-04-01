FROM python:latest

EXPOSE 5001

COPY . /src

WORKDIR /src

RUN pip install -r requirements.txt

COPY app.py /src
CMD python app.py