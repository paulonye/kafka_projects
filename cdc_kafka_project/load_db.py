import pandas as pd
import psycopg2 
import csv
from time import ctime, sleep

#reading in the file object
file_object = open('../assests/acc_records.csv', "r")
ext = csv.DictReader(file_object)

#make a connection to the database
conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' port=5433 password='postgres'")
curr = conn.cursor()

#simulating real time data transfer to DB
for row in ext:
	#date, customer_id, payment_method, delivery_status, duration, orders, amount = row
	curr.execute(
            "INSERT INTO public.transactions (date, customer_id, payment_method, delivery_status, duration, orders, amount) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            #(date, customer_id, payment_method, delivery_status, duration, orders, amount),)
			(row["date"], row["customer_id"], row["payment_method"], row["delivery_status"], row["duration"], row["orders"], row["amount"]),)
	#print(df_row)
	sleep(15)
	conn.commit()
	print(f'committed to db at: {ctime()}')

#closing database connection
curr.close()
#closing the file object
file_object.close()






