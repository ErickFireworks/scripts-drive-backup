import os
from datetime import date

class WebsiteBackup:
  def createWebsiteBackup(self):
    today = date.today()

    cmd = f'zip -0 -r backup-{today}.zip /home/erick_93/aprovisionamiento'
    os.system(cmd)