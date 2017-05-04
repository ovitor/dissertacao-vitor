def onClick(self, controlID):
    # (...)
    if controlID == 7020:
        contacts = self.server.getContacts()
        self.server.sendSMS(contacts)
        header = 'Conclusão'
        msg = "Você ativou o botão de pânico. "
        msg = msg + "Os contatos cadastrados estão sendo notificados. " 
        msg = msg + "Aguarde e mantenha a calma"
	xbmcgui.Dialog().ok(header, msg)
    # (...)

