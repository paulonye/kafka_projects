"""This script shows how to simulate a real time data transfer while reading from a csv source file"""

from os.path import join, realpath, dirname
import pandas as pd
from sqlalchemy import create_engine
import csv
from time import ctime, sleep

#Getting the File Path
file_path = dirname(realpath(__file__))
dir_path = join(file_path, 'assests/acc_records.csv')

#USING THE DICTREADER METHOD
def read_by_dict_method():
	#reading in the file object
	file_object = open(dir_path, "r")
	data = csv.DictReader(file_object)

	#simulating real time data transfer
	for row in data:
		print(row)
		sleep(1)
	file_object.close()

#USING THE READER METHOD
#make a connection to the database
#ensure you create a database first
def read_by_reader_method():
	engine = create_engine(f"postgresql://{'root'}:{'root'}@{'localhost'}:{5432}/{'test_db'}")
	with open(dir_path, 'r') as file_object:
		data = csv.reader(file_object)
		#create the header row and skip through it
		header = next(data)
		#simulating a real time data transfer
		for row in data:
			df_row = pd.DataFrame([row], columns = header)
			print(df_row)
			df_row.to_sql('db_table_name', engine=engine, if_exists='append', index =False)
			print(f'committed to db at: {ctime()}')
			sleep(1)


if __name__ == '__main__':
	read_by_dict_method()




