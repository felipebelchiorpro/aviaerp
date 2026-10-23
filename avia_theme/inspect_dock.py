import re

with open("/home/frappe/frappe-bench/apps/frappe/frappe/public/dist/js/desk.bundle.PNLZH7KQ.js", "r") as f:
    text = f.read()

idx = text.find("make_dock_item")
if idx != -1:
    print(text[max(0, idx-100):min(len(text), idx+600)])
else:
    print("Not found")
