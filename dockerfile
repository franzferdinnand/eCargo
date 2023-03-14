FROM python:3.10

RUN apt update
RUN mkdir /eCargo

WORKDIR /eCargo

COPY src ./src

COPY requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r ./requirements.txt

CMD ["python", "src/manage.py", "runserver", "0:8000"]

#docker build -t ecargo .
#docker run --rm -it -d -p 8010:8000 --name ecargo_kont ecargo
