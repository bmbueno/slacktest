import os.path
import pickle
from pprint import pprint
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from googleapiclient import discovery

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None

if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'creds.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)


service = discovery.build('sheets', 'v4', credentials=creds)

# The ID of the spreadsheet to update.
spreadsheet_id = '1gkE5fP7rFDB68kiLJxQNDq0FvChnsmhSdpGFr3IlYUk' 

# The A1 notation of the values to update.
range_ = 'Pag1!B9'  

# How the input data should be interpreted.
value_input_option = 'RAW'  

value_range_body = {
    {
  "range": "Pag1!B8", "majorDimension": "ROWS",
  "values": [
    [
      12
    ]
    
  ]
    }
}

request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, body=value_range_body)
response = request.execute()

# TODO: Change code below to process the `response` dict:
pprint(response)