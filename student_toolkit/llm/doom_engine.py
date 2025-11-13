import ollama

# Actual bot calling and chat setting up details ( could be replaced by genai if needed or seen necessary)
def ask_llm(user_input):
    response = ollama.chat(
        model="DOOM_BOT_ASSITANT",
        messages=[{"role": "user", "content": user_input}]
    )
    reply = response["message"]["content"]
    return reply
