
class MakeFriend:
    def __init__(self, interface):
        self.interface = interface
        self.connection = interface.connection

    def make_friend(self):
        print('MAKE FRIEND: case-sensitive. (enter nothing to exit Make Friend)')
        user_input = input('Enter a user ID to make a friend with: ').strip()
        self.spc()

        if len(user_input) == 0:
            self.exit_make_friend()
            return

        curr_user = self.interface.user_id

        if user_input == curr_user:
            print('Invalid friend ID: the inputted user ID is the same as your ID, please try again.')
            self.spc()
            return

        check_friend = self.search_friend_id(user_input)
        if check_friend is False:
            print('Invalid friend ID: Cannot find user ID \'' + user_input + '\', please try again.')
            self.spc()
            return

        check_user_friend = self.search_user_friend(curr_user, user_input)
        if check_user_friend is False:
            print('Invalid friend ID: there is already a friendship (\'' + curr_user + '\' and \'' +
                 user_input + '\').')
            print('Please try again.')
            self.spc()
            return

        # Inserting a new friendship
        sqlStatement = 'INSERT INTO friendship(user_id, friend) VALUES(?,?)'
        cursor = self.connection.cursor()
        cursor.execute(sqlStatement, curr_user, user_input)
        self.connection.commit()

        # check if the insert was succesful
        if cursor.rowcount > 0:
            print('Friendship has been made between \'' + curr_user + '\' and \'' + user_input + '\'!')
        else:
            print('Friendship was not able to made. Please try again.')
        cursor.close()

        while True:
            print('Choose what to do next: (1) Continue to make friends, (e) exit from Make Friend.')
            user_input = input('Enter option: ').strip()
            self.spc()

            if user_input == '1':
                return
            elif user_input == 'e':
                self.exit_make_friend()
                return
            else:
                print('Invalid option input: Please try again.')
                self.spc()

    # search if friend ID exists
    def search_friend_id(self, friend_user) -> bool:
        cursor = self.connection.cursor()
        cursor.execute('SELECT user_id '
                       'FROM user_yelp '
                       'WHERE user_id = \'' + friend_user + '\'')

        # this makes the search case-sensitive
        row = cursor.fetchone()
        while row is not None:
            if row[0] == friend_user:
                cursor.close()
                return True
            row = cursor.fetchone()

        cursor.close()
        return False

    # This checks if there is already a friendship between the user's id and inputted id
    def search_user_friend(self, current_user, friend_user) -> bool:
        cursor = self.connection.cursor()
        cursor.execute('SELECT user_id, friend '
                       'FROM friendship '
                       'WHERE friend = \'' + friend_user + '\'')

        row = cursor.fetchone()
        while row is not None:
            if current_user == row[0]:
                cursor.close()
                return False
            row = cursor.fetchone()

        cursor.close()
        return True

    def exit_make_friend(self):
        self.interface.updateCurrPage('main_menu')

    def spc(self):
        print('\n')

    def run(self):
        self.make_friend()