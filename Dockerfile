FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install setuptools==39.1.0
RUN pip install pyparser==1.0
RUN pip install pyparsing==2.1.0
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "run.py"]
