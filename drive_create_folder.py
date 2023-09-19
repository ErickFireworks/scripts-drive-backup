from __future__ import print_function
from googleapiclient.errors import HttpError
from datetime import date
import os.path
import json
import os

class ActionsFolderFromGoogleDrive:

  def __init__(self):
    today = date.today()

    path = f'./backup-{today}'
    isExist = os.path.exists(path)

    if isExist is False:
      os.system(F"mkdir backup-{today}")
    else: 
      print( "Folder Exist" )


  def create_folder(self, service):
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

      file = service.files().create(body=file_metadata, fields="id").execute()

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
