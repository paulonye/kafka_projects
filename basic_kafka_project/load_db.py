import pandas as pd
from sqlalchemy import create_engine
import csv
from time import ctime, sleep

#reading in the file object
file_object = open('acc_records.csv', "r")
ext = csv.reader(file_object)

#skipping row heaer
header = next(ext)

#make a connection to the database
engine = create_engine(f"postgresql://{'root'}:{'root'}@{'localhost'}:{5432}/{'test_db'}")

#simulating real time data transfer to DB
for row in ext:
	df_row = pd.DataFrame([row], columns = header)
	print(df_row)
	df_row.to_sql('transactions', engine, if_exists='append', index=False)
	print(f'committed to db at: {ctime()}')
	sleep(15)






