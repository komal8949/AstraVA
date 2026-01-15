
from core.listener import listen_command
from core.speaker import speak
from core.intent_classifier import classify_intent
from system_control.open_apps import open_application
from code_assistant.explain_code import explain_code

def main():
    speak("Astra is online. How can I help you?")
    while True:
        command = listen_command()
        if not command:
            continue

        intent = classify_intent(command)

        if intent == "open_app":
            open_application(command)
        elif intent == "explain_code":
            explain_code()
        elif intent == "exit":
            speak("Goodbye")
            break
        else:
            speak("Sorry, I did not understand that.")

if __name__ == "__main__":
    main()
