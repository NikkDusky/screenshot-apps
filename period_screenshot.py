from PIL import ImageGrab
from time import localtime, strftime, sleep
from loguru import logger
from os import mkdir, path, system
from sys import stdout
from configparser import ConfigParser

class ScreenShot():
    def __init__(self):
        system("title Screenshot maker.")
        self.cfg_file = 'screenshot_settings.ini'
        self.config = ConfigParser()
        self.counter = 0
        logging_model = {
            "handlers": [
                {"sink": stdout, "format": "[<cyan>{time:YYYY-MM-DD HH:mm:ss}</cyan>] [<level>{level}</level>] <level>{message}</level>"}
                ]
        }
        logger.configure(**logging_model)

    def createConfig(self, period=1800):
        self.config.add_section("screenshot_settings")
        self.config.set("screenshot_settings", "period", f"{period}")
        with open(self.cfg_file, "w") as config_file:
            self.config.write(config_file)

    def checkConfigExist(self):
        logger.info(f"{self.cfg_file} проверяю наличие.")
        if path.isfile(self.cfg_file):
            logger.success(f"{self.cfg_file} существует, запускаю программу.")
            self.getConfigSettings()
            pass
        else:
            logger.error(f"{self.cfg_file} не найден, создаю новый.")
            self.createConfig()
            self.getConfigSettings()

    def getConfigSettings(self):
        logger.info(f"Получаю настройки из {self.cfg_file}")
        self.config.read(self.cfg_file)
        self.period = int(self.config.get("screenshot_settings", "period"))
        logger.info(f"Периодичность скриншотов получена = {self.period} с.")

    def make_dir(self):
        self.dir_name = strftime('%d.%m.%y')
        logger.info(f"Создаю дирректорию: {self.dir_name}")
        try:
            mkdir(f"{self.dir_name}")
        except:
            pass

    def get_time(self):
        named_tuple = localtime()
        return (f'{strftime("%H-%M-%S", named_tuple)}')

    def get_screenshot(self):
        screen_name = f"{self.get_time()}.png"
        print("\033[A\033[A")
        screen = ImageGrab.grab(include_layered_windows=True)
        screen.save(f'{self.dir_name}\{screen_name}')
        screen.close()
        logger.info(f"Скриншот сохранён: {screen_name}\n")

    def timer(self):
        if self.period > self.counter:
            print("\033[A\033[A")
            logger.info(f"Следующий скриншот через: {self.period - self.counter} с. ")
            self.counter += 1
            sleep(0.98)
        else:
            try:
                self.get_screenshot()
            except:
                pass
            self.counter = 0

if __name__ == '__main__':
    ss = ScreenShot()
    ss.checkConfigExist()
    ss.make_dir()
    while True:
        ss.timer()