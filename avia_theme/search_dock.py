import frappe
import re

def search_dock():
    # Check how Frappe renders the dock top app icon
    import glob
    js_files = glob.glob("/home/frappe/frappe-bench/apps/frappe/frappe/public/dist/js/desk.bundle.*.js")
    for f in js_files:
        with open(f, "r", encoding="utf-8") as fl:
            content = fl.read()
            # search for dock or app switcher
            matches = re.findall(r'(\b[a-zA-Z_-]*dock[a-zA-Z_-]*\b)', content, re.IGNORECASE)
            print(f"File {f}: found {len(set(matches))} dock matches: {list(set(matches))[:10]}")

            # Check app logo url in erpnext hooks
            erp_hooks = frappe.get_hooks(app_name="erpnext")
            print("ERPNext app_logo_url:", erp_hooks.get("app_logo_url"))
            print("ERPNext app_title:", erp_hooks.get("app_title"))
            
            avia_hooks = frappe.get_hooks(app_name="avia_theme")
            print("AVIA app_logo_url:", avia_hooks.get("app_logo_url"))
            print("AVIA app_title:", avia_hooks.get("app_title"))
            print("AVIA app_include_css:", avia_hooks.get("app_include_css"))
            print("AVIA app_include_js:", avia_hooks.get("app_include_js"))
            break
