##Creating Docker image

FROM python:3.8-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python app.py
#CMD ["python", "app.py"]