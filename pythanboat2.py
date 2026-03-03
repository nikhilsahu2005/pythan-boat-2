import pyautogui
import pyperclip
import time
import requests

OPENROUTER_API_KEY = ""

time.sleep(3)

# 1️⃣ Click chat
pyautogui.click(1176, 1165)
time.sleep(1)

# 2️⃣ Select chat history
pyautogui.moveTo(712, 190, duration=0.4)
pyautogui.dragTo(712, 1113, duration=1, button='left')

time.sleep(1)
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)

chat_history = pyperclip.paste()
print("Chat History:\n", chat_history)

if not chat_history.strip():
    exit()

# Extract last message only
last_message = chat_history.strip().split("\n")[-1]

# 🔥 OpenRouter API Call
response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    },
    json={
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": "You are a person named Nikhil Sahu who speaks hindi as well as english. you are from india and you are a coder. you analyze chat history and respose like Nikhil Sahu.Output should be the next chat response as Nikhil Sahu"
            },
            {
                "role": "user",
                "content": last_message
            }
        ]
    }
)

result = response.json()

if "choices" not in result:
    print("API Error:", result)
    exit()

ai_reply = result["choices"][0]["message"]["content"]

print("AI Reply:\n", ai_reply)

# Copy reply
pyperclip.copy(ai_reply)

# Click message box
pyautogui.click(849, 1086)
time.sleep(1)

# Paste
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# Send
pyautogui.press('enter')
