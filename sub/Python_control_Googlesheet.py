import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import urllib.request

#set GoogleSheet_API(Power)
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

#set GoogleSheet_API(air)
api_path = os.path.abspath("./api/airAPI.json")
print('API_path: ', api_path)

credentials = ServiceAccountCredentials.from_json_keyfile_name(api_path, scope)
gc = gspread.authorize(credentials)
sheet = gc.open("jiayou").sheet1

def read_sheet(row, column):
    '''
        read_sheet(row, column)
        (5, 8) is data_count
    '''
    data = sheet.cell(row, column).value
    return data

def upload_sheet(row, values):
    '''
        upload_sheet(row, values)
        values: ['time', 'lat', 'lon', 'pm25', 'h', 't']
    '''
    for i in range(4):
        sheet.update_cell(row, i+1, values[i])
    for j in range(2):
        sheet.update_cell(row, j+6, values[j+4])

    sheet.update_cell(5, 8, int(row)+1)

if __name__=='__main__':
    data_count = read_sheet(5, 8)
    print('data_count: ', data_count)
    upload_data = ['time', 'lat', 'lon', 'pm25', 'h', 't']
    upload_sheet(int(data_count), upload_data)
    print('Okay')