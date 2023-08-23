FROM python:3.11
COPY . .
RUN pip install requeriments.txt
CMD [ "python", "./echobot.py" ]