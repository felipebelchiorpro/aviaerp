import frappe

def run():
    frappe.db.begin()

    # 1. Update Website Settings
    try:
        ws = frappe.get_doc("Website Settings")
        ws.app_name = "AVIA"
        ws.app_logo = "/assets/avia_theme/images/avia_logo_clean_white.png"
        ws.favicon = "/assets/avia_theme/images/avia_favicon.png"
        ws.splash_image = "/assets/avia_theme/images/avia_app_icon.png"
        ws.copyright = "Grupo Belchior"
        ws.disable_signup = 1
        ws.hide_footer_signup = 1
        ws.footer_powered = ""
        ws.save(ignore_permissions=True)
        print("[✓] Website Settings configurado como AVIA!")
    except Exception as e:
        print("[!] Erro ao atualizar Website Settings:", e)

    # 2. Update Navbar Settings
    try:
        nb = frappe.get_doc("Navbar Settings")
        nb.app_logo = "/assets/avia_theme/images/avia_logo_clean_white.png"
        nb.save(ignore_permissions=True)
        print("[✓] Navbar Settings configurado com logo AVIA!")
    except Exception as e:
        print("[!] Erro ao atualizar Navbar Settings:", e)

    # 3. Update System Settings
    try:
        ss = frappe.get_doc("System Settings")
        ss.app_name = "AVIA"
        ss.save(ignore_permissions=True)
        print("[✓] System Settings app_name atualizado para AVIA!")
    except Exception as e:
        print("[!] Erro ao atualizar System Settings:", e)

    # 4. Enforce Dark Desk Theme on all users
    try:
        users = frappe.get_all("User", filters={"user_type": "System User"}, fields=["name"])
        for u in users:
            frappe.db.set_value("User", u.name, "desk_theme", "Dark")
        print(f"[✓] Tema Dark aplicado a todos os {len(users)} usuarios do sistema!")
    except Exception as e:
        print("[!] Erro ao atualizar tema dos usuarios:", e)

    # 5. Commit database changes
    frappe.db.commit()

    # 6. Clear all caches
    frappe.clear_cache()
    print("[✓] Cache geral e cache de website limpos com sucesso!")
