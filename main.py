from drive_outh import TokenOuthGoogleDrive
from drive_create_folder import ActionsFolderFromGoogleDrive
from drive_upload_files import GoogleDriveUploadFiles

from website_backup import WebsiteBackup
from database_backup import DatabaseBackup
from datetime import date

if __name__ == "__main__":
  today = date.today()
  # Instance
  token_drive = TokenOuthGoogleDrive()
  handle_folder = ActionsFolderFromGoogleDrive(today)
  handle_upload = GoogleDriveUploadFiles()

  service = token_drive.getCredentialFromDrive()
  folder_main_id = handle_folder.getIdFolderMain()

  print("\nBienvenido al sistema de respaldos.\n")

  choice = ''

  while choice != 'q':

    print("\n[1] Respaldar sitio.")
    print("[2] Respaldar Base de Datos.")
    print("[3] Subir respaldo a drive.")
    print("[q] Enter q to quit.\n")

    choice = input("\n¿Que te gustaría realizar?\n")

    if choice == "1":
      website_backup = WebsiteBackup(today)
      website_backup.createWebsiteBackup()
    elif choice == "2":
      database_backup = DatabaseBackup(today)
      database_backup.createDatabaseBackup()
    elif choice == "3":
      handle_folder.create_folder(service, folder_main_id)
      # handle_upload.uploadFile(service, folder_id)
    elif choice == "q":
      print("\nGracias por usar el sistema de respaldos.\n")
      break
    else:
      print("\nNo entiendo la elección, por favor intenta de nuevo!!!.\n")

# token_drive.getListDocumentsFromDrive()
# handle_folder.create_folder(service)
