FROM python:3.7.3

RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt

EXPOSE 8080
CMD ["python3", "/code/app.py"]