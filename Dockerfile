#Python base image
FROM python:3

#Copy required files to the image
COPY requirements.txt requirements.txt
COPY /src/. /app

#Install python dependencies
RUN pip install -r requirements.txt

#Start the application
CMD python /main.py