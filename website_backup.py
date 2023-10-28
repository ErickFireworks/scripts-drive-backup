import os

class WebsiteBackup:
  def __init__(self, today_date):
    self.today = today_date

  def createWebsiteBackup(self):
    print('\nCreate backup website ...\n')

    cmd = f'zip -0 -r backup-{self.today}.zip ./testing_files && mv backup-{self.today}.zip ./backup-{self.today}'
    os.system(cmd)

    print('\nFinish backup website ...\n')

    return {
      "name": f"backup-{self.today}.zip",
      "path": os.path.abspath(f"./backup-{self.today}/backup-{self.today}.zip") 
    }