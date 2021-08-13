from PIL import ImageGrab
from time import localtime, strftime, sleep
from loguru import logger
from os import mkdir, system
from sys import stdout
import keyboard

class ScreenShot():
    def __init__(self):
        system("title Screenshot maker.")
        self.cfg_file = 'screenshot_settings.ini'
        self.counter = 0
        logging_model = {
            "handlers": [
                {"sink": stdout, "format": "[<cyan>{time:YYYY-MM-DD HH:mm:ss}</cyan>] [<level>{level}</level>] <level>{message}</level>"}
                ]
        }
        logger.configure(**logging_model)

    def make_dir(self):
        self.dir_name = strftime('%d.%m.%y')
        try:
            mkdir(f"{self.dir_name}")
        except:
            pass

    def get_time(self):
        named_tuple = localtime()
        return (f'{strftime("%H-%M-%S", named_tuple)}')

    def get_screenshot(self):
        ss.make_dir()
        screen_name = f"{self.get_time()}.png"
        print("\033[A\033[A")
        screen = ImageGrab.grab(include_layered_windows=True)
        screen.save(f'{self.dir_name}\{screen_name}')
        screen.close()
        logger.info(f"Скриншот сохранён: {screen_name}\n")

if __name__ == '__main__':
    ss = ScreenShot()
    while True:
        while True:
            if keyboard.read_key() == "-":
                ss.get_screenshot()
                break
        sleep(0.5)