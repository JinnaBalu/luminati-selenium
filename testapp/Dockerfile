FROM python:3.7

WORKDIR /app
COPY ./requirements.txt .
COPY app .

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD [ "python", "-u", "app.py" ]