import pyautogui as pa
from time import sleep
import keyboard


def scroll(loop=12, time=2.5):
    for _ in range(loop):
        pa.scroll(-500)
        sleep(time)
# sleep(5)
# print(pa.position())