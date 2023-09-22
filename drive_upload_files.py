from __future__ import print_function
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

class GoogleDriveUploadFiles:

  def __init__(self, service):
    self.service = service

  def uploadFile(self, files_path, folder_id_current):
    
    try:

      for file in files_path:
        print('upload file ...')
        self.handleUploadDrive(file, folder_id_current)

    except HttpError as error:
      print(f"An error occurred: {error}")
      return None
  
  def handleUploadDrive(self, file_name ,folder_id_current):
    file_metadata = {
      "name": file_name["name"], 
      "parents": [folder_id_current]
    }
    media = MediaFileUpload(file_name["path"], resumable=True)

    file = (
      self.service.files()
      .create(body=file_metadata, media_body=media, fields="id")
      .execute()
    )
    print(f'File ID: "{file.get("id")}".')