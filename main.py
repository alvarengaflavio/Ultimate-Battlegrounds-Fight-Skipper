import subprocess
import ctypes
# import sys
from subprocess import DEVNULL
from time import sleep


class UHSBFS:

    def __init__(self):
        self.PATH_TO_FILE = 'C:\\Program Files (x86)\\Hearthstone\\Hearthstone.exe'
        self.RULE_NAME = 'Hearthstone_Fast_DC'
        self._get_settings()

    def __str__(self):
        return f'Path to Hearthstone.exe: {self.PATH_TO_FILE}\nFirewall Rule Name: {self.RULE_NAME}'

    # ###############      STATIC METHODS      ########################################################################
    @staticmethod
    def _check_admin():
        try:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        except AttributeError:
            is_admin = False
        return is_admin

    @staticmethod
    def _print_header():
        print(f'#' * 60 + '\n' + f'             Ultimate              '.center(60, '#') + '\n' +
              f'   Hearthstone Fight Skipper 0.2   '.center(60, '#') + '\n' +
              f'           by Veros 2020           '.center(60, '#') + '\n' + f'#' * 60 + '\n')

        print('\t' + f'  commands  '.center(46, '-') +
              '\n\tAdd Rule     [add]\tSkip Fight [yes][skip]\n'
              '\tExit Program [exit] \n' + '\t' + '-' * 46 + '\n')

    @staticmethod
    def _print_not_admin():
        print('\n\t\t' + '#' * 60 + '\n' +
              '\t\t' + f'   Please execute CMD with administration rights   '.center(60, '#') + '\n' +
              '\t\t' + '#' * 60 + '\n')

    @staticmethod
    def _finishing():
        print(f'\t\t\t\tFinishing...')
        sleep(2)
        print('\t\t\t\tDone!')
        sleep(0.5)
        return False

    # ##################################################################################################################

    def _add_rule(self):
        """
        Creates a new Firewall rule blocking Hearthstone communication
        """
        subprocess.call(
            f'netsh advfirewall firewall add rule name={self.RULE_NAME} dir=out action=block enable=no program={self.PATH_TO_FILE}',
            shell=True,
            stdout=DEVNULL,
            stderr=DEVNULL
        )
        print(f'\t\t\t\tRule {self.RULE_NAME}\n'
              f'\t\t\t\t{self.PATH_TO_FILE}\n'
              f'\t\t\t\tadded!\n')

    def _switch_rule(self, state):
        """
        Enable/Disable specific Windows Firewall rule
        :param state: 0 = disable / 1 = Enable
        """
        state, message = ('yes', 'Enabled') if state else ('no', 'Disabled')
        subprocess.call(
            f'netsh advfirewall firewall set rule name={self.RULE_NAME} new enable={state}',
            shell=True,
            stdout=DEVNULL,
            stderr=DEVNULL
        )

    def _get_settings(self):
        with open('./settings.txt', 'r') as f:
            settings = f.readlines()
            path2file, rule_name = settings[0].split('=') or self.PATH_TO_FILE, settings[1].split('=') or self.RULE_NAME
            path2file, rule_name = path2file[1].strip().removesuffix('\n'), rule_name[1].strip().removesuffix('\n')

        self.PATH_TO_FILE = path2file
        self.RULE_NAME = rule_name

    def main(self):
        if not self._check_admin():
            self._print_not_admin()
            return

        self._print_header()

        working = True
        while working:
            try:
                cmd = str(input('\t[cmd] Skip Next Battlegrounds Fight? '))[0].strip().lower()
            except Exception:
                continue

            if cmd in 'sy':
                print(f'\t\t\t\tSkipping Fight...')
                self._switch_rule(1)
                sleep(3)
                self._switch_rule(0)
                print(f'\t\t\t\tDone!\n')

            elif cmd in 'a':
                print(f'\t\t\t\tAdding Firewall Rule...')
                self._add_rule()

            elif cmd in 'nqe':
                working = self._finishing()


if __name__ == '__main__':
    bfs = UHSBFS()
    # print(str(bfs))
    bfs.main()
