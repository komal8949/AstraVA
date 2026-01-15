
def classify_intent(command):
    if "open" in command:
        return "open_app"
    if "explain" in command or "code" in command:
        return "explain_code"
    if "exit" in command or "stop" in command:
        return "exit"
    return "unknown"
