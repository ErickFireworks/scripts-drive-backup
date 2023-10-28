from __future__ import print_function
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import os.path

SCOPES = [
  "https://www.googleapis.com/auth/drive",
  "https://www.googleapis.com/auth/drive.file",
  "https://www.googleapis.com/auth/drive.appdata",
]


class TokenOuthGoogleDrive:
  def getCredentialFromDrive(self):
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
      else:
        flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
          token.write(creds.to_json())

    service = build("drive", "v3", credentials=creds)

    return service

  def getListDocumentsFromDrive(self):
    service = self.getCredentialFromDrive()

    try:
      results = (
        service.files()
        .list(pageSize=10, fields="nextPageToken, files(id, name)")
        .execute()
      )
      items = results.get("files", [])

      if not items:
        print("No files found.")
        return
      
      print("Files:")
      for item in items:
        print("{0} ({1})".format(item["name"], item["id"]))

    except HttpError as error:
      print(f"An error occurred: {error}")

  def searchDocumentsFromDrive(self):
    service = self.getCredentialFromDrive()

    # Search all drive (no access shared drive folder)
    # results = service.files().list().execute()

    # Search all folders (no access shared drive folder)
    # results = service.files().list(q="mimeType='application/vnd.google-apps.folder'").execute()

    # search for all folders containing the word 'Carpeta' (Access shared drive folder)
    # results = service.files().list(
    #      q="fullText contains 'carpeta' and mimeType = 'application/vnd.google-apps.folder'",
    #      includeItemsFromAllDrives=True, 
    #      supportsAllDrives=True, 
    #      fields="nextPageToken, files(id, name)").execute()

    # search for all (Access shared drive folder)
    results = service.files().list(
         includeItemsFromAllDrives=True, 
         supportsAllDrives=True, 
         fields="nextPageToken, files(id, name)").execute()
    items = results.get("files", [])
    for item in items:
        print("{0} ({1})".format(item["name"], item["id"]))
