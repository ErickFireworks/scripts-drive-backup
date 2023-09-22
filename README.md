# scripts-drive-backup

Before using this tool you must have python version 3 installed and the following dependencies:

```
sudo apt update
sudo apt install python3-pip
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

Generate files:

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
