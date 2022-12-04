from googletrans import Translator
import googletrans
import PySimpleGUI as sg

translator = Translator()

sg.theme('Dark Blue')
languages = googletrans.LANGUAGES.values()
languagedict = googletrans.LANGUAGES

layout = [[sg.Multiline(key='-INPUT-',size=(50,10)),sg.Spin(languages, key='-languagepicker-'),sg.Text('',key='-TEXT-',background_color='#3A5165',text_color='white',size=(50,10))],
        [sg.Button('Translate!',size=(103,2),key='-translate-')],
        []]
window = sg.Window('Translator', layout,element_justification='c',size=(900,200))


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == '-translate-':
        inputvalue = values['-INPUT-']
        translatelanguage = values['-languagepicker-']
        translatelanguage = translatelanguage.replace("'","")
        translatelanguage = translatelanguage.replace(',','')
        if '{' in translatelanguage:
            translatelanguage = translatelanguage.replace('{','')
        elif '}' in translatelanguage:
            translatelanguage = translatelanguage.replace('}','')
        key_list = list(languagedict.keys())
        val_list = list(languagedict.values())
    
        position = val_list.index(translatelanguage)

        translation = translator.translate(inputvalue, dest=key_list[position])
        window['-TEXT-'].update(translation.text)

    