FROM python:latest

WORKDIR /src

COPY requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /src

EXPOSE 5001

CMD ["python", "app.py"]
