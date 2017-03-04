def showNotificationOk(self, id, header, message):
    try:
      header = header.encode('utf-8')
      message = message.encode('utf-8')
      if XBMC_ENABLE == True:
        xbmcgui.Dialog().ok(header, message)
    except Exception, e:
      logging.error("Erro -> notificacao OK ID: %s : %s" % (id, e))

def showNotificationPopup(self, id, header, message):
  try:
    header = header.encode('utf-8')
    message = message.encode('utf-8')
    if XBMC_ENABLE == True:
      message_content = 'Notification("{0}", "{1}")'.format(header, message)
      xbmc.executebuiltin(message_content)
  except Exception, e:
    logging.error("Erro -> notificacao POPUP ID: %s : %s" % (id, e))