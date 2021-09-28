import PySimpleGUI as sg
import pyautogui
'''sg.theme('DarkAmber')   # Add a little color to your windows
# All the stuff inside your window. This is the PSG magic code compactor...
layout = [  [sg.Text('Menu de opções!')],
            [sg.Text('Digite o que voce deseja abrir:'), sg.InputText()],
            [sg.OK(), sg.Cancel()]]

# Create the Window
window = sg.Window('Lipe GS', layout)
# Event Loop to process "events"
while True:             
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        pyautogui.click(x=56, y=745)
    if event (sg.WIN_X_EVENT, 'OK'):
        pyautogui.click(x=56, y=745)
window.close()'''





sg.theme('Dark Blue 3')  # please make your creations colorful

layout = [  [sg.Text('Filename')],
            [sg.Input(), sg.FileBrowse()], 
            [sg.OK(), sg.Cancel()]] 

window = sg.Window('Get filename example', layout)

event, values = window.read()
window.close()

