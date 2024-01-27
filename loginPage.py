
class LogIn:
    def __init__(self, interface):
        self.interface = interface
        self.connection = interface.connection
        self.user_id = ''
        print('Welcome to my SQL search application!')

    # user ID's are the ones from datafiles
    def log_in(self):
        print('LOG IN: case-sensitive. (Enter nothing to quit) ')
        user_ID = input('Log in with your yelp user ID: ').strip()
        self.spc()

        if len(user_ID) == 0:
            self.interface.updateCurrPage('quit')
            return

        cursor = self.connection.cursor()
        cursor.execute('SELECT user_id '
                       'FROM user_yelp '
                       'WHERE user_id = \'' + user_ID + '\'')

        # If the user id is found, update interface information of userid
        # this makes the search case-sensitive
        row = cursor.fetchone()
        while row is not None:
            if row[0] == user_ID:
                print('ID found, logging in!')
                self.spc()
                self.interface.updateUserID(user_ID)
                self.interface.updateCurrPage('main_menu')
                cursor.close()
                return
            row = cursor.fetchone()

        print('There is no ID \'' + user_ID + '\', please try again.')
        cursor.close()

    def run(self):
        self.log_in()

    def spc(self):
        print('\n')


