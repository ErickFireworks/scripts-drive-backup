from drive_outh import Google
from drive_create_folder import DriveHandlerActions
from drive_upload_files import Upload

if __name__ == '__main__':
  #Instance
  myDrive = Google()
  handle = DriveHandlerActions()
  upload_files = Upload()

  creds = myDrive.getCredentialFromDrive()
  #handle.create_folder(creds)
  folder_id = handle.getIdFolderMain()
  upload_files.setBackup( creds,folder_id )