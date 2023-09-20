from drive_outh import TokenOuthGoogleDrive
from drive_create_folder import ActionsFolderFromGoogleDrive
from drive_upload_files import GoogleDriveUploadFiles

from website_backup import WebsiteBackup
from database_backup import DatabaseBackup
from datetime import date

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

  #Get the folder that will have all the backups
  folder_main_id = handle_folder.getIdFolderMain()

  print("\nInitiating site backup.\n")

  #Create packing zip website
  path_file_zip = website_backup.createWebsiteBackup()
  file_paths.append(path_file_zip)

  #Create file SQL 
  path_file_sql = database_backup.createDatabaseBackup()
  file_paths.append(path_file_sql)

  #Creates the folder where backups are set up and upload files to drive
  folder_id_current = handle_folder.create_folder(folder_main_id)
  handle_upload.uploadFile( file_paths, folder_id_current)
  handle_folder.deleteFolderTempFiles()

  print("\nComplete backup.\n")
  file_paths = []
