from __future__ import print_function
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

class GoogleDriveUploadFiles:

  def __init__(self, service):
    self.service = service

  def uploadFile(self, folder_id):

    try:
      results = (
        self.service.files()
        .list(
          q="name = 'BackupFireworksStudio'",
          fields="nextPageToken, files(id, name)",
        )
        .execute()
      )

      items = results.get("files", [])

      if not items:
        print("No files found.")
        return

      for item in items:
        if item["id"] == folder_id:
          print(item)
        else:
          print("does not exist")
          # Create Error in case does not exist folder
          return

      file_metadata = {
        "name": "id_folder_main.json", 
        "parents": [folder_id]
      }
      media = MediaFileUpload("id_folder_main.json", resumable=True)

      file = (
        self.service.files()
        .create(body=file_metadata, media_body=media, fields="id")
        .execute()
      )
      print(f'File ID: "{file.get("id")}".')
      return file.get("id")

    except HttpError as error:
      print(f"An error occurred: {error}")
      return None
