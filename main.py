from drive_outh import TokenOuthGoogleDrive
from drive_create_folder import ActionsFolderFromGoogleDrive
from drive_upload_files import GoogleDriveUploadFiles

if __name__ == "__main__":
  # Instance
  token_drive = TokenOuthGoogleDrive()
  handle_folder = ActionsFolderFromGoogleDrive()
  handle_upload = GoogleDriveUploadFiles()

  service = token_drive.getCredentialFromDrive()
# token_drive.getListDocumentsFromDrive()
# handle_folder.create_folder(service)
# folder_id = handle_folder.getIdFolderMain()
# handle_upload.uploadFile(service, folder_id)
