from __future__ import print_function
from googleapiclient.errors import HttpError
import os.path
import json
import os

class ActionsFolderFromGoogleDrive:

  def __init__(self, service ,today_date):
    self.today = today_date
    self.service = service

    path = f'./backup-{self.today}'
    isExist = os.path.exists(path)

    if isExist is False:
      os.system(F"mkdir backup-{self.today} && touch list_files.json && mv list_files.json backup-{self.today}")


  def create_folder(self, folder_main_id):
    try:

      file_metadata = {
        "name": f"backup-{self.today}",
        "mimeType": "application/vnd.google-apps.folder",
        "parents": [folder_main_id]
      }

      file = self.service.files().create(body=file_metadata, fields="id").execute()

      return file.get("id")

    except HttpError as error:
      print(f"An error occurred: {error}")
      return None

  def create_folder_main(self):
    """Create a folder and prints the folder ID
    Returns : Folder Id

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """

    try:
      # create drive api client
      file_metadata = {
        "name": "BackupFireworksStudio",
        "mimeType": "application/vnd.google-apps.folder",
      }

      file = self.service.files().create(body=file_metadata, fields="id").execute()

      folder = {"id": file.get("id")}

      json_object = json.dumps(folder, indent=2)

      with open("id_folder_main.json", "w") as outfile:
        outfile.write(json_object)

      return file.get("id")

    except HttpError as error:
      print(f"An error occurred: {error}")
      return None

  def getIdFolderMain(self):
    if os.path.exists("id_folder_main.json"):
      with open("id_folder_main.json", "r") as openfile:
        json_object = json.load(openfile)
        return json_object["id"]
      
  def deleteFolderTempFiles(self):
    os.system(F"rm -rf backup-{self.today}")

  def deleteFolderDrive(self, folder_id):
    self.service.files().delete(fileId=folder_id).execute()
    print('Delete folder drive')

