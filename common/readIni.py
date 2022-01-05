import os
from configparser import ConfigParser

class ReadIni():
    def __init__(self):
        path =os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        ini_path = os.path.join(path,"config","config.ini")
        #print(ini_path)
        self.cp = ConfigParser()
        self.file = self.cp.read(ini_path,encoding="utf-8-sig")

    def getSection(self):
        ini_section = self.cp.sections()
        print(ini_section)

    def getItem(self,section = 'loginfo'):
        ini_item = self.cp.items(section)
        print(ini_item)

    def getValue(self, section='host', option='host'):
        # cfg = self.cp.get(self.file)
        ini_value = self.cp.get(section, option)
        #print(ini_value)
        return ini_value

if __name__ == '__main__':
    ri = ReadIni()
    ri.getSection()
    ri.getItem()
    ri.getValue(section="host", option='host')