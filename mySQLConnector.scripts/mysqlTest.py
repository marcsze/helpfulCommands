#! python
#mysqlTest.py

from __future__ import print_function
import mysql.connector, sys


def commandLine():
	commands = sys.argv
	readTable = commands[1]
		
	return readTable

def populateTable(readTable):
	cnx = mysql.connector.connect(user='root', password='insertpassword', 
	database='copdtissuedatabase')
	cursor = cnx.cursor()
	
	myTable = open(readTable, 'r')
	x = 0
	for line in myTable:
		if x > 0:
			var2, var3, var4, var5, var6 = line.split("\t")
			
			add_data = ("INSERT INTO tissuecoreinformation "
			"(EntryNumber, HistologyCore, PatientID, SliceNumber, Phenotype, DiseaseStatus) "
			"VALUES (%(test)s, %(test2)s, %(test3)s, %(test4)s, %(test5)s, %(test6)s)")
			
			print(x, var2, var3, var4, var5, var6)
			
			data = {'test':x, 'test2':var2, 'test3':var3, 
			'test4':var4, 'test5':var5, 'test6':var6}
			
			cursor.execute(add_data, data)
			
			x = x + 1
		else:	
			x = x + 1

	cnx.commit()
	cursor.close()
	cnx.close()
	
def main():
	readTable = commandLine()
	populateTable(readTable)
	
	
	
	
if __name__ == '__main__': main()


