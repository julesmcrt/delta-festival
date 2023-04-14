from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



def moveFile(creds, file_id, folder_id):
    """Move specified file to the specified folder.
    Args:
        file_id: Id of the file to move.
        folder_id: Id of the folder
    Print: An object containing the new parent folder and other meta data
    Returns : Parent Ids for the file
    """

    try:
        # call drive api client
        service = build('drive', 'v3', credentials=creds)

        # pylint: disable=maybe-no-member
        # Retrieve the existing parents to remove
        file = service.files().get(fileId=file_id, fields='parents').execute()
        previous_parents = ",".join(file.get('parents'))
        # Move the file to the new folder
        file = service.files().update(fileId=file_id, addParents=folder_id,
                                      removeParents=previous_parents,
                                      fields='id, parents').execute()
        return file.get('parents')

    except HttpError as error:
        print(F'An error occurred: {error}')
        return None