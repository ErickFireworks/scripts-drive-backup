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

  folder_main_id = handle_folder.getIdFolderMain()

  print("\nBienvenido al sistema de respaldos.\n")

  choice = ''

  while choice != 'q':

    print("\n[1] Respaldar sitio.")
    print("[2] Respaldar Base de Datos.")
    print("[3] Subir respaldo a drive.")
    print("[q] Enter q to quit.\n")

    choice = input("\n¿Que te gustaría realizar?\n")

    #TODO: Generate tracking every task is complete with a log in screen

    if choice == "1":
      path_file_zip = website_backup.createWebsiteBackup()
      file_paths.append(path_file_zip)

    elif choice == "2":
      path_file_sql = database_backup.createDatabaseBackup()
      file_paths.append(path_file_sql)

    elif choice == "3":
      folder_id_current = handle_folder.create_folder(folder_main_id)
      handle_upload.uploadFile( file_paths, folder_id_current)

    elif choice == "q":
      print("\nGracias por usar el sistema de respaldos.\n")
      break
    else:
      print("\nNo entiendo la elección, por favor intenta de nuevo!!!.\n")
    
    file_paths = []
    #Delete File Temps
