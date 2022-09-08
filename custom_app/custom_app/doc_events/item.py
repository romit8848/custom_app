# import frappe

# def validate(self,method):
#     frappe.msgprint("input data saved")

#     if self.item_name == "close":
#         frappe.msgprint("item name save")
        
#     if self.over_billing_allowance == 0:
#         frappe.msgprint("not any persantage of over billing allowance")

#     if self.min_order_qty < 1:
#         frappe.msgprint("please Enter Order Quantity ")

#     if self.brand in [None,""]:
#         frappe.msgprint("Please Enter Brand Name")

#     if self.lead_time_days != int(self.warranty_period):
#         frappe.msgprint("lead time day is not same warranty period")
    
#     if self.lead_time_days == int(self.warranty_period):
#         frappe.msgprint("lead time day is  same warranty period")

#     if self.end_of_life < '2099-12-31':
#         frappe.msgprint(("End of life  {0}").format(self.end_of_life))

#     if self.min_order_qty != 0:
#         frappe.msgprint(("your order quanty is {0} ").format(self.min_order_qty))

#     if self.valuation_method in [None,""]:
#         frappe.throw("please select valuation Method")

#     if self.valuation_method in ["FIFO","Moving Average"]:  
#         frappe.msgprint(("selcet valuation method is {0}").format(self.valuation_method))

#     for x in self.uoms:
#         frappe.msgprint(x.uom)
#         frappe.msgprint(str(x.conversion_factor))

#     if not self.is_stock_item:
#         frappe.throw("please check maintain stock")

#     if not self.valuation_rate:
#         frappe.throw("Enter Valuation rate")

#     if not self.include_item_in_manufacturing:
#         frappe.throw("include item manufacture not check")

#     if self.has_batch_no:
#         if not (self.has_expiry_date or self.create_new_batch or self.batch_number_series):
#             frappe.throw("please select one checkbox")

#     if self.has_serial_no:
#         if not self.serial_no_series:
#             frappe.throw("please enter series")

#     if self.safety_stock >= self.min_order_qty:
#         frappe.throw("not availble stock")

#     for idx, x in enumerate(self.customer_items):
#         if x.idx == 2 and x.ref_code == "456789":
#             frappe.msgprint("change referral code")
 
#     for idx, x in enumerate(self.item_defaults):
#         if x.idx == 1 and x.default_price_list == "abc":
#             frappe.msgprint(("Price list ({})").format(x.default_price_list))

#         if x.idx == 1 and x.income_account == "Salary - t":
#             frappe.msgprint("Income account is salary-t")


#     for x in self.barcodes:
#         if x.barcode_type in ["", None]:
#             frappe.msgprint("enter barcode type")


#     self.purchase_uom = "Nos"

#     if self.enable_deferred_revenue and self.no_of_months:
#         frappe.msgprint(("Deferred Revenue Experience is {0} moths").format(self.no_of_months))

#     if self.enable_deferred_expense and self.no_of_months_exp:
#         frappe.msgprint(("Deferred expense Experience is {0} moths").format(self.no_of_months_exp))

#     self.country_of_origin = "India"
#     frappe.msgprint(("your country is {}").format(self.country_of_origin))

#     self.deferred_revenue_account = "Creditors - t"
#     self.deferred_expense_account = "Cash - t"

#     self.hub_warehouse = "All Warehouses - t"

#     after_insert(self,method)

# def before_save(self,method):
#     if self.stock_uom == "Nos":
#         frappe.msgprint("Unit of Measure is Nos")

# def before_insert(self,method):
   
#     if self.valuation_rate == 0:
#         frappe.msgprint("not change in valuation rate")


#     if int(self.warranty_period) < 10:
#         frappe.msgprint("Warranty period added")
#         frappe.msgprint(("please enter warrenty period is {0}").format(self.warranty_period))

# def after_insert(self,method):
#     if self.shelf_life_in_days == 0:
#         frappe.msgprint("Enter Shelf Life Days") 



 


