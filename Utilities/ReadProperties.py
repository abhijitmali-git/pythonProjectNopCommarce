import configparser
config=configparser.RawConfigParser()
config.read(".\\Configration\\Config.ini")

class Readconfig:
    @staticmethod
    def getApplication():
        url=config.get('Common Info','baseURL')
        return url

    @staticmethod
    def getUsername():
        username=config.get('Common Info','username')
        return username

    @staticmethod
    def getPassword():
        password=config.get('Common Info','password')
        return password

