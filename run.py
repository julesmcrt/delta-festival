import gauth, gdrive

# Step 1. Connects to Google Drive's API
print('Connecting to Google Workspace\'s API...', end='\r')
credentials = gauth.getCredentials('credentials/token.json', 'credentials/credentials.json')
print('Connecting to Google Workspace\'s API... Done')

# Step 2. Move file to new folder
file = ""
folder = ""
parent_ids = gdrive.moveFile(credentials, file, folder)
print(parent_ids)