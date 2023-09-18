from __future__ import print_function

import os.path

import google.auth
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

def create_folder():
    """ Create a folder and prints the folder ID
    Returns : Folder Id

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    
    """ creds, _ = google.auth.default() """

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)
        file_metadata = {
            'name': 'Backups Test',
            'mimeType': 'application/vnd.google-apps.folder'
        }

        # pylint: disable=maybe-no-member
        file = service.files().create(body=file_metadata, fields='id'
                                      ).execute()
        # print(F'Folder ID: "{file.get("id")}".')
        return file.get('id')

    except HttpError as error:
        print(F'An error occurred: {error}')
        return None


if __name__ == '__main__':
    create_folder()