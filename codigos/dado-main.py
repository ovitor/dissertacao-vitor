def onClick(self, controlID):
    if not (controlID in [7011, 7012]):
        if not (SINTOMS[controlID] in self.selectedSintoms):
            self.selectedSintoms.append(SINTOMS[controlID])
    # (...)
    if controlID == 7016:
        if len(self.selectedSintoms) != 0:
            self.server.requestSession()
            self.server.requestPatient(self.selectedSintoms)
            self.diseases = self.server.parseRequestPatient()
	    header = 'Conclusão'
	    message = 'Possíveis doenças são: {0}. Procure seu médico.'
                .format(', '.join(self.diseases))
	    xbmcgui.Dialog().ok(header, message)
    # (...)
