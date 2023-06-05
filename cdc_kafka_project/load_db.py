import pandas as pd
import psycopg2 
import csv
from time import ctime, sleep

#reading in the file object
file_object = open('acc_records.csv', "r")
ext = csv.reader(file_object)

#skipping row heaer
header = next(ext)

#make a connection to the database
conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' port=5433 password='postgres'")
curr = conn.cursor()
print('here')

#simulating real time data transfer to DB
for row in ext:
	curr.execute(
            "INSERT INTO public.transactions (date, customer_id, payment_method, delivery_status, duration, orders, amount) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6]),)
	#print(df_row)
	sleep(15)
	conn.commit()
	print(f'committed to db at: {ctime()}')
curr.close()






