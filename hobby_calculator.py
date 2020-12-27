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

    # Set unit lists and coefficients
    len_units = ['Inch', 'Foot', 'Yard', 'Millimeter', 'Centimeter', 'Meter']
    coeff_l = [[1, 1/12, 1/36, 25.4, 2.54, 0.0254],
               [12, 1, 1/3, 304.8, 30.48, 0.3048],
               [36, 3, 1, 914.4, 91.44, 0.9144],
               [1/25.4, 1/304.8, 1/914.4, 1, 0.1, 0.001],
               [1/2.54, 1/30.48, 1/91.44, 10, 1, 0.01],
               [39.37, 3.281, 1.094, 1000, 100, 1]]
    key_l = {'Inch' : 0, 'Foot' : 1, 'Yard' : 2, 'Millimeter' : 3,
                'Centimeter' : 4, 'Meter' : 5}

    temp_units = ['Fahrenheit', 'Celsius', 'Kelvin']
    convert_t = [[lambda x: x, lambda x: (x-32)*(5/9), lambda x: (x-32)*(5/9)+273.15],
                 [lambda x: (x*9/5)+32, lambda x: x, lambda x: x+273.15],
                 [lambda x: (x-273.15)*9/5+32, lambda x: x-273.15, lambda x: x]]
    key_t = {'Fahrenheit' : 0, 'Celsius' : 1, 'Kelvin' : 2}

    vol_units = ['Teaspoon', 'Tablespoon', 'Fluid Ounce', 'Cup', 'Pint', 'Quart', 'Gallon', 'Liter']
    weight_units = ['Ounce', 'Pound', 'Gram', 'Kilogram']

    # Set up Tab layouts
    len_layout = [
        [sg.T('From:', size=(20,1)), sg.T('To:', size=(20,1))],
        [sg.In(size=(22,1), enable_events=True, key='-INPUT_L-'), sg.T(size=(20,1), key='-OUTPUT_L-', background_color='white', text_color='black')],
        [sg.Listbox(len_units, key='-FROM_UNIT_L-', enable_events=True, size=(20,12)), sg.Listbox(len_units, key='-TO_UNIT_L-', enable_events=True, size=(20,12))]
    ]

    temp_layout = [
        [sg.T('From:', size=(20,1)), sg.T('To:', size=(20,1))],
        [sg.In(size=(22,1), enable_events=True, key='-INPUT_T-'), sg.T(size=(20,1), key='-OUTPUT_T-', background_color='white', text_color='black')],
        [sg.Listbox(temp_units, key='-FROM_UNIT_T-', enable_events=True, size=(20,12)), sg.Listbox(temp_units, key='-TO_UNIT_T-', enable_events=True, size=(20,12))]
    ]

    vol_layout = [
        [sg.T('From:', size=(20,1)), sg.T('To:', size=(20,1))],
        [sg.In(size=(22,1), enable_events=True, key='-INPUT_V-'), sg.T(size=(20,1), background_color='white', key='-OUTPUT_V-', text_color='black')],
        [sg.Listbox(vol_units, key='-FROM_UNIT_V-', enable_events=True, size=(20,12)), sg.Listbox(vol_units, key='-TO_UNIT_V-', enable_events=True, size=(20,12))]
    ]

    weight_layout = [
        [sg.T('From:', size=(20,1)), sg.T('To:', size=(20,1))],
        [sg.In(size=(22,1), enable_events=True, key='-INPUT_W-'), sg.T(size=(20,1), key='-OUTPUT_W-', background_color='white', text_color='black')],
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
        if event == sg.WIN_CLOSED:
            break
        # ----- Length functions --------
        elif event == '-INPUT_L-':
            # The user has entered a length to convert
            if values['-FROM_UNIT_L-']==[] or values['-TO_UNIT_L-']==[]:
                # If there is no selected unit or no number, do nothing
                pass
            else:
                c = key_l[values['-TO_UNIT_L-'][0]]
                r = key_l[values['-FROM_UNIT_L-'][0]]
                
                result = int(values['-INPUT_L-']) * coeff_l[r][c]
                window['-OUTPUT_L-'].update(result)
        elif event == '-FROM_UNIT_L-':
            if values['-TO_UNIT_L-']==[] or values['-INPUT_L-'] == '':
                # If there is no selected "to" unit or no number, do nothing
                pass
            else:
                c = key_l[values['-TO_UNIT_L-'][0]]
                r = key_l[values['-FROM_UNIT_L-'][0]]
                
                result = int(values['-INPUT_L-']) * coeff_l[r][c]
                window['-OUTPUT_L-'].update(result)
        elif event == '-TO_UNIT_L-':
            if values['-FROM_UNIT_L-'] == [] or values['-INPUT_L-'] == '':
                # If there is no selected "from" unit or no number, do nothing
                pass
            else:
                c = key_l[values['-TO_UNIT_L-'][0]]
                r = key_l[values['-FROM_UNIT_L-'][0]]
                
                result = int(values['-INPUT_L-']) * coeff_l[r][c]
                window['-OUTPUT_L-'].update(result)
        # ----- Temperature functions ------
        elif event == '-INPUT_T-':
            # The user has entered a temperature to convert
            if values['-FROM_UNIT_T-']==[] or values['-TO_UNIT_T-']==[]:
                # If there is no selected unit or no number, do nothing
                print("pass")
                pass
            else:
                c = key_t[values['-TO_UNIT_T-'][0]]
                r = key_t[values['-FROM_UNIT_T-'][0]]

                result = convert_t[r][c](int(values['-INPUT_T-']))
                window['-OUTPUT_T-'].update(result)
        elif event == '-FROM_UNIT_T-':
            if values['-TO_UNIT_T-']==[] or values['-INPUT_T-'] == '':
                # If there is no selected "to" unit or no number, do nothing
                pass
            else:
                c = key_t[values['-TO_UNIT_T-'][0]]
                r = key_t[values['-FROM_UNIT_T-'][0]]
                
                result = convert_t[r][c](int(values['-INPUT_T-']))
                window['-OUTPUT_T-'].update(result)
        elif event == '-TO_UNIT_T-':
            if values['-FROM_UNIT_T-'] == [] or values['-INPUT_T-'] == '':
                # If there is no selected "from" unit or no number, do nothing
                pass
            else:
                c = key_t[values['-TO_UNIT_T-'][0]]
                r = key_t[values['-FROM_UNIT_T-'][0]]
                
                result = convert_t[r][c](int(values['-INPUT_T-']))
                window['-OUTPUT_T-'].update(result)
    window.close()

conversion_calculator()