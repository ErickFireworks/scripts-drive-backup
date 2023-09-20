import os

class DatabaseBackup:

  def __init__(self, today_date):
    self.today = today_date

  def createDatabaseBackup(self):
    # cmd = f'mysqldump -u root -p namedatabase >backup-{self.today}.sql && mv backup-{self.today}.sql ./backup-{self.today}'
    print('\nLoading ...\n')
    cmd = f'cp db_test.sql ./backup-{self.today}/backup-{self.today}.sql'
    os.system(cmd)
    print('\nFinish ...\n')
    return os.path.abspath(f"./backup-{self.today}/backup-{self.today}.sql")
