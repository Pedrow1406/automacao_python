import pyautogui as pa
from time import sleep
import keyboard


def scroll():
    for _ in range(12):
        pa.scroll(-500)
        sleep(2.5)
# print(pa.position())-