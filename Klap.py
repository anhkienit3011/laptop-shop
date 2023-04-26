from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import*
import sys
from PyQt6.uic import loadUiType
import mysql.connector as con

ui, _ = loadUiType('Klap.ui')

class MainApp(QMainWindow, ui):
	def __init__(self):
		QMainWindow.__init__(self)
		self.setupUi(self)

		self.tabWidget.setCurrentIndex(0)
		self.tabWidget.tabBar().setVisible(False)
		self.menubar.setVisible(False)
#set login
		self.b01.clicked.connect(self.login)
		
#set laptop
		self.menu11.triggered.connect(self.show_add_new_lap_tab)
		self.menu12.triggered.connect(self.edit_lap)
		#find lap
		self.b41.clicked.connect(self.show_infor_laptop)
		#update button
		self.b42.clicked.connect(self.update_laptop_details)
		#delete button
		self.b43.clicked.connect(self.delete_latop_details)		
		self.menu13.triggered.connect(self.show_laptop_list)
		self.b71.clicked.connect(self.get_all_data_from_db)
		self.bt12.clicked.connect(self.save_laptop_details)
#set customer
		self.menu21.triggered.connect(self.show_add_new_customer)
		self.b31.clicked.connect(self.save_customer_details)
	#edit
		self.menu22.triggered.connect(self.edit_laptop)
		self.b51.clicked.connect(self.show_infor_customer)
		self.b52.clicked.connect(self.update_customer_details)
		self.b53.clicked.connect(self.delete_customer_details)
	#show customer list
		self.menu23.triggered.connect(self.show_customer_list)
		self.b61.clicked.connect(self.get_all_customer_from_db)
	#log out
		self.log_out.triggered.connect(self.logout)
#set invoice
		self.menu31.triggered.connect(self.show_add_new_invoice)
		self.b81.clicked.connect(self.add_lap_to_invoice)
		self.b82.clicked.connect(self.total_invoice)
		self.b83.clicked.connect(self.save_invoice)
# login form
	def login(self):
		un = self.tb01.text()
		pw = self.tb02.text()
		if(un=="admin" and pw == "admin"):
			self.menubar.setVisible(True)
			self.tabWidget.setCurrentIndex(1)
		else:
			QMessageBox.information(self,"Laptop shop management system","Invalid admin login details,Try agian !")
#logout
	def logout(self):
		
		
		self.tabWidget.setCurrentIndex(0)
		self.tb01.setText("")
		self.tb02.setText("")
# add new laptop
	def 	show_add_new_lap_tab(self):
		self.tabWidget.setCurrentIndex(2)
		self.fill_next_registration_number_lap()
	
	def fill_next_registration_number_lap(self):
		try:
			rn = 0
			mydb = con.connect(host="localhost",user="root",password="kientdt301120",db="laptop")
			cursor = mydb.cursor()
			cursor.execute("select * from laptop.laptops ")
			result = cursor.fetchall()
			if result:
				for lap in result:
					rn = rn + 1
			self.tb11.setText(str(rn+1))
		except con.Error as e :
			print("Error occured in select laptop reg number" )
	def save_laptop_details(self):
		try:
			
			mydb = con.connect(host="localhost",user="root",password="kientdt301120",db="laptop")
			cursor = mydb.cursor()
			registration_number = self.tb11.text()
			brand = self.tb12.text()
			model = self.tb13.text()
			price = self.tb14.text()
			quantity = self.tb15.text()

			qry = "insert into laptops (registration_number,brand,model,price,quantity) values(%s,%s,%s,%s,%s)"
			value=(registration_number,brand,model,price,quantity)
			cursor.execute(qry,value)
			mydb.commit()

			self.l12.setText("Laptop details saved successfully")
			QMessageBox.information(self,"Laptop shop magament system","Laptop details added successfully !")
		except con.Error as e :
			self.l12.setText("Error in save laptop form !" )
#edit laptop
	
	def edit_lap(self):
		self.tabWidget.setCurrentIndex(4)

	#find laptop
	def show_infor_laptop(self):
		
			a = self.tb40.text()
			try:
				mydb = con.connect(host="localhost",user="root",password="kientdt301120",db="laptop")
				cursor = mydb.cursor()

				qry= "SELECT laptop_id,registration_number,brand,model,price,quantity FROM laptop.laptops where status = 'active' "
				
				cursor.execute(qry)
				result = cursor.fetchall()
				for row in result:
					if row[3]==a:
						c = row
				try:
					self.tb41.setText(str(c[1]))
					self.tb42.setText(str(c[2]))
					self.tb43.setText(str(c[3]))
					self.tb44.setText(str(c[4]))
					self.tb45.setText(str(c[5]))
				except:
					QMessageBox.information(self,"Laptop shop management system","Invalid  details,Try agian !")
					self.tb41.setText("")
					self.tb42.setText('')
					self.tb43.setText('')
					self.tb44.setText('')
					self.tb45.setText('')
			except Exception as e :
				print("get data fail")
				print(e)
	#update lap
	def update_laptop_details(self):
		try:
			a = self.tb40.text()
			mydb = con.connect(host="localhost",user="root",password="kientdt301120",db="laptop")
			cursor = mydb.cursor()
			registration_number = self.tb41.text()
			brand = self.tb42.text()
			model = self.tb43.text()
			price = self.tb44.text()
			quantity = self.tb45.text()

			qry = "UPDATE  laptops SET registration_number = %s,brand= %s,model= %s,price= %s,quantity= %s WHERE model= %s  ; "
			value=(registration_number,brand,model,price,quantity,model)
			
			cursor.execute(qry,value)
			mydb.commit()

			
			QMessageBox.information(self,"Laptop shop magament system","Laptop details updated successfully !")
		except:
					QMessageBox.information(self,"Laptop shop management system","Invalid  details,Try agian !")
	#delete lap
	def delete_latop_details(self):
		try:
			a = self.tb40.text()
			b = 'dis'
			mydb = con.connect(host="localhost",user="root",password="kientdt301120",db="laptop")
			cursor = mydb.cursor()
			qry = "UPDATE laptops SET status = %s WHERE model= %s ; "
			value = (b,a)
			cursor.execute(qry,value)
			mydb.commit()

			QMessageBox.information(self,"Laptop shop magament system","Laptop details deleted successfully !")			
		except:
					QMessageBox.information(self,"Laptop shop management system","Invalid  details,Try agian !")

#function to getting data ( laptop list)
	def 	show_laptop_list(self):
		self.tabWidget.setCurrentIndex(7)
		
	def get_all_data_from_db(self):
		try:
			mydb = con.connect(host="localhost",user="root",password="kientdt301120",db="laptop")
			cursor = mydb.cursor()

			qry= "SELECT laptop_id,registration_number,brand,model,price,quantity FROM laptop.laptops where status = 'active'"
			cursor.execute(qry)
			result = cursor.fetchall()
			self.result_table.setRowCount(0)

			for row_number , row_data in enumerate(result):
				self.result_table.insertRow(row_number)

				for column_number,data in enumerate(row_data):
					self.result_table.setItem(row_number,column_number,QTableWidgetItem(str(data)))
			
	
		except Exception as e :
			print("get data fail")
			print(e)


#customer
	def 	show_add_new_customer(self):
		self.tabWidget.setCurrentIndex(3)
		self.fill_next_registration_number()
	
	def fill_next_registration_number(self):
		try:
			rn = 0
			mydb = con.connect(host="localhost",user="root",password="kientdt301120",db="laptop")
			cursor = mydb.cursor()
			cursor.execute("select * from customers ")
			result = cursor.fetchall()
			if result:
				for i in result:
					rn += 1
			self.l31.setText(str(rn+1))
		except con.Error as e :
			print("Error occured in select customer reg number" )
	def save_customer_details(self):
		try:
			
			mydb = con.connect(host="localhost",user="root",password="kientdt301120",db="laptop")
			cursor = mydb.cursor()
			registration_number = self.l31.text()
			Fn = self.l32.text()
			G = self.c31.currentText()
			A = self.l33.text()
			DOB = self.l34.text()
			E = self.l35.text()
			P = self.l36.text()
			Add = self.l37.text()
			

			qry = "insert into customers (registration_number,name,gender,age, date_of_birth,email,phone,address) values(%s,%s,%s,%s,%s,%s,%s,%s)"
			value=(registration_number,Fn,G,A,DOB,E,P,Add)
			cursor.execute(qry,value)
			mydb.commit()			
			QMessageBox.information(self,"Laptop shop magament system","Laptop details added successfully !")
		except con.Error as e :
			QMessageBox.information(self,"Laptop shop management system","Invalid  details,Try agian !")
#edit customer
	def edit_laptop(self):
		self.tabWidget.setCurrentIndex(5)
	#find customer
	def show_infor_customer(self):
		
			a = self.l51.text()
			try:
				mydb = con.connect(host="localhost",user="root",password="kientdt301120",db="laptop")
				cursor = mydb.cursor()

				qry= "SELECT id,registration_number,name,gender,age,date_of_birth,email,phone,address FROM laptop.customers where status = 'active' "
				
				cursor.execute(qry)
				result = cursor.fetchall()
				for row in result:
					if row[2]==a:
						c = row
				try:
					self.l52.setText(str(c[1]))
					self.l53.setText(str(c[2]))
					self.l54.setText(str(c[3]))
					self.l55.setText(str(c[4]))
					self.l56.setText(str(c[5]))
					self.l57.setText(str(c[6]))
					self.l58.setText(str(c[7]))
					self.l59.setText(str(c[8]))
				except:
					QMessageBox.information(self,"Laptop shop management system","Invalid  details,Try agian !")
					self.l52.setText('')
					self.l53.setText('')
					self.l54.setText('')
					self.l55.setText('')
					self.l56.setText('')
					self.l57.setText('')
					self.l58.setText('')
					self.l59.setText('')
			except Exception as e :
				print("get data fail")
				print(e)
	#update customer
	def update_customer_details(self):
		try:
			a = self.l51.text()
			mydb = con.connect(host="localhost",user="root",password="kientdt301120",db="laptop")
			cursor = mydb.cursor()
			registration_number = self.l52.text()
			name = self.l53.text()
			gender = self.l54.text()
			age = self.l55.text()
			dob = self.l56.text()
			phone = self.l57.text()
			email = self.l58.text()
			address = self.l59.text()

			qry = "UPDATE customers SET registration_number = %s,name= %s,gender= %s,age= %s,date_of_birth= %s,email = %s,phone=%s,address=%s WHERE name= %s  ; "
			value=(registration_number,name,gender,age,dob,phone,email,address,a)
			
			cursor.execute(qry,value)
			mydb.commit()

			
			QMessageBox.information(self,"Laptop shop magament system","Laptop details updated successfully !")
		except:
					QMessageBox.information(self,"Laptop shop management system","Invalid  details,Try agian !")
	#delete cus
	def delete_customer_details(self):
		try:
			a = self.l51.text()
			b = 'dis'
			mydb = con.connect(host="localhost",user="root",password="kientdt301120",db="laptop")
			cursor = mydb.cursor()
			qry = "UPDATE customers SET status = %s WHERE name = %s ; "
			value = (b,a)			
			cursor.execute(qry,value)
			mydb.commit()

			QMessageBox.information(self,"Laptop shop magament system","Customer details deleted successfully !")						
		except:
					QMessageBox.information(self,"Laptop shop management system","Invalid  details,Try agian !")
							
#function to getting data ( customer list)
	def 	show_customer_list(self):
		self.tabWidget.setCurrentIndex(6)
		
		
	
	def get_all_customer_from_db(self):
		try:
			mydb = con.connect(host="localhost",user="root",password="kientdt301120",db="laptop")
			cursor = mydb.cursor()

			qry= "SELECT id,registration_number,name,gender,age,date_of_birth,email,phone,address FROM laptop.customers where status = 'active' "
			cursor.execute(qry)
			result = cursor.fetchall()
			self.customer_table.setRowCount(0)

			for row_number , row_data in enumerate(result):
				self.customer_table.insertRow(row_number)

				for column_number,data in enumerate(row_data):
					self.customer_table.setItem(row_number,column_number,QTableWidgetItem(str(data)))
			
	
		except Exception as e :
			print("get data fail")
			print(e)
#invoice
	
	def 	show_add_new_invoice(self):
		self.tabWidget.setCurrentIndex(8)
	def add_lap_to_invoice(self):
		try:
			model = self.l83.text()
			quantity = self.l84.text()

			mydb = con.connect(host="localhost",user="root",password="kientdt301120",db="laptop")
			cursor = mydb.cursor()
			qry = f"SELECT price FROM laptops WHERE model = '{model}'"
			cursor.execute(qry)
			price = cursor.fetchone()[0]

		# Tìm hàng trống đầu tiên trong bảng để thêm dữ liệu
			empty_row_index = -1
			row_count = self.table_8.rowCount()
			for i in range(row_count):
				if self.table_8 .item(i,0) is None:
					empty_row_index = i
					break
			if empty_row_index == -1:
				empty_row_index = row_count
				self.table_8.setRowCount(row_count + 1)

			# Tạo đối tượng QTableWidgetItem để thêm vào bảng
			mod = QTableWidgetItem(model)
			qty = QTableWidgetItem(quantity)
			pr  = QTableWidgetItem(price)
			# add to row
			self.table_8.setItem(empty_row_index,0,mod)
			self.table_8.setItem(empty_row_index,2,qty)
			self.table_8.setItem(empty_row_index,1,pr)
		except:
			QMessageBox.information(self,"Laptop shop management system","Invalid  model,Try agian !")
	#total invoice
	def total_invoice(self):
		total = 0
		for row in range (self.table_8.rowCount()):
			qty = int(self.table_8.item(row,2).text())
			pr  = int(self.table_8.item(row,1).text())
			total += qty * pr
		self.l85.setText(str(total))
	#save invoice
	def save_invoice(self):
		try:
			
			mydb = con.connect(host="localhost",user="root",password="kientdt301120",db="laptop")
			cursor = mydb.cursor()
			time = self.l82.text()
			cus_name = self.l81.text()
			total = self.l85.text()
			qry = f"SELECT id FROM customers WHERE name = '{cus_name}'"
			cursor.execute(qry)
			customer_id = cursor.fetchone()[0]
			for row in range (self.table_8.rowCount()):	
				qty = int(self.table_8.item(row,2).text())
				model = self.table_8.item(row,0).text()
				price = self.table_8.item(row,1).text()
				qry1 = f"SELECT laptop_id FROM laptops WHERE model = '{model}'"
				cursor.execute(qry1)
				laptop_id = cursor.fetchone()[0]
				
				quantity = self.table_8.item(row,2).text()
				qry3 = "insert into invoices (customer_id,laptop_id,quantity,invoice_date,total) values(%s,%s,%s,%s,%s)"
				value=(customer_id,laptop_id,quantity,time,total)
				cursor.execute(qry3,value)
				mydb.commit()
			#update quantity...
			
			QMessageBox.information(self,"Laptop shop magament system","Invoice saved successfully !")
		except con.Error as e :
			QMessageBox.information(self,"Laptop shop management system","Invalid  details,Try agian !")
					
def main():
	app = QApplication(sys.argv)
	window = MainApp()
	window.setFixedHeight(784)
	window.setFixedWidth(780)
	window.show()
	app.exec()

if __name__ == '__main__':
	main()