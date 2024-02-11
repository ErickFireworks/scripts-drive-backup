import json
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

    print("\nInitiating site backup!!!.\n")

    # Create packing zip website
    path_file_zip = website_backup.createWebsiteBackup()
    file_paths.append(path_file_zip)
    addRoutePath(list_files, file_paths)

    # Create file SQL
    path_file_sql = database_backup.createDatabaseBackup()
    file_paths.append(path_file_sql)
    addRoutePath(list_files, file_paths)

    # Creates the folder where backups are set up and upload files to drive
    files_uploads = getRoutePath(list_files)
    handle_upload.uploadFile(files_uploads, folder_main_id, handle_folder)
    handle_folder.deleteFolderTempFiles()

    print("\nComplete backup!!!.\n")
    file_paths = []
