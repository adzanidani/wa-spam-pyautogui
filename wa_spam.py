from turtle import pos
import pyautogui, time
time.sleep(2)
position =pyautogui.position()
pesan = "<<ENTER YOUR MESSAGES HERE>>"

for a in range(50):
    pyautogui.click(position.x,position.y)
    pyautogui.typewrite(pesan)
    print(pesan)
    time.sleep(1)
    pyautogui.typewrite(["enter"])