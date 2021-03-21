FROM python:3.9
EXPOSE 5000
COPY . /pythonProject
WORKDIR /pythonProject
RUN pip install pipenv && pipenv install --system
CMD ["python", "app.py"]
