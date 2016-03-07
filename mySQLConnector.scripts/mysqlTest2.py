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
			var1, var2, var3, var4, var5, var6, var7 = line.split("\t")
			
			add_data = ("INSERT INTO microctdata "
			"(MicroCTCore, TissueCoreInformation_HistologyCore, Lm, LnLm, SurfaceArea, LnSurfaceArea, TerminalBronchioles) "
			"VALUES (%(test)s, %(test2)s, %(test3)s, %(test4)s, %(test5)s, %(test6)s, %(test7)s)")
			
			print(var1, var2, var3, var4, var5, var6, var7)
			
			data = {'test':var2, 'test2':var1, 'test3':var3, 
			'test4':var4, 'test5':var5, 'test6':var6, 'test7':var7}
			
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