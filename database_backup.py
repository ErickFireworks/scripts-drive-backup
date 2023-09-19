import os
from datetime import date

class DatabaseBackup:
  def createDatabaseBackup():
    today = date.today()

    cmd = f'mysqldump -u root -p namedatabase >backup-{today}-.sql'
    os.system(cmd)