import os

class DatabaseBackup:

  def __init__(self, today_date):
    self.today = today_date

  def createDatabaseBackup(self):
    cmd = f'mysqldump -u root -p namedatabase >backup-{self.today}-.sql'
    os.system(cmd)