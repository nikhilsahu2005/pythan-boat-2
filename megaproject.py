import pyautogui
import pyperclip
import time
from google import genai

# 🔐 Gemini Client
client = genai.Client(api_key="AIzaSyDU7e5W77jGORsCh9iPO_ttWfNpsEoTz9I")

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

# 3️⃣ Gemini AI Response
completion = client.models.generate_content(
       model="gemini-2.0-flash",
    contents=f"""
You are Nikhil from India.
You are a coder.
You roast people in a funny way.
Do not include timestamps.
Output only the next WhatsApp message.

Chat history:
{chat_history}
"""
)

response = completion.text
print("AI Reply:\n", response)

# 4️⃣ Copy reply
pyperclip.copy(response)

# 5️⃣ Click message box
pyautogui.click(849, 1086)
time.sleep(1)

# 6️⃣ Paste
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# 7️⃣ Send
pyautogui.press('enter')