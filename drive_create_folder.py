from __future__ import print_function

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os.path
import json

class DriveHandlerActions:
  def create_folder(self, creds):
    """ Create a folder and prints the folder ID
    Returns : Folder Id

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """

    try:
      # create drive api client
      service = build('drive', 'v3', credentials=creds)
      file_metadata = {
          'name': 'BackupFireworksStudio',
          'mimeType': 'application/vnd.google-apps.folder'
      }

      # pylint: disable=maybe-no-member
      file = service.files().create(body=file_metadata, fields='id'
                                    ).execute()
      # print(F'Folder ID: "{file.get("id")}".')

      folder = {
        "id" : file.get('id')
      }

      json_object = json.dumps(folder, indent=2)

      with open('id_folder_main.json', 'w') as outfile:
          outfile.write(json_object)

      return file.get('id')

    except HttpError as error:
      print(F'An error occurred: {error}')
      return None
    
  def getIdFolderMain(self):
    if os.path.exists('id_folder_main.json'):
      
      with open('id_folder_main.json', 'r') as openfile:
        json_object = json.load(openfile)
        return json_object['id']