FROM python:3.8

EXPOSE 5000
COPY . /app

WORKDIR /app

#COPY requirements.txt /app
RUN pip install  -r requirements.txt --upgrade pip
RUN pip install flask flask-wtf
RUN pip install python-dotenv
RUN pip install flask flask-login flask-sqlalchemy flask-wtf

#ENV PYTHONPATH "${PYTHONPATH}:/app/final-project/final_project:/app"

CMD ["python", "wsgi.py"]