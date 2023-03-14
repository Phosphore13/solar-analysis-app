#the base image to be used for docker image, here we are using python 3.8
FROM python:3.8-slim-buster

#working directory inside the container
WORKDIR /app

#copy the requirement.txt file
COPY requirements.txt requirements.txt

#install the python package inside the container
RUN pip3 install -r requirements.txt

#to copy all the files
COPY . .

#default comand to be executed with app.py as argument
CMD [ "python3", "app.py" ]
