FROM python:3.7-slim
WORKDIR /phonebook
RUN python -m pip install --upgrade pip
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt
COPY . /phonebook
EXPOSE 8000
CMD ["python3", "./manage.py", "runserver", "0.0.0.0:8000"]
