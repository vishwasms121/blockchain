FROM python:3.8
ADD web3helpers.py .
ADD webserver.py .
ADD .env .
RUN pip install web3
RUN pip install python-decouple
EXPOSE 8080
CMD ["python3", "webserver.py"]