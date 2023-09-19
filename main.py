from drive_outh import TokenOuthGoogleDrive
from drive_create_folder import ActionsFolderFromGoogleDrive
from drive_upload_files import GoogleDriveUploadFiles
from website_backup import WebsiteBackup
from database_backup import DatabaseBackup

if __name__ == "__main__":
  # Instance
  token_drive = TokenOuthGoogleDrive()
  handle_folder = ActionsFolderFromGoogleDrive()
  handle_upload = GoogleDriveUploadFiles()

  service = token_drive.getCredentialFromDrive()

  print("\nBienvenido al sistema de respaldos.\n")

  choice = ''

  while choice != 'q':

    print("\n[1] Respaldar sitio.")
    print("[2] Respaldar Base de Datos.")
    print("[3] Subir respaldo a drive.")
    print("[q] Enter q to quit.\n")

    choice = input("\n¿Que te gustaría realizar?\n")

    if choice == "1":
      website_backup = WebsiteBackup()
      website_backup.createWebsiteBackup()
    elif choice == "2":
      database_backup = DatabaseBackup()
      database_backup.createDatabaseBackup()
    # elif choice == "3":
      
    elif choice == "q":
      print("\nGracias por usar el sistema de respaldos.\n")
      break
    else:
      print("\nNo entiendo la elección, por favor intenta de nuevo!!!.\n")

# name = input('What is your name?\n')
# print( name )

# token_drive.getListDocumentsFromDrive()
# handle_folder.create_folder(service)
# folder_id = handle_folder.getIdFolderMain()
# handle_upload.uploadFile(service, folder_id)
