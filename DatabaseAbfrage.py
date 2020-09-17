import cx_oracle
import os
import sys

dir path = os.path.dirname(os.path.realpath(__file__))
sys.path.append('{}'/..config'.format(dir_path))

from config import example

def executeQueryAll(schema):
  try:
    con = cx_Oracle.connect('{}/{}@{}/{}'.format(schema[0],schema[1],schema[2],schema[3]))
	cursor = con.cursor()
	
	if cursor: 
	  print("Connection successful")
	
	else: 
	  print("Connection not successful")
  
  except cx_Oracle.DatabaseError as e:
    x = e.args[0]
	print('DB error occured. ORA={}'.format(x))
  
  finally:
    con.close()

executeQueryAll(example)