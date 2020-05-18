FROM python:3

ADD server.py /

RUN pip install mysql-connector python-dotenv

EXPOSE 5000

CMD ["python", "./server.py" ]