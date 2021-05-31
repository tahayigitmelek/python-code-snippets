
import pyautogui
import time

time.sleep(8)

pyautogui.click()
uzunluk = 500

while uzunluk > 0:
    pyautogui.dragRel(uzunluk, 0, duration = 0.1) #sağa çizgi
    uzunluk = uzunluk - 5
    pyautogui.dragRel(0, uzunluk, duration = 0.1) #aşağı çizgi
    pyautogui.dragRel(-uzunluk, 0, duration = 0.1) #sola çizgi
    uzunluk -= 5
    pyautogui.dragRel(0, -uzunluk, duration = 0.1)