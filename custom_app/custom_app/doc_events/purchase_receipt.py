import frappe

from frappe.utils import cint

def on_submit(self,method):
    if self.supplier_delivery_note and cint(frappe.db.get_value("Stock Settings",None,"check_supplier_invoice_uniqueness__for_purchase_receipt")) == 1:
        if frappe.db.sql("""
                SELECT 
                    name
                from 
                    `tabPurchase Receipt`
                WHERE
                    supplier_delivery_note = '{}' and supplier = '{}' and  docstatus = 1
                    and name != '{}' and posting_date between '2022-04-01' and '2023-03-31'
                """.format(self.supplier_delivery_note, self.supplier, self.name)):
            frappe.throw("Supplier Invoice No Already Exists")