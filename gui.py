import licence_pysimle_gui
import PySimpleGUI as sg


form_rows = [
    [sg.Text('Find company data')],
    [sg.Text('Add company CUI', size=(15, 1)),sg.Input(key='-CUI-',do_not_clear=False)],
    [sg.Text('Select contract draft', size=(15, 1)), sg.InputText(key='-DRAFT-'),sg.FileBrowse(target='-DRAFT-')],
    [sg.Text('Contract start date', size=(15, 1)), sg.Input(key='-START_DATE-', size=(15, 1)), 
     sg.CalendarButton('Start date',close_when_date_chosen=True, target='-START_DATE-', location= (0,0), no_titlebar=False)],
    [sg.Text('Contract end date', size=(15, 1)), sg.Input(key='-END_DATE-', size=(15, 1)), 
     sg.CalendarButton('End date',close_when_date_chosen=True, target='-END_DATE-', location= (0,0), no_titlebar=False)],
    [sg.Submit('SUBMIT'), sg.Cancel()]
    ]

window = sg.Window('Company data extractor', form_rows)

while True:
    event, values = window.read()       
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'SUBMIT':
        print ('yes')
window.close()

