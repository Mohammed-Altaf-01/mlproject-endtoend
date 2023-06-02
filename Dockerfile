FROM python:3.10-slim-buster

# Creating app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY . .

# exposing and running the container 
EXPOSE 5000
CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]