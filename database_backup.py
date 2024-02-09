import os


class DatabaseBackup:

    def __init__(self, today_date, site, database):
        self.today = today_date
        self.database = database
        self.site = site

    def createDatabaseBackup(self):
        print("\nCreate backup data base ...\n")

        cmd = f"mysqldump -u root -p namedatabase > backup-{self.today}-{self.database}.sql && mv backup-{self.today}-{self.database}.sql ./{self.site}/backup-{self.today}"
        os.system(cmd)

        print("\nFinish backup data base ...\n")

        return {
            "name": f"backup-{self.today}-{self.database}.sql",
            "path": os.path.abspath(
                f"./{self.site}/backup-{self.today}/backup-{self.today}-{self.database}.sql"
            ),
        }
