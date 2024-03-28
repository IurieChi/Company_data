import licence_pysimle_gui
import PySimpleGUI as sg


form_rows = [
    [sg.Text('Contract filer')],
    [sg.Text('Add company CUI', size=(15, 1)),sg.Input(key='cui',do_not_clear=False)],
    [sg.Text('Select contract draft', size=(15, 1)), sg.InputText(key='draft'),sg.FileBrowse(target='draft')],
    [sg.Submit(), sg.Cancel()]
    ]

window = sg.Window('Contract ', form_rows)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
window.close()

