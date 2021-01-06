import subprocess
import ctypes
import sys
from subprocess import DEVNULL
from time import sleep


class UHSFS:

    def __init__(self):
        self.PATH_TO_FILE = None
        self.RULE_NAME = None
        self.get_settings()

    def _add_rule(self, rule_name, file_patch):
        pass

    def _switch_rule(self, rule_name, state):
        pass

    def get_settings(self):
        with open('settings.txt', 'r') as f:
            settings = f.readlines()
            path2file, rule_name = settings[0].split('=') or '', settings[1].split('=') or 'Hearthstone_Fast_DC'
            path2file, rule_name = path2file[1].strip().removesuffix('\n'), rule_name[1].strip().removesuffix('\n')

        self.PATH_TO_FILE = path2file
        self.RULE_NAME = rule_name

    def __str__(self):
        return f'Path to Hearthstone.exe: {self.PATH_TO_FILE}\nFirewall Rule Name: {self.RULE_NAME}'

    def _main(self):
        pass


if __name__ == '__main__':
    hsfs = UHSFS()
    print(str(hsfs))
