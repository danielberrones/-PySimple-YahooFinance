import PySimpleGUI as sg
import yfinance as yf

layout = [
        [sg.Text('Enter Ticker Symbol')],
        [sg.InputText()],               
        [sg.Submit(), sg.Cancel()]
        ]

window = sg.Window('Closing Stock Price', layout)

event, values = window.read()    
window.close()

text_input = values[0]    
userTicker = yf.Ticker(text_input)
close = userTicker.history()['Close'][0]

sg.popup(f'{text_input} close: ', round(close,2))
