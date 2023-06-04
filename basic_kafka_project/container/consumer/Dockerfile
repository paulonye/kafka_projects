FROM python:3.7-slim

RUN pip install \
    kafka-python==1.4.6 \
    pandas \
    df2gspread \
    gspread \
    gspread_dataframe \
    oauth2client

WORKDIR /opt/consumer

#CMD [ "python" "consumer.py"]