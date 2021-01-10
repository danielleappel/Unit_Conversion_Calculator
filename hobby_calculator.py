import PySimpleGUI as sg    

sg.ChangeLookAndFeel('Reddit')  


def numerical_calculator():
    # Code originally adapted from https://gist.github.com/ball13411/39014c86945ac40bbd7c39677b560991

    # Layout                                                         # Creat GUI
    layout = [
        [sg.Txt(''  * 10)],                      
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
    # Set unit lists and conversion equations
    len_units = ['Inch', 'Foot', 'Yard', 'Mile', 'Millimeter', 'Centimeter', 'Meter', 'Kilometer']
    convert_l = [
        [lambda x: x, lambda x: x*1/12, lambda x: x*1/36, lambda x: x/63360, lambda x: x*25.4, lambda x: x*2.54, lambda x: x*0.0254, lambda x: x/39370],
        [lambda x: x*12, lambda x: x, lambda x: x*1/3, lambda x: x/5280, lambda x: x*304.8, lambda x: x*30.48, lambda x: x*0.3048, lambda x: x/3281],
        [lambda x: x*36, lambda x: x*3, lambda x: x, lambda x: x/1760, lambda x: x*914.4, lambda x: x*91.44, lambda x: x*0.9144, lambda x: x/1094],
        [lambda x: x*63360, lambda x: x*5280, lambda x: x*1760, lambda x: x, lambda x: x*1609340, lambda x: x*160934, lambda x: x*1609.34, lambda x: x*1.60934],
        [lambda x: x*1/25.4, lambda x: x*1/304.8, lambda x: x*1/914.4, lambda x: x/1609340, lambda x: x, lambda x: x*0.1, lambda x: x*0.001, lambda x: x/1000000],
        [lambda x: x*1/2.54, lambda x: x*1/30.48, lambda x: x*1/91.44, lambda x: x/160934, lambda x: x*10, lambda x: x, lambda x: x*0.01, lambda x: x/100000],
        [lambda x: x*39.37, lambda x: x*3.28084, lambda x: x*1.09361, lambda x: x/1609.34, lambda x: x*1000, lambda x: x*100, lambda x: x, lambda x: x/1000],
        [lambda x: x*39370, lambda x: x*3280.84, lambda x: x*1093.61, lambda x: x/1.609, lambda x: x*1000000, lambda x: x*100000, lambda x: x*1000, lambda x: x]
    ]
    key_l = {'Inch' : 0, 'Foot' : 1, 'Yard' : 2, 'Mile' : 3, 'Millimeter' : 4,
                'Centimeter' : 5, 'Meter' : 6, 'Kilometer': 7}

    temp_units = ['Fahrenheit', 'Celsius', 'Kelvin']
    convert_t = [
        [lambda x: x, lambda x: (x-32)*(5/9), lambda x: (x-32)*(5/9)+273.15],
        [lambda x: (x*9/5)+32, lambda x: x, lambda x: x+273.15],
        [lambda x: (x-273.15)*9/5+32, lambda x: x-273.15, lambda x: x]
    ]
    key_t = {'Fahrenheit' : 0, 'Celsius' : 1, 'Kelvin' : 2}

    vol_units = ['Teaspoon', 'Tablespoon', 'Fluid Ounce', 'Cup', 'Pint', 'Quart', 'Gallon', 'Liter']
    convert_v = [
        [lambda x: x, lambda x: x*1/3, lambda x: x*1/6, lambda x: x*1/48, lambda x: x*1/96, lambda x: x*1/192, lambda x: x*1/768, lambda x: x*1/202.884],
        [lambda x: x*3, lambda x: x, lambda x: x*1/2, lambda x: x*1/16, lambda x: x*1/32, lambda x: x*1/64, lambda x: x*1/256, lambda x: x*1/67.628],
        [lambda x: x*6, lambda x: x*2, lambda x: x, lambda x: x*1/8, lambda x: x*1/16, lambda x: x*1/32, lambda x: x*1/128, lambda x: x*1/33.814],
        [lambda x: x*48, lambda x: x*16, lambda x: x*8, lambda x: x, lambda x: x*1/2, lambda x: x*1/4, lambda x: x*1/16, lambda x: x*1/4.227],
        [lambda x: x*96, lambda x: x*32, lambda x: x*16, lambda x: x*2, lambda x: x, lambda x: x*1/2, lambda x: x*1/18, lambda x: x*1/2.113],
        [lambda x: x*192, lambda x: x*64, lambda x: x*32, lambda x: x*4, lambda x: x*2, lambda x: x, lambda x: x*1/4, lambda x: x*1/1.057],
        [lambda x: x*768, lambda x: x*256, lambda x: x*128, lambda x: x*16, lambda x: x*8, lambda x: x*4, lambda x: x, lambda x: x*3.785],
        [lambda x: x*202.884, lambda x: x*67.628, lambda x: x*33.814, lambda x: x*4.227, lambda x: x*2.113, lambda x: x*1.057, lambda x: x*1/3.785, lambda x: x]
    ]
    key_v = {'Teaspoon' : 0, 'Tablespoon' : 1, 'Fluid Ounce' : 2, 'Cup' : 3,
                'Pint' : 4, 'Quart' : 5, 'Gallon' : 6, 'Liter' : 7}

    weight_units = ['Ounce', 'Pound', 'Gram', 'Kilogram']
    convert_w = [
        [lambda x: x, lambda x: x*1/16, lambda x: x*28.3495, lambda x: x*1/35.274],
        [lambda x: x*16, lambda x: x, lambda x: x*454, lambda x: x*1/2.205],
        [lambda x: x*1/28.35, lambda x: x*1/454, lambda x: x, lambda x: x*1/1000],
        [lambda x: x*35.274, lambda x: x*2.205, lambda x: x*1000, lambda x: x]
    ]
    key_w = {'Ounce' : 0, 'Pound' : 1, 'Gram' : 2, 'Kilogram' : 3}

    # Set up Tab layouts
    len_layout = [
        [sg.T('From:', size=(20,1)), sg.T('To:', size=(20,1))],
        [sg.In(size=(22,1), enable_events=True, key='-INPUT_L-'), sg.T(size=(20,1), key='-OUTPUT_L-', background_color='#d3dee8', relief=sg.RELIEF_SUNKEN, text_color='black')],
        [sg.Listbox(len_units, key='-FROM_UNIT_L-', enable_events=True, size=(20,12)), sg.Listbox(len_units, key='-TO_UNIT_L-', enable_events=True, size=(20,12))]
    ]

    temp_layout = [
        [sg.T('From:', size=(20,1)), sg.T('To:', size=(20,1))],
        [sg.In(size=(22,1), enable_events=True, key='-INPUT_T-'), sg.T(size=(20,1), key='-OUTPUT_T-', background_color='#d3dee8', relief=sg.RELIEF_SUNKEN, text_color='black')],
        [sg.Listbox(temp_units, key='-FROM_UNIT_T-', enable_events=True, size=(20,12)), sg.Listbox(temp_units, key='-TO_UNIT_T-', enable_events=True, size=(20,12))]
    ]

    vol_layout = [
        [sg.T('From:', size=(20,1)), sg.T('To:', size=(20,1))],
        [sg.In(size=(22,1), enable_events=True, key='-INPUT_V-'), sg.T(size=(20,1), background_color='#d3dee8', relief=sg.RELIEF_SUNKEN, key='-OUTPUT_V-', text_color='black')],
        [sg.Listbox(vol_units, key='-FROM_UNIT_V-', enable_events=True, size=(20,12)), sg.Listbox(vol_units, key='-TO_UNIT_V-', enable_events=True, size=(20,12))]
    ]

    weight_layout = [
        [sg.T('From:', size=(20,1)), sg.T('To:', size=(20,1))],
        [sg.In(size=(22,1), enable_events=True, key='-INPUT_W-'), sg.T(size=(20,1), key='-OUTPUT_W-', background_color='#d3dee8', relief=sg.RELIEF_SUNKEN, text_color='black')],
        [sg.Listbox(weight_units, key='-FROM_UNIT_W-', enable_events=True, size=(20,12)), sg.Listbox(weight_units, key='-TO_UNIT_W-', enable_events=True, size=(20,12))]
    ]

    # Set lists of the buttons for easy access
    input_list = ['-INPUT_L-', '-INPUT_T-', '-INPUT_V-', '-INPUT_W-']
    input_index = {'-INPUT_L-' : 0, '-INPUT_T-' : 1, '-INPUT_V-' : 2, '-INPUT_W-' : 3}

    from_list = ['-FROM_UNIT_L-', '-FROM_UNIT_T-', '-FROM_UNIT_V-', '-FROM_UNIT_W-']
    from_index = {'-FROM_UNIT_L-' : 0, '-FROM_UNIT_T-' : 1, '-FROM_UNIT_V-' : 2, '-FROM_UNIT_W-' : 3}

    to_list = ['-TO_UNIT_L-', '-TO_UNIT_T-', '-TO_UNIT_V-', '-TO_UNIT_W-']
    to_index = {'-TO_UNIT_L-' : 0, '-TO_UNIT_T-' : 1, '-TO_UNIT_V-' : 2, '-TO_UNIT_W-' : 3}

    output_list = ['-OUTPUT_L-', '-OUTPUT_T-', '-OUTPUT_V-', '-OUTPUT_W-']

    convert = [convert_l, convert_t, convert_v, convert_w]
    key = [key_l, key_t, key_v, key_w]

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
        # ----- Input number ------------
        if event in input_list:
            i = input_index[event]
            if values[from_list[i]]==[] or values[to_list[i]]==[]:
                # If there is no selected unit, do nothing
                pass
            else:
                curr_key = key[i]

                c = curr_key[values[to_list[i]][0]]
                r = curr_key[values[from_list[i]][0]]

                converter = convert[i]
                
                result = converter[r][c](int(values[input_list[i]]))
                window[output_list[i]].update(result)
        # ----- Unit changed
        elif event in from_list:
            i = from_index[event]
            if values[to_list[i]]==[] or values[input_list[i]] == '':
                # If there is no selected "to" unit or no number, do nothing
                pass
            else:
                curr_key = key[i]

                c = curr_key[values[to_list[i]][0]]
                r = curr_key[values[from_list[i]][0]]

                converter = convert[i]

                result = converter[r][c](int(values[input_list[i]]))
                window[output_list[i]].update(result)
        elif event in to_list:
            i = to_index[event]
            if values[from_list[i]] == [] or values[input_list[i]] == '':
                # If there is no selected "from" unit or no number, do nothing
                pass
            else:
                curr_key = key[i]
                
                c = curr_key[values[to_list[i]][0]]
                r = curr_key[values[from_list[i]][0]]

                converter = convert[i]

                result = converter[r][c](int(values[input_list[i]]))
                window[output_list[i]].update(result)
    window.close()
