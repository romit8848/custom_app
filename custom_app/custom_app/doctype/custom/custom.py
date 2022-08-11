# Copyright (c) 2022, romit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class custom(Document):
	def validate(self):
		if self.email in ["iuok@gmail.com","abc@gmail.com"]:
			frappe.throw("email iuok exist")

		
	
	def before_save(self):
		if self.lname == "xyz":
			frappe.throw("change last name")

		for item in self.custom_list:
			item.amount = item.rate * item.quantity
			frappe.msgprint("amount added")
	
	def before_insert(self):
		if self.lname == "abc":
			frappe.msgprint("change fname")

	def after_insert(self):
		if self.lname == "op":
			frappe.throw("last name is ok")

	def before_submit(self):
		if self.lname == "mn":
			frappe.msgprint("last name exicute")

	def on_submit(self):
		if self.lname == "pa":
			frappe.throw("last name exicute")
		
	def before_update_after_submit(self):
		if self.lname == "ap":
			frappe.throw("last name exicute")

	def on_update_after_submit(self):
		if self.age == 15:
			frappe.throw("age is less than 18") 

	def before_cancel(self):
		if self.age == 18:
			frappe.throw(" age is 18")

	def on_cancel(self):
		if self.age == 20:
			frappe.throw("age is 20")

	def on_trash(self):
		if self.age == 25:
			frappe.throw("age is 25")

	def after_delete(self):
		if self.age == 30:
			frappe.msgprint("deleted")	

def validate(self,method):
	if self.age == 21:
		frappe.msgprint("young")

	if self.date == "2022-08-06":
		frappe.msgprint("today date")

def before_save(self,method):
	if self.lname == "lname":
		frappe.msgprint("last name invalid")

def before_insert(self,method):
	if self.email == "test":
		frappe.msgprint("email invalid")

def article(self,method):
	if 	self.select == "yes":
		frappe.msgprint("right")

def munn(self,method):
	if self.select == "no":
		frappe.msgprint("false")