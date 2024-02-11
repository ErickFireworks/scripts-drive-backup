import os


class WebsiteBackup:
    def __init__(self, today_date, site, backup_path):
        self.today = today_date
        self.site = site
        self.backup_path = backup_path

    def createWebsiteBackup(self):
        print("\nCreate backup website ...\n")

        cmd = f"zip -0 -r backup-{self.today}-{self.site}.zip {self.backup_path } && mv backup-{self.today}-{self.site}.zip ./{self.site}/backup-{self.today}/"
        os.system(cmd)

        print("\nFinish backup website ...\n")

        return {
            "name": f"backup-{self.today}-{self.site}.zip",
            "path": os.path.abspath(
                f"./{self.site}/backup-{self.today}/backup-{self.today}-{self.site}.zip"
            ),
        }
