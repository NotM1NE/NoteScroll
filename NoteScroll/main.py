import pyautogui
#Automatic scroll for notes
speed = int(input("How was fast u want to scroll:"))
dir = input("Which direction u want to scroll (UP or DOWN):")

while 0 < 10:
    if dir == "UP":
        pyautogui.scroll(speed)
    elif dir == "DOWN":
        pyautogui.scroll(-speed)

