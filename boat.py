import pyautogui
import time
import pyperclip
import google.generativeai as genai

# 🔑 API KEY
genai.configure(api_key="AIzaSyC5_pDnxQhtwU6x6uvtMJl34U1LsyH1r-E")

model = genai.GenerativeModel("gemini-1.5-flash")

YOUR_NAME = "Nikhil Sahu"   # 👈 Apna exact WhatsApp name
last_processed_message = ""

time.sleep(5)

while True:
    time.sleep(5)

    # 🔹 Select chat
    pyautogui.moveTo(712, 190, duration=0.5)
    pyautogui.dragTo(712, 1060, duration=1, button='left')

    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)

    chat_history = pyperclip.paste().strip()

    if not chat_history:
        continue

    lines = chat_history.split("\n")
    last_line = lines[-1]

    print("Last Line:", last_line)

    # ❌ Skip if last message is yours
    if YOUR_NAME in last_line:
        continue

    # Extract message text safely
    if ":" not in last_line:
        continue

    last_message = last_line.split(":", 1)[1].strip()

    if not last_message:
        continue

    # ❌ Skip if already replied
    if last_message == last_processed_message:
        continue

    print("Sender Message:", last_message)

    try:
        response = model.generate_content(
            f"""
You are Naruto from India.
Reply naturally in Hindi + English.
Short WhatsApp style (1-2 lines).
Sound human. No timestamps. No names.

Message:
{last_message}

Reply:
""",
            generation_config={"temperature": 0.9}
        )

        # ✅ Safe extraction
        bot_reply = ""
        if hasattr(response, "text") and response.text:
            bot_reply = response.text.strip()
        elif response.candidates:
            bot_reply = response.candidates[0].content.parts[0].text.strip()

        if not bot_reply:
            print("Empty AI reply, skipping...")
            continue

    except Exception as e:
        print("API Error:", e)
        continue

    print("AI Reply:", bot_reply)

    # 🔹 Click message box
    pyautogui.click(1506, 254)
    time.sleep(1)

    pyperclip.copy(bot_reply)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

    # Save processed message
    last_processed_message = last_message