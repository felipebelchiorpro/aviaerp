import frappe

def list_workspaces():
    ws = frappe.get_all("Workspace", fields=["name", "title", "module", "public"])
    print(f"Total Workspaces: {len(ws)}")
    for w in ws:
        print(f" - {w.name} (title: '{w.title}', module: '{w.module}')")
