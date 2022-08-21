import pyautogui, time

#TIME TO PREPARE OPEN WHATSAPP DEKSTOP or WHATSAPP WEB"
#PLEASE BE AWARE OF THIS. CAUSED SOME SCREEN ERROR WHEN YOU OPEN ANOTHER SCREEN!
time.sleep(5)

position =pyautogui.position()
sendMessages = "<<ENTER YOUR MESSAGES HERE>>"

#START LOOPING
for a in range(50):
    pyautogui.click(position.x,position.y)
    pyautogui.typewrite(sendMessages)
    
    #CHECK STATEMENT IF SUCCESS ON TERMINAL
    print(sendMessages)

    #GIVE DELAY TIME TO SEND MESSAGES EVERY SECONDS
    time.sleep(1)

    #AUTO ENTER 
    pyautogui.typewrite(["enter"])