import pyautogui
import keyboard
import time

def ads():
    print("ads Working..................")
    for i in range(15):
        while keyboard.is_pressed('t') == False:
            pyautogui.click(x=1473, y=550)
            time.sleep(1)
            pyautogui.click(x=1473, y=550)
            time.sleep(5)
            pyautogui.click(x=1896, y=919)
            time.sleep(15)
            pyautogui.click(x=1473, y=550)
            break


def spin():
    print("Spin Working..................")
    for i in range(15):
        while keyboard.is_pressed('t') == False:
            pyautogui.click(x=1607, y=811) # Start
            time.sleep(5)
            pyautogui.click(x=1608, y=731) #Collact
            time.sleep(1)
            pyautogui.click(x=1896, y=919) #Back
            time.sleep(2)
            pyautogui.click(x=1608, y=731)  # Collact
            time.sleep(2)
            pyautogui.click(x=1608, y=731)  # Collact
            time.sleep(1)
            pyautogui.click(x=1896, y=919) #Back
            break



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        print('''
        1.spin
        2.ads
        ''')
        choice = int(input("Enter your choice : "))
        operation = [spin, ads]
        operation[choice - 1]()


