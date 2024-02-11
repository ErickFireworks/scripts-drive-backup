from drive_outh import TokenOuthGoogleDrive
from drive_create_folder import ActionsFolderFromGoogleDrive
from drive_upload_files import GoogleDriveUploadFiles

from website_backup import WebsiteBackup
from database_backup import DatabaseBackup
from datetime import date
from dotenv import dotenv_values

import json

if __name__ == "__main__":

    config = dotenv_values(".env")
    site = config["SITE"]
    database = config["DATABASE"]
    backup_path = config["BACKUP_FILES"]
    db_password = config["DB_PASSWORD"]
    today = date.today()
    file_paths = []

    # Instance
    token_drive = TokenOuthGoogleDrive()
    service = token_drive.getCredentialFromDrive()

    website_backup = WebsiteBackup(today, site, backup_path)
    database_backup = DatabaseBackup(today, site, database, db_password)

    handle_folder = ActionsFolderFromGoogleDrive(service, today)
    handle_upload = GoogleDriveUploadFiles(service)

    # Get the folder that will have all the backups
    folder_main_id = handle_folder.getIdFolderMain()

    # print("\nInitiating site backup!!!.\n")

    # # Create packing zip website
    # path_file_zip = website_backup.createWebsiteBackup()
    # file_paths.append(path_file_zip)
    # with open(f"./backup-{today}/list_files.json", "w") as file:
    #     file.write(json.dumps(file_paths))

    # # Create file SQL
    # path_file_sql = database_backup.createDatabaseBackup()
    # file_paths.append(path_file_sql)
    # with open(f"./backup-{today}/list_files.json", "w") as file:
    #     file.write(json.dumps(file_paths))

    # # Creates the folder where backups are set up and upload files to drive
    # list_files = list(open(f"./backup-{today}/list_files.json", "r"))
    # folder_id_current = handle_folder.create_folder(folder_main_id)
    # handle_upload.uploadFile(list_files, folder_id_current)
    # handle_folder.deleteFolderTempFiles()

    # print("\nComplete backup!!!.\n")
    # file_paths = []
