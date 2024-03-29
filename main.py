from datetime import date

from drive_outh import TokenOuthGoogleDrive
from drive_create_folder import ActionsFolderFromGoogleDrive
from drive_upload_files import GoogleDriveUploadFiles

from website_backup import WebsiteBackup
from database_backup import DatabaseBackup
from dotenv import dotenv_values
from services import *


if __name__ == "__main__":
    config = dotenv_values(".env")
    site = config["SITE"]
    database = config["DATABASE"]
    backup_path = config["BACKUP_FILES"]
    db_password = config["DB_PASSWORD"]
    today = date.today()
    list_files = f"./{site}/backup-{today}/list_files.json"
    file_paths = []

    # Instance
    token_drive = TokenOuthGoogleDrive()
    service = token_drive.getCredentialFromDrive()

    website_backup = WebsiteBackup(today, site, backup_path)
    database_backup = DatabaseBackup(today, site, database, db_password)

    handle_folder = ActionsFolderFromGoogleDrive(service, today, site)
    handle_upload = GoogleDriveUploadFiles(service)

    folder_main_id = handle_folder.getIdFolderMain()

    print("\nWelcome to the backup system.\n")

    choice = ""

    while choice != "q":

        print("\n[1] Backup WebSite.")
        print("[2] Backup Database.")
        print("[3] Upload Backup to Google drive.")
        print("[q] Enter q to quit.\n")

        choice = input("\nWhat would you like to do?\n")

        if choice == "1":
            path_file_zip = website_backup.createWebsiteBackup()
            file_paths.append(path_file_zip)
            addRoutePath(list_files, file_paths)

        elif choice == "2":
            path_file_sql = database_backup.createDatabaseBackup()
            file_paths.append(path_file_sql)
            addRoutePath(list_files, file_paths)

        elif choice == "3":
            files_uploads = getRoutePath(list_files)
            handle_upload.uploadFile(files_uploads, folder_main_id, handle_folder)
            handle_folder.deleteFolderTempFiles()

        elif choice == "q":
            print("\nThank you for using the backup system.\n")
            file_paths = []
            break

        else:
            print("\nI don't understand the choice, please try again.!!!.\n")
