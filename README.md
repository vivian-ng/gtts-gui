# GUI for gTTS

This is a GUI for [gTTS](https://github.com/pndurette/gTTS) created using [PySimpleGUI](https://pysimplegui.readthedocs.io). gTTS is a Python package that allows the use of Google's Text-to-Speech service. The GUI allows you to enter the text to be converted to speech, the language for the speech/text, and also the option to save the output to a file. You can also speed up the speech (1.25 or 1.5 times) because the default speed can sound a bit slow. The audio playback uses the [pydub](https://github.com/jiaaro/pydub) package.

## Requirements
```
gTTS
pydub
PySimpleGUI
```

## Limitations

Currently, the voices available are limited to whatever voice is available for that language on Google's service.