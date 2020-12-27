import PySimpleGUI as sg    

def numerical_calculator():
    # Code originally adapted from https://gist.github.com/ball13411/39014c86945ac40bbd7c39677b560991

    # Layout                                                         # Creat GUI
    layout = [[sg.Txt(''  * 10)],                      
            [sg.Text('', size=(15, 1), font=('Helvetica', 18), text_color='red', key='input')],
            [sg.Txt(''  * 10)],
            [sg.Button('(', size=(5,2)), sg.Button(')', size=(5,2)), sg.Button('c', size=(5,2)), sg.Button('«', size=(5,2))],
            [sg.Button('7', size=(5,2)), sg.Button('8', size=(5,2)), sg.Button('9', size=(5,2)), sg.Button('÷', size=(5,2))],
            [sg.Button('4', size=(5,2)), sg.Button('5', size=(5,2)), sg.Button('6', size=(5,2)), sg.Button('x', size=(5,2))],
            [sg.Button('1', size=(5,2)), sg.Button('2', size=(5,2)), sg.Button('3', size=(5,2)), sg.Button('-', size=(5,2))],
            [sg.Button('.', size=(5,2)), sg.Button('0', size=(5,2)), sg.Button('=', size=(5,2)), sg.Button('+', size=(5,2))],
            ]

    # Set PySimpleGUI
    window = sg.Window('CALCULATOR', layout, grab_anywhere=False)

    # Set Process
    Equal = ''
    List_Op_Error =  ['+','-','*','/','(']

    # Loop
    while True:
        event, value = window.read()                            # call GUI
        
        if event == 'c': 
            # Clear
            Equal = ''
            window['input'].update(Equal)
        elif event == '«':
            # Delete last char
            Equal = Equal[:-1]
            window['input'].update(Equal)
        elif len(Equal) == 16 :
            # If the number is too long, do nothing
            pass
        elif str(event) in '1234567890+-().':
            # Typed a number
            Equal += str(event)
            window['input'].update(Equal) 
        elif event == 'x':
            # Entered an x
            Equal += '*'
            window['input'].update(Equal)
        elif event == '÷':
            # Entered a ÷
            Equal += '/'
            window['input'].update(Equal)
        
    # Process Conditional - Check arithmetic rules
        elif event == '=':
            # Error Case
            for i in List_Op_Error :  
                if '*' == Equal[0] or '/' == Equal[0] or ')' == Equal[0]  or i == Equal[-1]:   
                    # Check Error Case: *, /, or ) at the beginning of the statement or +, -, *, /, or ( at the end 
                    Answer = "Error Operation" 
                    break
                elif '/0' in Equal or '*/' in Equal or '/*' in Equal :
                    Answer = "Error Operation" 
                    break
                elif '(' in Equal :
                    if ')' not in Equal :
                        Answer = "Error Operation" 
                        break   
                elif '(' not in Equal:
                    if ')' in Equal:
                        Answer = "Error Operation" 
                        break
        # Calculate Case    
            else :
                Answer = str("%0.2f" %(eval(Equal)))                         # eval(Equal)  
                if '.0' in Answer:
                    Answer = str(int(float(Answer)))                         # convert float to int
            window['input'].update(Answer)                         # Update to GUI
            Equal = Answer

        elif event == 'Quit'  or event == None:                            # QUIT Program
            break

def conversion_calculator():
    first = True

    # Set unit lists
    len_units = ['Inch', 'Foot', 'Yard', 'Millimeter', 'Centimeter', 'Meter']
    temp_units = ['Fahrenheit', 'Celsius', 'Kelvin']
    vol_units = ['Teaspoon', 'Tablespoon', 'Fluid Ounce', 'Cup', 'Pint', 'Quart', 'Gallon', 'Liter']
    weight_units = ['Ounce', 'Pound', 'Gram', 'Kilogram']

    # Set up Tab layouts
    len_layout = [
        [sg.T('From:', size=(20,1)), sg.T('To:', size=(20,1))],
        [sg.In(size=(22,1), enable_events=True, key='-FROM_L-'), sg.T(size=(20,1), key='-TO_L-', background_color='white')],
        [sg.Listbox(len_units, key='-FROM_UNIT_L-', enable_events=True, size=(20,12)), sg.Listbox(len_units, key='-TO_UNIT_L-', enable_events=True, size=(20,12))]
    ]

    temp_layout = [
        [sg.T('From:', size=(20,1)), sg.T('To:', size=(20,1))],
        [sg.In(size=(22,1), enable_events=True, key='-FROM_T-'), sg.T(size=(20,1), key='-TO_T-', background_color='white')],
        [sg.Listbox(temp_units, key='-FROM_UNIT_T-', enable_events=True, size=(20,12)), sg.Listbox(temp_units, key='-TO_UNIT_T-', enable_events=True, size=(20,12))]
    ]

    vol_layout = [
        [sg.T('From:', size=(20,1)), sg.T('To:', size=(20,1))],
        [sg.In(size=(22,1), enable_events=True, key='-FROM_V-'), sg.T(size=(20,1), background_color='white', key='-TO_V-')],
        [sg.Listbox(vol_units, key='-FROM_UNIT_V-', enable_events=True, size=(20,12)), sg.Listbox(vol_units, key='-TO_UNIT_V-', enable_events=True, size=(20,12))]
    ]

    weight_layout = [
        [sg.T('From:', size=(20,1)), sg.T('To:', size=(20,1))],
        [sg.In(size=(22,1), enable_events=True, key='-FROM_W-'), sg.T(size=(20,1), key='-TO_W-', background_color='white')],
        [sg.Listbox(weight_units, key='-FROM_UNIT_W-', enable_events=True, size=(20,12)), sg.Listbox(weight_units, key='-TO_UNIT_W-', enable_events=True, size=(20,12))]
    ]

    # Layout
    layout = [      
        [sg.TabGroup([[sg.Tab('Length', len_layout),
                        sg.Tab('Temperature', temp_layout),
                        sg.Tab('Volume', vol_layout),
                        sg.Tab('Weight', weight_layout)]])]
    ]

    # Launch window
    window = sg.Window('Unit conversion', layout, grab_anywhere=False)

    while True:
        event, values = window.read()
        print("Event is ", event, " Value is ", values[event])
        if event == sg.WIN_CLOSED:
            break
        elif event == '-FROM_L-':
            # The user has entered a length to convert
            if values['-FROM_UNIT_L-']==[] or values['-TO_UNIT_L-']==[]:
                # If there is no selected unit, do nothing
                pass
            else:
                print("converting... hopefully")
            pass
    window.close()

conversion_calculator()