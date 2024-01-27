
class SearchUsers:
    def __init__(self, interface):
        self.interface = interface
        self.connection = interface.connection

        # filter variables
        self.name = ''
        self.min_review_count = ''
        self.min_average_stars = ''

    def search_users(self):
        print('SEARCH USERS: Enter an option number to change a filter.')
        currentFilters = ('Name = \'' + self.name + '\', Min Review Count = \'' + self.min_review_count + '\', '
                          'Min Average Stars = \'' + self.min_average_stars + '\'')
        print('Current Filters: ' + currentFilters + '.')
        print('Filter Options: (1) Name, (2) Min Review Count, (3) Min Average Stars, (r) Run Search, '
              '(e) exit Search Users.')
        user_input = input("Enter your option: ").strip()
        self.spc()

        if user_input == '1':
            self.name_filter()
        elif user_input == '2':
            self.review_filter()
        elif user_input == '3':
            self.star_filter()
        elif user_input == 'e':
            self.exit_search_users()
        elif user_input == 'r':
            self.run_search()
        else:
            print('Invalid input: your option input \'' + user_input + '\' is invalid, please try again.')
            self.spc()

    def name_filter(self):
        print('Name Filter: (To clear filter, enter nothing)')
        user_input = input('Enter a name to update filter: ').strip()
        self.spc()

        if len(user_input) == 0:
            print('You entered nothing, clearing the Name filter.')
            self.spc()
            self.name = ''
            return

        self.name = user_input
        print('Name filter has been updated to: \'' + user_input + '\'')
        self.spc()

    def review_filter(self):
        print('Min Review Count Filter: Input number must be an integer. (To clear filter, enter nothing)')
        user_input = input('Enter a number to update filter: ').strip()
        self.spc()

        if len(user_input) == 0:
            print('You entered nothing, clearing the Min Review Count filter.')
            self.spc()
            self.min_review_count = ''
            return

        # Check if the input can be an int
        try:
            min_rev_count = int(user_input)
        except ValueError:
            print('Invalid count input: your input \'' + user_input + '\' is not valid, please try again.')
            self.min_review_count = ''
            self.spc()
            return

        # Check if the input is negative
        if min_rev_count < 0:
            print('Invalid count input: your input \'' + user_input + '\' is negative, please try again.')
            self.spc()
            self.min_review_count = ''
            return

        print('Min Review Count filter has been updated to \'' + user_input + '\'.')
        self.min_review_count = user_input
        self.spc()

    def star_filter(self):
        print('Min Average of Stars Filter: Input number must be >= 1.0 and <= 5.0 (1.00 >= input <= 5.00),'
              ' and can only be up to two decimal place (e.g. 2.22).')
        print('(To clear filter, enter nothing)')
        user_input = input('Enter a number to update filter: ').strip()
        self.spc()

        if len(user_input) == 0:
            print('You entered nothing, clearing the Min Average of Stars filter.')
            self.spc()
            self.min_average_stars = ''
            return

        # Check if the input can be a float
        try:
            min_stars = float(user_input)
        except ValueError:
            print('Invalid star input: your input \'' + user_input + '\' is not valid, please try again.')
            self.min_average_stars = ''
            self.spc()
            return

        if '.' in user_input:
            non_decimal, decimal = user_input.split('.')
            if len(decimal) > 2:
                print('Invalid star input: your input \'' + user_input + '\' is not valid, please try again.')
                self.min_average_stars = ''
                self.spc()
                return

        if min_stars < 1.00:
            print(
                'Invalid star input: your number input \'' + user_input + '\' is less than 1.0. Please try again.')
            self.min_average_stars = ''
            self.spc()
            return

        if min_stars > 5.00:
            print('Invalid star input: your number input \'' + user_input + '\' is greater than 5.0. '
                                                                            'Please try again.')
            self.min_average_stars = ''
            self.spc()
            return

        print('Min Average of Stars filter has been updated to \'' + user_input + '\'.')
        self.min_average_stars = user_input
        self.spc()

    def run_search(self):
        sqlStatement = ('SELECT user_id, name, review_count, useful, funny, cool, average_stars, yelping_since '
                        'FROM user_yelp')
        sqlWHERE = ' WHERE'

        filter_count = 0

        # Getting name variable
        if len(self.name) != 0:
            sqlWHERE += ' name LIKE \'%' + self.name + '%\''
            filter_count += 1

        # Getting stars variable
        if len(self.min_review_count) != 0:
            if filter_count != 0:
                sqlWHERE += ' AND review_count >= ' + self.min_review_count
            else:
                sqlWHERE += ' review_count >= ' + self.min_review_count
            filter_count += 1

        if len(self.min_average_stars) != 0:
            if filter_count != 0:
                sqlWHERE += ' AND average_stars >= ' + self.min_average_stars
            else:
                sqlWHERE += ' average_stars >= ' + self.min_average_stars
            filter_count += 1

        if filter_count != 0:
            sqlStatement += sqlWHERE

        sqlStatement += ' ORDER BY name'

        cursor = self.connection.cursor()
        cursor.execute(sqlStatement)

        row = cursor.fetchone()
        currentFilters = ('Name = \'' + self.name + '\', Min Review Count = \'' + self.min_review_count +
                          '\', Min Average of Stars = \'' + self.min_average_stars + '\'.')
        if row is None:
            print('Result is empty with current set of filters: ' + currentFilters)
            cursor.close()
            self.spc()
            return

        self.spc()

        row_count = 0
        while row is not None:
            print('| User ID: ' + str(row[0]) + ' | Name: ' + str(row[1]) + ' | Review Count: ' + str(row[2]) +
                  ' | Useful: ' + str(row[3]) + ' | Funny: ' + str(row[4]) + ' | Cool: ' + str(row[5]) +
                  ' | Average Stars: ' + str(row[6]) + ' | Yelping since: ' + str(row[7]) + ' |')
            row = cursor.fetchone()
            row_count += 1
        print('You have ' + str(row_count) + ' results with current filters: ' + currentFilters + '.')
        self.spc()
        cursor.close()

        while True:
            print('Choose what to do next: (1) Continue to search users, (2) Make Friend, (e) exit from Search '
                  'Users')
            user_input = input('Enter option: ').strip()
            self.spc()

            if user_input == '1':
                return
            elif user_input == '2':
                self.go_to_make_friend()
                return
            elif user_input == 'e':
                self.exit_search_users()
                return
            else:
                print('Invalid option input: Please try again.')
                self.spc()

    def exit_search_users(self):
        self.name = ''
        self.min_review_count = ''
        self.min_average_stars = ''
        self.interface.updateCurrPage('main_menu')

    def go_to_make_friend(self):
        self.name = ''
        self.min_review_count = ''
        self.min_average_stars = ''
        self.interface.updateCurrPage('make_friend')

    def spc(self):
        print('\n')

    def run(self):
        self.search_users()

