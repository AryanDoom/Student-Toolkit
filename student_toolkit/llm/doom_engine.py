import ollama

# Actual bot calling and chat setting up details ( could be replaced by genai if needed or seen necessary)
def ask_llm(user_input):
    response = ollama.chat(
        model="DOOM_BOT_ASSITANT",
        messages=[{"role": "user", "content": user_input}]
    )
    reply = response["message"]["content"]
    return reply
#Gen ai  set up is done, the calling in ui file and main.py is done through the the genai bot in the git pushed files 