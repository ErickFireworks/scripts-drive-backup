import os

class WebsiteBackup:
  def __init__(self, today_date):
    self.today = today_date

  def createWebsiteBackup(self):
    cmd = f'zip -0 -r backup-{self.today}.zip /home/erick_93/aprovisionamiento && mv backup-{self.today}.zip ./backup-{self.today}'
    os.system(cmd)