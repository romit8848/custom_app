frappe.ui.form.on('Item', {
	refresh(frm) {
    if (frm.doc.is_stock_item) {
			frm.add_custom_button(__("Stock Balance"), function() {
				frappe.route_options = {
					"item_code": frm.doc.name
				};
				frappe.set_route("query-report", "Stock Balance");
			},__("View"));

			
			frm.add_custom_button(__("Stock Ledger"), function() {
				frappe.route_options = {
					"item_code": frm.doc.name
				};
				frappe.set_route("query-report", "Stock Ledger");
			}, __("View"));

        }
        
        if (frm.doc.is_fixed_asset) {
			frm.trigger('is_fixed_asset');
			frm.trigger('auto_create_assets');
		}
        
        frm.set_intro();

	    if (frm.doc.has_variants) {
			frm.set_intro(__("This Item is a Template and cannot be used in transactions. Item attributes will be copied over into the variants unless 'No Copy' is set"), true);

			frm.add_custom_button(__("Show Variants"), function() {
				frappe.set_route("List", "Item", {"variant_of": frm.doc.name});
			}, __("View"));
			
			
			frm.add_custom_button(__("Item Variant Settings"), function() {
				frappe.set_route("Form", "Item Variant Settings");
			}, __("View"));

			frm.add_custom_button(__("Variant Details Report"), function() {
				frappe.set_route("query-report", "Item Variant Details", {"item": frm.doc.name});
			}, __("View"));

	        
	    }
	    
	    

        cur_frm.set_df_property("weight_per_unit", "read_only",1);
	}

});