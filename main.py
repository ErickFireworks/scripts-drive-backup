from drive_outh import TokenOuthGoogleDrive
from drive_create_folder import ActionsFolderFromGoogleDrive
from drive_upload_files import GoogleDriveUploadFiles

from website_backup import WebsiteBackup
from database_backup import DatabaseBackup
from datetime import date

import json

if __name__ == "__main__":
  today = date.today()
  file_paths = []

  # Instance
  token_drive = TokenOuthGoogleDrive()
  service = token_drive.getCredentialFromDrive()

  website_backup = WebsiteBackup(today)
  database_backup = DatabaseBackup(today)

  handle_folder = ActionsFolderFromGoogleDrive(service, today)
  handle_upload = GoogleDriveUploadFiles(service)

  folder_main_id = handle_folder.getIdFolderMain()

  print("\nWelcome to the backup system.\n")

  choice = ''

  while choice != 'q':

    print("\n[1] Backup WebSite.")
    print("[2] Backup Database.")
    print("[3] Upload Backup to Google drive.")
    print("[q] Enter q to quit.\n")

    choice = input("\nWhat would you like to do?\n")

    if choice == "1":
      path_file_zip = website_backup.createWebsiteBackup()
      file_paths.append(path_file_zip)
      with open(f"./backup-{today}/list_files.json", "w") as token:
        token.write(json.dumps(file_paths))

    elif choice == "2":
      path_file_sql = database_backup.createDatabaseBackup()
      file_paths.append(path_file_sql)
      with open(f"./backup-{today}/list_files.json", "w") as token:
        token.write(json.dumps(file_paths)) 

    elif choice == "3":
      # list_files = list(open(f"./backup-{today}/list_files.json", "r"))
      list_files = file_paths
      folder_id_current = handle_folder.create_folder(folder_main_id)
      handle_upload.uploadFile( list_files, folder_id_current)
      handle_folder.deleteFolderTempFiles()

    elif choice == "q":
      print("\nThank you for using the backup system.\n")
      file_paths = []
      break
    
    else:
      print("\nI don't understand the choice, please try again.!!!.\n")
