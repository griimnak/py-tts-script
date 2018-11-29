import os
import sys
""" usage: python speak.py "Hello world"

    or use as a module:
    import speak
    speak.speak_windows("Hello world")
"""

__version__ = "0.1.0"
__author__  = "github.com/griimnak"
__all__ = ["speak_windows", "speak_linux"]

def speak_windows(speech):
    os.system(
        "powershell.exe -ExecutionPolicy ByPass "+
        "param([String]$text='"+speech+"'); Add-Type -AssemblyName System.speech;"+
        "$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer;"+
        "$speak.SelectVoice('Microsoft Zira Desktop'); $speak.Speak($text)"
    )

def speak_linux(speech):
    os.system('say "'+speech+'"')

def _cli_output(arg):
    print('[working]')
    if os.name == 'nt':
        return speak_windows(arg)
    return speak_linux(arg)

if __name__ == '__main__':
    try:
        _cli_output(sys.argv[1])
    except IndexError:
        print('''
usage: python speak.py "Hello world"

or use as a module:
import speak
speak.speak_windows("Hello world")''')
        exit()
