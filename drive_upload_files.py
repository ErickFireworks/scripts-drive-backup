from __future__ import print_function

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

class Upload:

  def setBackup(self, creds ,folder_id):
    try:
      # create drive api client
      service = build('drive', 'v3', credentials=creds)

      results = service.files().list(
        q = "name = 'BackupFireworksStudio'",
        fields="nextPageToken, files(id, name)").execute()
      
      items = results.get('files', [])

      # print( items )
      if not items:
        print('No files found.')
        return
      
      for item in items:
        if item['id'] == folder_id:
          print(item)
        else:
          print("does not exist")
          # Create Error in case does not exist folder
          return
      
      file_metadata = {
          'name': 'id_folder_main.json',
          'parents': [folder_id]
      }
      media = MediaFileUpload(
        'id_folder_main.json',
        resumable=True)
      # pylint: disable=maybe-no-member
      file = service.files().create(body=file_metadata, media_body=media,
                                    fields='id').execute()
      print(F'File ID: "{file.get("id")}".')
      return file.get('id')

    except HttpError as error:
      print(F'An error occurred: {error}')
      return None
