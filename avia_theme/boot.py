# Copyright (c) 2026 Grupo Belchior
# License: MIT. See license.txt

import frappe

def boot_session(bootinfo):
	"""
	Sobrescreve informacoes de exibicao dos apps no Boot do Frappe
	para que o ERPNext apareca oficialmente como AVIA, com logo e titulo corretos
	tanto na tela de Apps (/app ou /desk) quanto no Dock lateral flutuante.
	"""
	# Frappe v16: apps_data e um dicionario contendo a chave 'apps'
	if "apps_data" in bootinfo and isinstance(bootinfo["apps_data"], dict):
		apps_list = bootinfo["apps_data"].get("apps", [])
		for app in apps_list:
			if app.get("name") in ["erpnext", "frappe"]:
				app["title"] = "AVIA"
				app["logo"] = "/assets/avia_theme/images/avia_app_icon.png"

	# Compatibilidade com versoes anteriores onde a chave era app_data (lista)
	if "app_data" in bootinfo and isinstance(bootinfo["app_data"], list):
		for app in bootinfo["app_data"]:
			if app.get("app_name") in ["erpnext", "frappe"]:
				app["app_title"] = "AVIA"
				app["app_logo_url"] = "/assets/avia_theme/images/avia_app_icon.png"

	# Forca tema escuro (Dark Mode) globalmente para a sessao do Desk
	bootinfo["desk_theme"] = "Dark"
	bootinfo["onboarding_disabled"] = 1
	if "user" in bootinfo and isinstance(bootinfo["user"], dict):
		bootinfo["user"]["onboarding_status"] = "{}"
		bootinfo["user"]["desk_theme"] = "Dark"
