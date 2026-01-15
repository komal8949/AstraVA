
import os
from core.speaker import speak

APP_MAP = {
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "notepad": "notepad.exe",
    "calculator": "calc.exe"
}

def open_application(command):
    for app in APP_MAP:
        if app in command:
            try:
                os.startfile(APP_MAP[app])
                speak(f"Opening {app}")
                return
            except:
                speak("Failed to open application")
    speak("Application not found")
