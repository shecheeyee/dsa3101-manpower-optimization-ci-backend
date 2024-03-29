FROM python:latest
COPY . /src
WORKDIR /src
RUN pip install -r ../requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"] 
