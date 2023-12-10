FROM python:3.11.6

WORKDIR '/sentiment-analysis'
ADD . /sentiment-analysis

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 6000

CMD ["python3", "predictor.py"]
