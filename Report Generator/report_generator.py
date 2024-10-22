import PySimpleGUI as sg
import mysql.connector
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

sg.theme('SandyBeach')
layout = [
    [sg.Text('Please enter SQL')],
    [sg.Multiline(size=(50,5),key= 'textbox')],
    [sg.Submit(),sg.Cancel()]
]
window = sg.Window('Report Generator', layout)
event, values = window.read()
query =values['textbox']

conn = mysql.connector.connect(
        host=os.environ.get("SQL_HOST"),
        user=os.environ.get("SQL_USER"),
        port=int(os.environ.get("SQL_PORT")),
        password=os.environ.get("SQL_PASSWORD"),
        database=os.environ.get("SQL_DATABASE")
        )

df = pd.read_sql(query,conn)
df.to_excel('report.xlsx', index =False)
os.startfile('report.xlsx')