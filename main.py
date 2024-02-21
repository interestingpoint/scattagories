import pyautogui
import keyboard
import cv2
import pytesseract
keyboard.add_hotkey("`", lambda: print(pyautogui.position()))
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
while True:
    keyboard.wait("=")
    pyautogui.screenshot("sum.png", region=(56, 309, 834, 52))
    so = cv2.imread("sum.png")
    txt = pytesseract.image_to_string("sum.png")
    letter = txt[68]
    if letter == "|":
        letter = "i"
    y = 416
    for i in range(9):
        pyautogui.moveTo(116, y)
        pyautogui.tripleClick()
        keyboard.press("ctrl+c")
        keyboard.release("ctrl+c")
        keyboard.press("ctrl+n")
        keyboard.release("ctrl+n")
        pyautogui.moveTo(1310, 82, 0.2)
        pyautogui.click()
        pyautogui.write("list of ")
        keyboard.press("ctrl+v")
        keyboard.release("ctrl+v")
        pyautogui.write(" starting with ")
        pyautogui.write(letter)
        keyboard.press("enter")
        keyboard.release("enter")
        pyautogui.moveTo(210, 521, 3)
        pyautogui.tripleClick()
        keyboard.press("ctrl+c")
        keyboard.release("ctrl+c")
        keyboard.press("ctrl+w")
        keyboard.release("ctrl+w")
        pyautogui.moveTo(677, y)
        pyautogui.click()
        keyboard.press("ctrl+v")
        keyboard.release("ctrl+v")
        y = y + 75
    pyautogui.moveTo(116, 416)
    y = 796 + 75
    pyautogui.click()
    pyautogui.scroll(-10000000)
    for i in range(4):
        pyautogui.moveTo(116, y)
        pyautogui.tripleClick()
        keyboard.press("ctrl+c")
        keyboard.release("ctrl+c")
        keyboard.press("ctrl+n")
        keyboard.release("ctrl+n")
        pyautogui.moveTo(1310, 82, 0.2)
        pyautogui.click()
        pyautogui.write("list of ")
        keyboard.press("ctrl+v")
        keyboard.release("ctrl+v")
        pyautogui.write(" starting with ")
        pyautogui.write(letter)
        keyboard.press("enter")
        keyboard.release("enter")
        pyautogui.moveTo(210, 541, 3)
        pyautogui.tripleClick()
        keyboard.press("ctrl+c")
        keyboard.release("ctrl+c")
        keyboard.press("ctrl+w")
        keyboard.release("ctrl+w")
        pyautogui.moveTo(677, y)
        pyautogui.click()
        keyboard.press("ctrl+v")
        keyboard.release("ctrl+v")
        y = y + 75
