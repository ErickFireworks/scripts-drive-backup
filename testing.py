from drive_outh import TokenOuthGoogleDrive
import sys

token_drive = TokenOuthGoogleDrive()

token_drive.searchDocumentsFromDrive()

# if sys.version_info[0] != 3:
#   print('Install')
# else:
#   print('no install')
