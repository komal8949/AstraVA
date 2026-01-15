
import pyperclip
from core.speaker import speak

def explain_code():
    code = pyperclip.paste()
    if not code.strip():
        speak("Clipboard is empty. Copy code first.")
        return

    explanation = f"This code has {len(code.splitlines())} lines. It performs logical operations."
    speak(explanation)
