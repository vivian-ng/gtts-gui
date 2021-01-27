#!/usr/bin/env python3
'''
    Adapted PySimpleGUI Google Text to Speech example
    Gets a multiline input, select a language, and either playback or save the speech output.
    Playback speed can also be changed.

    Original example: https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Google_TTS.py

    author: vivian-ng
'''
import PySimpleGUI as sg
from gtts import gTTS
from gtts import lang
import os
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play

# Build list of available languages
langs = []
for k in lang.tts_langs().keys():
    langs.append(k)

# Function to get sound from text using Google TTS
def get_sound_from_gtts(values):
    tts = gTTS(text=values['-INPUTTEXT-'], lang=values['-LANG-'], slow=False)
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    sound = AudioSegment.from_file(fp, format="mp3")
    if values['-SPEED-'] != 1.0:
        sound = sound.speedup(playback_speed=float(values['-SPEED-']))
    return sound

def run_gui():

    # Create the layout
    layout = [[sg.Text('What would you like me to say?'), sg.Text('Language:'), sg.Combo(langs, key='-LANG-', default_value='en'), sg.Text('Speed:'), sg.Combo([ 1.0, 1.25, 1.5 ], key='-SPEED-', default_value=1.0)],
              [sg.MLine(size=(60,10), enter_submits=True, key='-INPUTTEXT-')],
              [sg.InputText(key='File to Save', enable_events=True, justification='l'),
               sg.FileSaveAs('Select')],
              [sg.Button('Speak'), sg.Button('Save'), sg.Exit()]]

    # Create the window
    window = sg.Window('Google Text to Speech', layout)

    # Loop to handle the GUI
    while True:
        event, values = window.read()
        if event == 'Save':  # Save button pressed
            if values['File to Save'] != '':  # File name has been defined
                sound = get_sound_from_gtts(values)
                sound.export(values['File to Save'], 'mp3')
            else:  # Error because no file name defined
                sg.popup_error('No file selected!')
        elif event == 'Save As':  # Launch file browser to select file name for saving
            filename = values['Save As']
            if filename:
                window['File to Save'].update(value=filename)
        elif event in (sg.WIN_CLOSED, 'Exit'):  # Exit button or close button pressed
            break
        elif event == 'Speak':  # Speak button pressed
            sound = get_sound_from_gtts(values)
            play(sound)

    # Properly close the window
    window.close()

# Main program
def main():
    run_gui()
    # TODO: Add argument parser? Or just rely on gtts-cli command?

if __name__ == "__main__":
    main()
