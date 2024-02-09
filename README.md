# scripts drive backup

Before using this tool you must have python version 3 installed and the following dependencies:

```
sudo apt update
sudo apt install python3-pip
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install python-dotenv
```

### Configure and run an app that calls a Google Workspace API.

To run our backup script we must first generate authentication and authorization keys, the following documentation explains step by step how to create them.

[Python Quick Start Guide.](https://developers.google.com/drive/api/quickstart/python?hl=es-419)

At the end of the guide you should have a file with json extension that will contain the keys we need to send requests to the Google Drive API.

Generated files:

```
credentials.json
```

Attach this file to the root of your project.

### Authorization and Testing

Execute the following command:

```
python3 testing.py
```

Run the following command to authorize that you will use the google drive API and which account will have access to the files.

After granting the authorization a json file called:

```
token.json
```

will be generated. This file has the keys to authorize the requests that we are going to make from the script to the drive account that we chose in the previous step.

Finally if everything went well, the script will list all the folders that contain our drive account in the terminal.

## Execute backups

```
- token.json
- id_folder_main.json
```

Change the directory path of the folder to be packed in the website_backup.py file.

Rename database, users in database_backup.py file.

Use the following command to generate the backup

```
python3 main.py
```
