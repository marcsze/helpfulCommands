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
			var1, var2, var3, var4, var5 = line.split("\t")
			
			add_data = ("INSERT INTO demographicinfo "
			"(EntryNumber, TissueCoreInformation_HistologyCore, MicroCTData_MicroCTCore, Sex, Age, PackYears) "
			"VALUES (%(test)s, %(test2)s, %(test3)s, %(test4)s, %(test5)s, %(test6)s)")
			
			if var3 == 1:
				sex = 'M'
			else:
				sex = 'F'
				
			print(x, var1, var2, sex, var4, var5)
			
			
			data = {'test':x, 'test2':var1, 'test3':var2, 
			'test4':sex, 'test5':var4, 'test6':var5}
			
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