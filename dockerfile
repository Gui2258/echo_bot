FROM python:3.11
COPY . .
RUN pyrhon -m pip install -r requeriments.txt
CMD [ "python", "./echobot.py" ]