
class MainMenu:
    def __init__(self, interface):
        self.interface = interface
        self.connection = interface.connection

    def main_menu(self):
        print('MAIN MENU: Enter an option number or enter (q) to quit.')
        print('Options: (1) Search Business, (2) Search Users, (3) Make Friend, (4) Review Business, (q) Quit.')
        user_input = input("Enter your Input: ").strip()
        self.spc()

        if user_input == '1':
            self.interface.updateCurrPage('search_business')
        elif user_input == '2':
            self.interface.updateCurrPage('search_users')
        elif user_input == '3':
            self.interface.updateCurrPage('make_friend')
        elif user_input == '4':
            self.interface.updateCurrPage('review_business')
        elif user_input == 'q':
            self.interface.updateCurrPage('quit')
        else:
            print('Your option input \'' + user_input + '\' is invalid, please try again.')

    def run(self):
        self.main_menu()

    def spc(self):
        print('\n')

