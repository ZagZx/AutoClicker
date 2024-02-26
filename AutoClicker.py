import pyautogui
import keyboard

if keyboard.is_pressed('pagedown'):
    ligado = True
    while ligado:
         pyautogui.click()
         if keyboard.is_pressed('pagedown'):
             ligado = False



