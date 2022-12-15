import PySimpleGUI as sg

layout = [
    [sg.Text('Hello from PySimpleGUI')],
    [sg.Button('OK')]
]

# create the window
window = sg.Window('Demo', layout)

#create an event loop
while True:
    event, values = window.read()
    #end program if user closes window or press OK
    if event == 'OK' or event == sg.WIN_CLOSED:
        break

window.close()

# sg.Window(title='Hello World', layout = [[]], margins=(100,50)).read()