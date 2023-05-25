"""This python file sets up a secured connection
    to the script"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import df2gspread as d2g
from gspread_dataframe import set_with_dataframe
import os
import pandas as pd

#import environment variable
key_file = os.getenv('GCP_KEY')

# defining the scope of the application
scope_app = ['https://www.googleapis.com/auth/drive',
             'https://spreadsheets.google.com/feeds']


def get_connect_sheet():

    cred = ServiceAccountCredentials.from_json_keyfile_name(
        key_file, scope_app)

    client = gspread.authorize(cred)

    return client

def push_to_sheets(sheet: str, df):
    '''This function takes in the sheet and the
    dataframe'''
    sheet.clear()
    set_with_dataframe(worksheet=sheet, dataframe=df, include_index=False,
                       include_column_header=True, resize=True)


def append_new_data(df, sheet_name: str, sheet: str):
    """This function takes in the dataframe and the name of the sheet you wish
    to append the data to """

    values = df
    push_sheet = get_connect_sheet().open(sheet)
    push_sheet.values_append(sheet_name, {'valueInputOption': 'USER_ENTERED'},
                             {'values': values})

def get_dataframe(sheet: str, sheet_name: str):
    """This function is used to import the file as a dataframe object"""

    client = get_connect_sheet().open(sheet)

    data = pd.DataFrame.from_dict(
        client.worksheet(sheet_name).get_all_records())

    return data


if __name__ == '__main__':
    client = get_connect_sheet()
    sheet = client.open('test_sheet')
    print(sheet.worksheets())
    data = get_dataframe('test_sheet', 'trans')
    print(data.head(5))